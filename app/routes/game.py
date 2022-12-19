from app import app
from flask import request, jsonify
from ..view.game import Game



@app.route('/start', methods=['POST'])
def start_game():
    # obtenha os parâmetros da solicitação
    data = request.get_json()
    id_lobby = data['id_lobby']
    rounds = data['rounds']
    theme = data['theme']

    # crie uma instância de Game
    game = Game(id_lobby, rounds)

    # inicie o jogo
    game.start(theme)

    return 'Jogo iniciado com sucesso!'