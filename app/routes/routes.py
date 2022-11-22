from app import app
from flask import jsonify
from ..view import lobby, lobbyAux

@app.route('/', methods=['GET'])
def root():
    return jsonify({'mensagem': 'Deu bom'})

@app.route('/lobbys', methods=['POST'])
def post_lobby():
    return lobby.post_lobby()

@app.route('/lobbys/<id>', methods=['PUT'])
def put_lobby(id):
    return lobby.update_lobby(id)

@app.route('/lobbys/<id>', methods=['GET'])
def get_lobby(id):
    return lobby.get_lobby(id)

@app.route('/lobbys/', methods=['GET'])
def get_all_lobbys():
    return lobby.get_all_lobbys()

## Jogadores


@app.route('/lobbysaux/<id_sala>', methods=['POST'])
def post_lobbyAux(id_sala):
    return lobbyAux.post_lobbyAux(id_sala)

@app.route('/lobbysaux/<id>', methods=['PUT'])
def put_lobbyAux(id):
    return lobbyAux.update_lobbyAux(id)

@app.route('/lobbysaux/<id>', methods=['GET'])
def get_lobbyAux(id):
    return lobbyAux.get_lobbyAux(id)

@app.route('/lobbysaux/', methods=['GET'])
def get_all_lobbysAux():
    return lobbyAux.get_all_lobbysAux()

@app.route('/lobbysaux/ranking/', methods=['GET'])
def get_top_pontos():
    return lobbyAux.get_top_pontos()
