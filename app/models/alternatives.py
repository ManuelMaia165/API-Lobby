from app import db, ma

class Alternative(db.Model):
    __tablename__ = 'alternatives'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)
    text = db.Column(db.String(255), nullable=False)


class AlternativeSchema(ma.Schema):
    """Esquema para serializar/deserializar alternativas."""

    class Meta:
        fields = ('id', 'question_id', 'text')

alternative_schema = AlternativeSchema()
alternative_schema_schema = AlternativeSchema(many=True)