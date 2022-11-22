from flask import request, jsonify


from app import db
from sqlalchemy.sql import func
from ..models.lobbyAux import LobbyAux, lobbyAux_schema


def post_lobbyAux(id_sala):
    id_sala = id_sala
    user = request.json['user']
    pontuacao = 0
    player = LobbyAux(id_sala, user, pontuacao)

    try:
        db.session.add(player)
        db.session.commit()
        return jsonify({'mensagem': 'Registrado com sucesso','ID': player.id}), 201
    except:
        return jsonify({'mensagem': 'Não criado'}), 500


def update_lobbyAux(id):
    id_sala : int = request.json['id_sala']
    user : str = request.json['user']
    pontuacao : int = request.json['pontuacao']

    lobby : LobbyAux = LobbyAux.query.get(id)

    print(lobby)

    if not lobby:
        return jsonify({'mensagem': 'Lobby não existe'})

    try:
        lobby.user = user
        lobby.id_sala = id_sala
        lobby.pontuacao = pontuacao
        db.session.commit()
        return jsonify({'mensagem': 'Registrado com sucesso'}), 201
    except:
        return jsonify({'mensagem': 'Não criado'}), 500


def get_lobbyAux(id):
    lobby = LobbyAux.query.get(id)
    if lobby:
        results = lobbyAux_schema.dumps(lobby)
        return results, 201

    return jsonify({'mensagem': 'O usuario não existe'}), 404

def get_all_lobbysAux():
    lobby = LobbyAux.query.all()
    print(lobby)
    lista = []
    if lobby:
        for lobbys in lobby:
            dicts = lobbyAux_schema.dump(lobbys)
            lista.append(dicts)
        print(lista)
        return lista, 201



    return jsonify({'mensagem': 'O usuario não existe'}), 404


def get_top_pontos():
    lobby = db.session.query(LobbyAux.user, func.sum(LobbyAux.pontuacao).label("sum")).group_by(LobbyAux.user)
    print(lobby)
    lista = []
    if lobby:
        for lobbys in lobby:
            dicts = lobbyAux_schema.dump(lobbys)
            lista.append(dicts)
        print(lista)
        return lista, 201

    return jsonify({'mensagem': 'A tabela está vazia'}), 404
