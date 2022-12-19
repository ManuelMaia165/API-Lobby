from app import db
from ..models.alternatives import Alternative

class AlternativeController:
    def get_alternatives_by_question_id(question_id):
        alternatives = db.session.query(Alternative).filter(Alternative.question_id == question_id).all()
        return alternatives