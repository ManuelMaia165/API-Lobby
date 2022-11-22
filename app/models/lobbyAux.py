from app import db, ma


class LobbyAux(db.Model):
    id : int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_sala : int = db.Column(db.Integer, autoincrement=True, nullable=False)
    user : str = db.Column(db.String(80), unique=False, nullable=False)
    pontuacao : str = db.Column(db.Integer, nullable=False)

    def __init__(self, id_sala, user, pontuacao=0):
        self.id_sala = id_sala
        self.user = user
        self.pontuacao = pontuacao


class LobbyAuxSchema(ma.Schema):
    class Meta:
        fields = ('id', 'user','id_sala','sum')


lobbyAux_schema = LobbyAuxSchema()
lobbysAux_schema = LobbyAuxSchema(many=True)
