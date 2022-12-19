import pika
import json
from .player import PlayerController
from .question import QuestionController
from .alternative import AlternativeController

player_controler = PlayerController()
alternative_controller = AlternativeController()
question_controller = QuestionController()

class Game:
    def __init__(self, id_lobby, rounds, host='localhost'):
        self.id_lobby = id_lobby
        self.rounds = rounds
        self.host = host
        self.current_round = 0
        self.connection = None
        self.channel = None

    def start(self, theme):
        questions = []
        alternatives = []

        for i in range(self.rounds):
            question = question_controller.get_random_question_by_theme(theme)
            questions.append(question)
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

    def _finish_game(self):
        # Implemente o método para finalizar o jogo aqui
        pass

    def _connect(self):
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.host)
        )
        self.channel = self.connection.channel()

    def _close_connection(self):
        self.connection.close()

    def _send_question(self, round):
        self._connect()
        self.channel.exchange_declare(exchange='lobbies', exchange_type='topic')
        self.channel.basic_publish(
            exchange='lobbies',
            routing_key=f'lobby.{self.id_lobby}',
            body=json.dumps({'question': round.question, 'alternatives': round.alternatives})
        )
        self._close_connection()

    def _send_ranking(self, ranking):
        self._connect()
        self.channel.exchange_declare(exchange='lobbies', exchange_type='topic')
        self.channel.basic_publish(
            exchange='lobbies',
            routing_key=f'lobby.{self.id_lobby}',
            body=json.dumps({'ranking': ranking})
        )



class Round:
    def __init__(self, game, question, alternatives):
        self.game = game
        self.question = question
        self.alternatives = alternatives
        self.answers = {}

    def add_answer(self, user, answer):
        self.answers[user] = answer

    def finish(self):
        self.game._end_round(self)

    def get_correct_answer(self):
        # Implemente a lógica para determinar qual é a resposta correta de acordo com as regras do jogo aqui
        return self.alternatives[0]  # considera que a primeira alternativa é a correta