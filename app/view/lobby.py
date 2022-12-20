from app import db
from flask import request, jsonify
from ..models.lobby import Lobby, lobby_schema, lobbys_schema



class LobbyController:
    def create_lobby(self):
        # Obtém os dados da requisição
        user = request.json['user']
        max_player = request.json['max_player']
        tema = request.json['tema']
        tempo = request.json['tempo']

        # Cria um novo lobby com os dados obtidos
        new_lobby = Lobby(user, max_player, tema, tempo)

        # Adiciona o novo lobby ao banco de dados
        db.session.add(new_lobby)
        db.session.commit()

        # Retorna o lobby criado
        return lobby_schema.jsonify(new_lobby)

    def update_lobby(self, id):
        # Obtém o lobby com o ID especificado
        lobby = Lobby.query.get(id)

        # Verifica se o lobby existe
        if lobby:
            # Obtém os dados de atualização da requisição
            user = request.json['user']
            max_player = request.json['max_player']
            tema = request.json['tema']
            tempo = request.json['tempo']

            # Atualiza os campos do lobby com os novos dados
            lobby.user = user
            lobby.max_player = max_player
            lobby.tema = tema
            lobby.tempo = tempo

            # Salva as alterações no banco de dados
            db.session.commit()

            # Retorna o lobby atualizado
            return lobby_schema.jsonify(lobby)
        else:
            # Retorna um erro 404 (não encontrado)
            return {'message': 'Lobby not found'}, 404

    def get_lobby(self, id):
        # Obtém o lobby com o ID especificado
        lobby = Lobby.query.get(id)

        # Verifica se o lobby existe
        if lobby:
            # Retorna o lobby
            return lobby_schema.jsonify(lobby)
        else:
            # Retorna um erro 404 (não encontrado)
            return {'message': 'Lobby not found'}, 404

    def get_all_lobbys(self):
        # Obtém todos os lobbys
        lobbys = Lobby.query.all()

        # Retorna a lista de lobbys
        return lobbys_schema.jsonify(lobbys)

    def delete_lobby(self, id):
        # Obtém o lobby com o ID especificado
        lobby = Lobby.query.get(id)

        # Verifica se o lobby existe
        if lobby:
            # Exclui o lobby do banco de dados
            db.session.delete(lobby)
            db.session.commit()

            # Retorna uma mensagem de sucesso
            return {'message': 'Lobby deleted'}
        else:
            # Retorna um erro 404 (não encontrado)
            return {'message': 'Lobby not found'}, 404

    def finish_game(self, id):
        # Obtém o lobby com o ID especificado
        lobby = Lobby.query.get(id)

        # Verifica se o lobby existe
        if lobby:
            # Atualiza o status do lobby para 0 (finalizado)
            lobby.status = 0

            # Salva as alterações no banco de dados
            db.session.commit()

            # Retorna o lobby atualizado
            return lobby_schema.jsonify(lobby)
        else:
            # Retorna um erro 404 (não encontrado)
            return {'message': 'Lobby not found'}, 404
