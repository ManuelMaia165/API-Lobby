from app import app
from flask import request
from ..view.game import Game


@app.route('/start_game', methods=['POST'])
def start_game():
    data = request.get_json()
    id_lobby = data['id_lobby']
    theme = data['theme']
    rounds = data['rounds']

    game = Game(id_lobby, rounds)
    game.start(theme)

    return 'Jogo iniciado'