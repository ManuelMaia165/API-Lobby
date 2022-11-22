from app import db, ma

class Lobby(db.Model):
    id : int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user : str = db.Column(db.String(80), unique=True, nullable=False)
    max_player : int = db.Column(db.Integer, nullable=False)
    tema : int = db.Column(db.Integer, nullable=False)
    tempo : int = db.Column(db.Integer, nullable=False)
    status : int = db.Column(db.Integer, nullable=False)

    def __init__(self, user : str, max_player : int, tema : int, tempo : int, status = 1):
        self.user : str = user
        self.max_player : int = max_player
        self.tema : int = tema
        self.tempo : int = tempo
        self.status : int = status

class LobbySchema(ma.Schema):
    class Meta:
        fields = ('id', 'user', 'max_player', 'tema', 'tempo', 'status')

lobby_schema = LobbySchema()
lobbys_schema = LobbySchema(many=True)