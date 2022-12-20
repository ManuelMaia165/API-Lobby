from app import db
from ..models.alternatives import Alternative, AlternativeSchema, alternative_schema_schema

class AlternativeController:
    def get_alternatives_by_question_id(self, question_id):
        alternatives = db.session.query(Alternative).filter(Alternative.question_id == question_id).all()
        return alternatives