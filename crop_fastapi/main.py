from typing import List
from fastapi import FastAPI, Depends, Body, Query, HTTPException
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


def model_to_base(record: models.RecommendationModel):
    recommendation = schemas.RecommendationBase(**record.__dict__)
    return recommendation


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
    records = db_operations.get_recommendations(db)
    if records is None:
        raise HTTPException(status_code=404, detail="No recommendation found")
    recommendations = [model_to_base(rec) for rec in records]
    return recommendations


@app.get('/{recommendation_id}', response_model=schemas.RecommendationBase)
async def get_recommendation(recommendation_id: int, db: Session = Depends(get_db)):
    recommendation = db_operations.get_recommendation(recommendation_id, db)
    if recommendation is None:
        raise HTTPException(status_code=404, detail="recommendation not found")
    recommendation = model_to_base(recommendation)
    return recommendation


@app.post('/', response_model=schemas.RecommendationBase)
async def create_recommendation(recommendation: schemas.RecommendationBase = Body(), db: Session = Depends(get_db)):
    record = db_operations.create_recommendation(recommendation, db)
    if record == 201:
        return recommendation
    raise record


@app.post('/test', response_model=str)
async def test_post_request(msg: str = Body(), name: str = Body()):
    print(f'the message is {msg} and the name is {name}')
    return 'khra'


@app.put('/{recommendation_id}', response_model=schemas.RecommendationBase)
async def update_recommendation(recommendation_id: int, recommendation: schemas.RecommendationBase = Body(), db: Session = Depends(get_db)):
    record = db_operations.modify_recommendation(recommendation, db)

    if record is None:
        raise HTTPException(status_code=404, detail="the recommendation you want to update does not exist")

    if record == 204:
        return recommendation

    raise record


@app.delete('/{recommendation_id}', response_model=List[schemas.RecommendationBase])
async def delete_recommendation(recommendation_id: int, db: Session = Depends(get_db)):
    records = db_operations.delete_recommendation(recommendation_id, db)
    if records is None:
        raise HTTPException(status_code=404, detail="the record you want to delete does not exist")
    recommendations = [model_to_base(rec) for rec in records]
    return recommendations
