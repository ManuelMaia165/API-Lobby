from app import app
from ..view.lobby import LobbyController
from ..view.player import PlayerController

lobby_controller = LobbyController()
player_controller = PlayerController()

@app.route('/lobby', methods=['POST'])
def create_lobby():
    return lobby_controller.create_lobby()

@app.route('/lobby/<id>', methods=['PUT'])
def update_lobby(id):
    return lobby_controller.update_lobby(id)

@app.route('/lobby/<id>', methods=['GET'])
def get_lobby(id):
    return lobby_controller.get_lobby(id)

@app.route('/lobbys', methods=['GET'])
def get_all_lobbys():
    return lobby_controller.get_all_lobbys()

@app.route('/lobby/<id>', methods=['DELETE'])
def delete_lobby(id):
    return lobby_controller.delete_lobby(id)

@app.route('/player', methods=['POST'])
def join_lobby():
    return player_controller.join_lobby()

@app.route('/players/<id_lobby>', methods=['GET'])
def get_players_by_lobby(id_lobby):
    return player_controller.get_players_by_lobby(id_lobby)

@app.route('/players/<id_lobby>/<user>', methods=['GET'])
def get_player_by_lobby(id_lobby, user):
    return player_controller.get_player_by_lobby(id_lobby, user)

@app.route('/lobby/<int:id_lobby>/player/<int:user>/score', methods=['PUT'])
def update_player_score(id_lobby, user):
    score = request.json['score']
    return PlayerController().update_score(id_lobby, user, score)

@app.route('/lobby/<int:id_lobby>/player/<string:user>', methods=['DELETE'])
def leave_lobby(id_lobby, user):
    return player_controller.leave_lobby(id_lobby, user)


