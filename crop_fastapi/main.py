from typing import List
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import config, db_operations, models, schemas
# import pandas as pd

models.Base.metadata.create_all(bind=config.engine)


def get_db():
    db = config.SessionLocal()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()

'''
@app.on_event("startup")
async def populate_database():
    with config.SessionLocal() as db:
        df = pd.read_csv('crop_recommendation.csv')
        for sample in df.iterrows():
            recommendation = models.RecommendationModel(
                    nitrogen=sample[1]['N'],
                    phosphorous=sample[1]['P'],
                    potassium=sample[1]['K'],
                    temperature=sample[1]['temperature'],
                    humidity=sample[1]['humidity'],
                    ph=sample[1]['ph'],
                    rainfall=sample[1]['rainfall'],
                    label=sample[1]['label'])
            print(type(db))
            print('add' in dir(db))
            print('\n\n')
            db.add(recommendation)
            db.commit()
'''


@app.get('/', response_model=List[schemas.RecommendationBase])
async def get_recommendations(db: Session = Depends(get_db)):
    recommendations = db_operations.get_recommendations(db)
    return recommendations


@app.get('/{recommendation_id}', response_model=schemas.RecommendationBase)
async def get_recommendation(recommendation_id: int, db: Session = Depends(get_db)):
    recommendation = db_operations.get_recommendation(recommendation_id, db)
    return recommendation


@app.post('/', response_model=schemas.RecommendationBase)
async def create_recommendation(recommendation: schemas.RecommendationBase, db: Session = Depends(get_db)):
    record = db_operations.create_recommendation(recommendation, db)
    return record


@app.put('/', response_model=schemas.RecommendationBase)
async def update_recommendation(recommendation_id: int, recommendation: schemas.RecommendationBase, db: Session = Depends(get_db)):
    record = db_operations.modify_recommendation(recommendation, db)
    return record


@app.delete('/', response_model=List[schemas.RecommendationBase])
async def delete_recommendation(recommendation_id: int, db: Session = Depends(get_db)):
    recommendations = db_operations.delete_recommendation(recommendation_id, db)
    return recommendations
