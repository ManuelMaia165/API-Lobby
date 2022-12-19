from app import app
from flask import request, jsonify
from ..view.game import Game



@app.route('/games/<int:id_lobby>/start', methods=['POST'])
def start_game(id_lobby):
    data = request.get_json()
    theme = data['theme']
    rounds = data['rounds']

    game = Game(id_lobby, rounds)
    game.start(theme)

    return 'Jogo iniciado com sucesso'