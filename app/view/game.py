import pika
import pika.exceptions
import json
from .player import PlayerController
from .question import QuestionController
from .alternative import AlternativeController, AlternativeSchema
from .lobby import LobbyController
from .rabbitMQ import RabbitMQClient
from .round import Round

player_controler = PlayerController()
alternative_controller = AlternativeController()
question_controller = QuestionController()
lobby_controller = LobbyController()
alternative_schema = AlternativeSchema()



class Game:
    def __init__(self, id_lobby, rounds, host='localhost'):
        self.id_lobby = id_lobby
        self.rounds = rounds
        self.host = host
        self.current_round = 0
        self.active_players = []
        self.rabbitmq_client = RabbitMQClient(host)

    def start(self, theme):
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

    def _start_round(self):
        # Obtenha a pergunta e as alternativas da rodada atual a partir da lista
        question = self.questions[self.current_round - 1]
        alternatives = self.alternatives[self.current_round - 1]
        round = Round(self, question, alternatives)
        self._send_question(round)

    def _end_round(self, round):
        # Atualize a pontuação de cada jogador
        for user, answer in round.answers.items():
            score = player_controler.update_score(user, answer)

        # Obtenha o ranking dos jogadores
        ranking = player_controler.get_players_by_lobby(self.id_lobby)

        # Envie o ranking para os jogadores
        self._send_ranking(ranking)

        if self.current_round < self.rounds:
            self.current_round += 1
            self._start_round()
        else:
            self._finish_game()

    def _send_question(self, round):
        try:
            self.rabbitmq_client.connect()
        except pika.exceptions.AMQPConnectionError:
            print("Error connecting to RabbitMQ server")
            return

        try:
            # Serialize as alternativas usando o AlternativeSchema
            serialized_alternatives = alternative_schema.dump(round.alternatives, many=True)

            self.rabbitmq_client.send_message(
                exchange='lobbies',
                routing_key=self.id_lobby,
                body=json.dumps(
                    {'type': 'question', 'question': round.question.question, 'alternatives': serialized_alternatives})
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