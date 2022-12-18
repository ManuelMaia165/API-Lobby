import random
import select
import threading
import time
import requests
from .lobby import LobbyController
from .player import PlayerController


lobby_controller = LobbyController()
player_controller = PlayerController()

class Game:
    def __init__(self, clients, questions, num_rounds, time_limit, id_lobby):
        self.clients = clients
        self.questions = questions
        self.num_rounds = num_rounds
        self.time_limit = time_limit
        self.id_lobby = id_lobby
        self.scores = {}
        self.current_question = 0  # Adiciona a variável de controle de pergunta

    def play_round(self, client):
        # Seleciona a pergunta atual
        question = self.questions[self.current_question]

        # Envia a pergunta e as alternativas para o cliente
        client.send(question["question"].encode())
        for choice in question["choices"]:
            client.send(choice.encode())

        # Recebe respostas e tempos do cliente
        ready, _, _ = select.select([client], [], [], self.time_limit * 4)  # Aumenta o tempo de espera para 4 vezes o limite
        if client in ready:
            answer = client.recv(1024).decode()
            time = client.recv(1024).decode()
        else:
            player_controller.leave_lobby(self.id_lobby, client.recv(1024).decode())
            self.clients.remove(client)
            return

        # Verifica se a resposta é correta e atualiza a pontuação do jogador no banco de dados, se necessário
        if answer == question["correct_answer"]:
            user = client.recv(1024).decode()  # Obtém o usuário do jogador
            score = time * 10  # Calcula a pontuação do jogador baseado no tempo
            if user not in self.scores:  # Verifica se a pontuação já foi atualizada
                self.scores[user] = score  # Atualiza o score no dicionário
                result = player_controller.update_score(self.id_lobby, user, score)  # Atualiza o score no banco de dados
                if 'error' in result:
                    # Trata o erro aqui
                    pass
        else:
            # Trata a resposta incorreta aqui, se desejado
            pass

        # Incrementa o índice da pergunta atual
        self.current_question += 1


    def send_ranking_to_frontend(self, ranking):
        # Envia o ranking para o front-end através de uma chamada HTTP POST
        response = requests.post("http://frontend.com/ranking", json=ranking)

        # Verifica se a chamada foi bem-sucedida
        if response.status_code == 200:
            print("Ranking enviado com sucesso para o front-end")
        else:
            print("Erro ao enviar ranking para o front-end:", response.text)

    def start_game(self):
        # Loop pelas rodadas do jogo
        for round_num in range(self.num_rounds):
            # Cria uma thread para cada jogador
            threads = []
            for client in self.clients:
                t = threading.Thread(target=self.play_round, args=(client,))
                t.start()
                threads.append(t)

            # Aguarda todas as threads finalizarem
            for t in threads:
                t.join()

            # Exibe o ranking após cada rodada
            time.sleep(self.time_limit * 2)  # Aguarda o dobro do tempo especificado
            ranking = player_controller.get_players_by_lobby(self.id_lobby)

            # Envia o ranking para o front-end
            self.send_ranking_to_frontend(ranking)



