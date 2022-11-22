from app import db
from flask import request, jsonify
from ..models.lobby import Lobby, lobby_schema, lobbys_schema
from ..view import lobbyAux
import json

def post_lobby():
    user = request.json['user']
    max_player = request.json['max_player']
    tema = request.json['tema']
    tempo = request.json['tempo']
    status = 1
    lobby = Lobby(user, max_player, tema, tempo, status)

    try:
        db.session.add(lobby)
        db.session.commit()
        return jsonify({'mensagem': 'Registrado com sucesso','ID' : lobby.id}), 201
    except:
        return jsonify({'mensagem': 'Não criado'}), 500


def update_lobby(id):
    user = request.json['user']
    max_player = request.json['max_player']
    tema = request.json['tema']
    tempo = request.json['tempo']
    status = request.json['status']
    lobby = Lobby.query.get(id)

    print(lobby)

    if not lobby:
        return jsonify({'mensagem': 'Lobby não existe'})

    try:
        lobby.user = user
        lobby.max_player = max_player
        lobby.tema = tema
        lobby.tempo = tempo
        lobby.status = status
        db.session.commit()
        return jsonify({'mensagem': 'Registrado com sucesso'}), 201
    except:
        return jsonify({'mensagem': 'Não criado'}), 500


def get_lobby(id):
    lobby = Lobby.query.get(id)
    if lobby:
        results = lobby_schema.dumps(lobby)
        return results, 201

    return jsonify({'mensagem': 'O usuario não existe'}), 404

def get_all_lobbys():
    lobby = Lobby.query.all()
    print(lobby)
    lista = []
    if lobby:
        for lobbys in lobby:
            dicts = lobby_schema.dump(lobbys)
            lista.append(dicts)
        print(lista)
        return lista, 201

    return jsonify({'mensagem': 'O usuario não existe'}), 404


