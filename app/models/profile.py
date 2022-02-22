from sqlalchemy import Column, DateTime, Integer, JSON, String

from app.models import Base


class Profile(Base):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    sex = Column(Integer)
    number_of_purchases = Column(Integer)
    avg_price_of_cart = Column(Integer)
    days_since_last_purchase = Column(Integer)
    last_purchase_date = Column(DateTime)
    average_days_beetween_purchases = Column(Integer)
    average_number_of_purchases = Column(Integer)
    device_list = Column(Integer)
    locations_list = Column(String)
    last_seen_location = Column(JSON)
