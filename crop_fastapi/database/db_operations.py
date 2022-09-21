from .models import RecommendationModel
from .schemas import RecommendationBase
from sqlalchemy.orm import Session


def model_to_base(record: RecommendationModel):
    recommendation = RecommendationBase(**record.__dict__)
    return recommendation


def get_recommendations(db: Session):
    recommendation = db.query(RecommendationModel).all()
    return recommendation


def get_recommendation(recommendation_id: int, db: Session):
    recommendation = db.query(RecommendationModel).get(recommendation_id)
    return recommendation


def create_recommendation(recommendation: RecommendationBase, db: Session):
    try:
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
        return 201
    except Exception as err:
        print('\n\n\n')
        print(err)
        print('\n\n\n')
        return err


def modify_recommendation(recommendation_id: int, recommendation: RecommendationBase, db: Session):
    record = db.query(RecommendationModel).get(recommendation_id)
    if record is None:
        return None
    try:
        record.nitrogen = recommendation.nitrogen
        record.phosphorous = recommendation.phosphorous
        record.potassium = recommendation.potassium,
        record.temperature = recommendation.temperature,
        record.humidity = recommendation.humidity,
        record.ph = recommendation.ph,
        record.rainfall = recommendation.rainfall,
        record.label = recommendation.label
        db.commit()
        return 204
    except Exception as err:
        print('\n\n\n')
        print(err)
        print('\n\n\n')
        return err


def delete_recommendation(recommendation_id: int, db: Session):
    recommendation = db.query(RecommendationModel).get(recommendation_id)
    if recommendation is None:
        return None
    db.query(RecommendationModel).filter(RecommendationModel.id==recommendation_id).delete()
    db.commit()
    recommendations = db.query(RecommendationModel).all()
    return recommendations
