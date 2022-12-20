from app import app
from flask import request
from ..view.game import Game
from ..view.rabbitMQ import RabbitMQClient
import json

rabbitmq_client = RabbitMQClient()

@app.route('/start_game', methods=['POST'])
def start_game():
    data = request.get_json()
    id_lobby = data['id_lobby']
    theme = data['theme']
    rounds = data['rounds']
    time_left = data['time_left']

    game = Game(id_lobby, rounds, theme)
    game.start_round(time_left)

@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    data = request.get_json()
    id_lobby = data['id_lobby']
    user = data['user']
    answer = data['answer']
    time_left = data['time_left']

    game = Game.get_game_by_lobby_id(id_lobby)
    round = game.current_round
    round.add_answer(user, answer, time_left)

    if round.is_finished():
        round.finish_round()

@app.route('/finish_round', methods=['POST'])
def finish_round():
    data = request.get_json()
    id_lobby = data['id_lobby']

    game = Game.get_game_by_lobby_id(id_lobby)
    round = game.current_round
    game.end_round(round)

    if game.current_round <= game.rounds:
        game.start_round()
    else:
        game.finish_game()
