
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