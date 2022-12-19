from app import db, ma

class Question(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    text = db.Column(db.String(255), nullable=False)
    correct_answer = db.Column(db.String(255), nullable=False)
    theme = db.Column(db.String(255), nullable=False)

class QuestionSchema(ma.Schema):
    class Meta:
        fields = ('id', 'text', 'correct_answer', 'theme')

question_schema = QuestionSchema()
question_schemas = QuestionSchema(many=True)