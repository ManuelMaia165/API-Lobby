from .player import PlayerController
player_controller = PlayerController()

class Round:
    def __init__(self, game, question, alternatives, time_left):
        self.game = game
        self.question = question
        self.alternatives = alternatives
        self.answers = {}
        self.time_left = time_left  # adicione o tempo restante como um atributo da rodada

    def add_answer(self, user, answer, time_left):
        self.answers[user] = {'answer': answer, 'time_left': time_left}

    def finish(self):
        # Obtenha o tempo restante e atribua a pontuação de acordo com a regra estabelecida
        time_left = self.time_left

        # Atualize a pontuação de cada jogador
        for user, answer_data in self.answers.items():
            answer = answer_data['answer']
            if answer == self.question.correct_answer:
                # Se a resposta do jogador for correta, adicione pontos à sua pontuação
                score = max(0,
                            100 - time_left)  # a pontuação é 100 pontos menos o tempo restante, mas nunca menor que zero
                player_controller.update_score(user, score)

    def get_score(self):
        scores = []
        for user, (answer, time_left) in self.answers.items():
            score = max(0, 100 - time_left)  # a pontuação é 100 pontos menos o tempo restante, mas nunca menor que zero
            scores.append(score)
        return scores