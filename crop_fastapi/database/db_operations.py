from .models import RecommendationModel
from .schemas import RecommendationBase
from sqlalchemy.orm import Session


def get_recommendations(db: Session):
    record = db.query(RecommendationModel).all()
    return record


def get_recommendation(recommendation_id: int, db: Session):
    record = db.query(RecommendationModel).get(recommendation_id)
    return record


def create_recommendation(recommendation: RecommendationBase, db: Session):
    record = RecommendationModel(
            nitrogen=recommendation.nitrogen,
            phosphorous=recommendation.phosphorous,
            potassium=recommendation.potassium,
            temperature=recommendation.temperature,
            humidity=recommendation.humidity,
            ph=recommendation.ph,
            rainfall=recommendation.rainfall,
            label=recommendation.label)
    db.add(record)
    db.commit()
    return record


def modify_recommendation(recommendation_id: int, db: Session):
    record = db.query(RecommendationModel).get(recommendation_id)
    record.nitrogen = record.nitrogen
    record.phosphorous = record.phosphorous
    record.potassium = record.potassium,
    record.temperature = record.temperature,
    record.humidity = record.humidity,
    record.ph = record.ph,
    record.rainfall = record.rainfall,
    record.label = record.label
    db.commit()
    return record


def delete_recommendation(recommendation_id: int, db: Session):
    db.query(RecommendationModel).get(recommendation_id).delete()
    db.commit()
