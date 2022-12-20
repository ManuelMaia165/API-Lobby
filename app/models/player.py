from app import db, ma

class Player(db.Model):
    """Classe que representa um lobby auxiliar no banco de dados."""

    id_ : int = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_lobby : int = db.Column(db.Integer, autoincrement=True, nullable=False)
    user : str = db.Column(db.String(80), unique=False, nullable=False)
    pontuacao : int = db.Column(db.Integer, nullable=False)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)



class PlayerSchema(ma.Schema):
    """Esquema para serializar/deserializar lobbys auxiliares."""

    class Meta:
        fields = ('id', 'user','id_sala','pontuacao')

player_schema = PlayerSchema()
player_schema_schema = PlayerSchema(many=True)