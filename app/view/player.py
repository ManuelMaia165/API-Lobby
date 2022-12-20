from app import db
from flask import request
from ..models.player import Player, player_schema, player_schema_schema
from ..models.lobby import Lobby

class PlayerController:
    def join_lobby(self):
        # Obtém os dados da requisição
        id_lobby = request.json['id_lobby']
        user = request.json['user']
        pontuacao = request.json['pontuacao']

        # Verifica se o lobby existe e se o seu status é 1
        lobby = Lobby.query.get(id_lobby)
        if lobby and lobby.status == 1:
            # Verifica se o player já está associado a outro lobby com status 1
            player = Player.query.filter_by(user=user, id_lobby=lobby.id).first()
            if player:
                return {'message': 'Player already associated with a lobby'}, 400

            # Cria um novo player com os dados obtidos
            new_player = Player(user=user, id_lobby=id_lobby, pontuacao=pontuacao)

            # Adiciona o novo player ao banco de dados
            db.session.add(new_player)
            db.session.commit()

            # Retorna o player criado
            return player_schema.jsonify(new_player)
        else:
            # Retorna um erro 400 (solicitação inválida)
            return {'message': 'Invalid lobby'}, 400

    def get_player_by_lobby(self, id_lobby, user):
        # Obtém o jogador do lobby especificado
        player = Player.query.filter_by(user=user, id_lobby=id_lobby).first()

        # Verifica se o jogador existe e está associado ao lobby especificado
        if player:
            # Retorna o jogador
            return player_schema.jsonify(player)
        else:
            # Retorna um erro 404 (não encontrado)
            return {'message': 'Player not found or not associated with the specified lobby'}, 404

    def get_players_by_lobby(self, id_lobby):
        # Obtém todos os jogadores do lobby especificado
        players = Player.query.filter_by(id_lobby=id_lobby).all()

        # Retorna a lista de jogadores
        return player_schema_schema.jsonify(players)

    def leave_lobby(self, id_lobby, user):
        # Verifica se o lobby existe
        lobby = Lobby.query.get(id_lobby)
        if lobby and lobby.status == 1:
            # Obtém o jogador que deseja sair do lobby
            player = Player.query.filter_by(user=user, id_lobby=id_lobby).first()

            # Verifica se o jogador existe e está associado ao lobby especificado
            if player:
                # Remove o jogador do banco de dados
                db.session.delete(player)
                db.session.commit()

                # Retorna uma mensagem de sucesso
                return {'message': 'Player successfully removed from lobby'}
            else:
                # Retorna um erro 400 (solicitação inválida)
                return {'message': 'Player not found or not associated with the specified lobby'}, 400
        else:
            # Retorna um erro 400 (solicitação inválida)
            return {'message': 'Invalid lobby'}, 400

    def update_score(self, id_lobby, user, score):
        # Obtém o jogador do lobby especificado
        player = Player.query.filter_by(user=user, id_lobby=id_lobby).first()

        # Verifica se o jogador existe e está associado ao lobby especificado
        if player:
            # Atualiza a pontuação do jogador com a soma do valor atual e do valor passado como parâmetro
            player.score += score

            # Salva as alterações no banco de dados
            db.session.commit()

            # Retorna uma mensagem de sucesso
            return {'message': 'Player score successfully updated'}
        else:
            # Retorna um erro 400 (solicitação inválida)
            return {'message': 'Player not found or not associated with the specified lobby'}, 400