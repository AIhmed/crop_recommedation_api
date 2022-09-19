from sqlalchemy import Column, String, Float, Integer
from .config import Base


class RecommendationModel(Base):
    __tablename__ = "recommendation"

    id = Column(Integer, primary_key=True, index=True)
    nitrogen = Column(Integer)
    phosphorous = Column(Integer)
    potassium = Column(Integer)
    temperature = Column(Float)
    humidity = Column(Float)
    ph = Column(Float)
    rainfall = Column(Float)
    label = Column(String(12))
