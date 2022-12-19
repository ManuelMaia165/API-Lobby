from app.models.question import Question
from sqlalchemy import func

class QuestionController:
    def get_all_questions(self):
        return Question.query.all()

    def get_random_question_by_theme(self, theme):
        return (
            Question.query
            .filter_by(theme=theme)
            .order_by(func.random())
            .first()
        )