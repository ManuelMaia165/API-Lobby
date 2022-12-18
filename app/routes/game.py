from app import app
from flask import request
from ..view.game import Game


@app.route('/start-game', methods=['POST'])
def start_game():
    # Obtém os parâmetros da requisição
    clients = request.json['clients']
    questions = request.json['questions']
    num_rounds = request.json['num_rounds']
    time_limit = request.json['time_limit']
    id_lobby = request.json['id_lobby']

    # Cria uma instância da classe Game e inicia o jogo
    game = Game(clients, questions, num_rounds, time_limit, id_lobby)
    game.start_game()

    return "Jogo iniciado com sucesso"