from .models import RecommendationModel
from .schemas import RecommendationBase
from sqlalchemy.orm import Session


def model_to_base(record: RecommendationModel):
    recommendation = RecommendationBase(
            nitrogen=record.nitrogen,
            phosphorous=record.phosphorous,
            potassium=record.potassium,
            temperature=record.temperature,
            humidity=record.humidity,
            ph=record.ph,
            rainfall=record.rainfall,
            label=record.label)
    return recommendation


def get_recommendations(db: Session):
    records = db.query(RecommendationModel).all()
    recommendations = [model_to_base(record) for record in records]
    return recommendations


def get_recommendation(recommendation_id: int, db: Session):
    record = db.query(RecommendationModel).get(recommendation_id)
    recommendation = model_to_base(record)
    return recommendation


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
    return recommendation


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
    recommendation = model_to_base(record)
    return recommendation


def delete_recommendation(recommendation_id: int, db: Session):
    db.query(RecommendationModel).get(recommendation_id).delete()
    db.commit()
    records = db.qeury(RecommendationModel).all()
    recommendations = [model_to_base(record) for record in records]
    return recommendations
