import pika
import pika.exceptions
import json
from .player import PlayerController
from .question import QuestionController, QuestionSchema, question_schemas
from .alternative import AlternativeController, AlternativeSchema, alternative_schema_schema
from .lobby import LobbyController
from .rabbitMQ import RabbitMQClient
from .round import Round

player_controler = PlayerController()
alternative_controller = AlternativeController()
question_controller = QuestionController()
lobby_controller = LobbyController()
alternative_schema = AlternativeSchema()



class Game:
    def __init__(self, id_lobby, rounds, theme, host='localhost'):
        self.id_lobby = id_lobby
        self.rounds = rounds
        self.theme = theme
        self.host = host
        self.current_round = 0
        self.active_players = []
        self.rabbitmq_client = RabbitMQClient(host)

    def start(self, theme):
        self.theme = theme
        if self.rounds <= 0:
            raise ValueError("Number of rounds must be greater than zero")
        questions = []
        alternatives = []

        for i in range(self.rounds):
            question = question_controller.get_random_question_by_theme(theme)
            questions.append(question)
            print(question.id)
            round_alternatives = alternative_controller.get_alternatives_by_question_id(question.id)
            alternatives.append(round_alternatives)

        self.questions = questions
        self.alternatives = alternatives
        self.current_round = 1
        self._start_round()

    def start_round(self, time_left):
        # Obtenha uma pergunta aleatória do banco de dados
        question = QuestionController().get_random_question_by_theme(self.theme)

        # Obtenha as alternativas da pergunta
        alternatives = AlternativeController().get_alternatives_by_question_id(question.id)

        # Inicie uma nova rodada com a pergunta e as alternativas
        round = Round(self, question, alternatives, time_left)

        # Armazene a rodada atual
        self.current_round = round

    def end_round(self, round):
        # Atualize a pontuação de cada jogador
        for user, answer in round.answers.items():
            # Multiplique o tempo restante pelo fator de pontuação
            score = answer['time_left'] * self.point_factor

            # Adicione a pontuação ao placar do jogador
            player_controler.update_score(user, score)
        # Envie o ranking atualizado para todos os jogadores
        message = {
            'type': 'ranking_updated',
            'ranking': self.scores
        }
        self._send_message_to_all_players(message)

        # Se ainda houver rodadas, inicie a próxima
        if self.current_round < self.rounds:
            self.start_round()
        else:
            self.finish_game()

    def _send_question(self, round):
        try:
            self.rabbitmq_client.connect()
        except pika.exceptions.AMQPConnectionError:
            print("Error connecting to RabbitMQ server")
            return

        try:
            # Serialize the alternatives using the AlternativeSchema
            serialized_alternatives = alternative_schema.dump(round.alternatives, many=True)

            self.rabbitmq_client.send_message(
                exchange='lobbies',
                routing_key=self.id_lobby,
                body=json.dumps(
                    {'type': 'question', 'question': round.question.text, 'alternatives': serialized_alternatives})
            )
        except pika.exceptions.AMQPError:
            print("Error sending message to RabbitMQ server")

        self.rabbitmq_client.close_connection()

    def _send_ranking(self, ranking):
        # Envie o ranking para os jogadores
        try:
            self.rabbitmq_client.connect()
        except pika.exceptions.AMQPConnectionError:
            print("Error connecting to RabbitMQ server")
            return

        try:
            self.rabbitmq_client.send_message(
                exchange='lobbies',
                routing_key=self.id_lobby,
                body=json.dumps({'type': 'ranking', 'ranking': ranking})
            )
        except pika.exceptions.AMQPError:
            print("Error sending message to RabbitMQ server")

        self.rabbitmq_client.close_connection()

    def _finish_game(self):
        # Envie a mensagem de fim de jogo para os jogadores
        try:
            self.rabbitmq_client.connect()
        except pika.exceptions.AMQPConnectionError:
            print("Error connecting to RabbitMQ server")
            return

        try:
            self.rabbitmq_client.send_message(
                exchange='lobbies',
                routing_key=self.id_lobby,
                body=json.dumps({'type': 'finish'})
            )
        except pika.exceptions.AMQPError:
            print("Error sending message to RabbitMQ server")

        self.rabbitmq_client.close_connection()

    def disconnect_player(self, player_id):
        if player_id in self.active_players:
            self.active_players.remove(player_id)

        try:
            self.rabbitmq_client.connect()
        except pika.exceptions.AMQPConnectionError:
            print("Error connecting to RabbitMQ server")
            return

        try:
            self.rabbitmq_client.send_message(
                exchange='lobbies',
                routing_key=player_id,
                body=json.dumps({'type': 'disconnect'})
            )
        except pika.exceptions.AMQPError:
            print("Error sending message to RabbitMQ server")

        self.rabbitmq_client.close_connection()

    def receive_answer(self, user, answer, time_left):
        # Adicione a resposta do jogador à rodada atual
        self.current_round.add_answer(user, answer, time_left)

    def add_answer(self, user, answer, time_left):
        # Obtenha o round atual
        round = self.current_round

        # Adicione a resposta do jogador ao round
        round.add_answer(user, answer, time_left)

        # Verifique se todos os jogadores já responderam ou se o tempo esgotou
        if round.is_finished():
            round.finish()
        else:
            # Envie uma mensagem para o jogador informando o tempo restante
            message = {
                'type': 'time_left',
                'time_left': time_left
            }
            self.rabbitmq_client.send_message(exchange='', routing_key=user, body=json.dumps(message))