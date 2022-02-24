from datetime import datetime
from enum import IntEnum
from typing import Optional

from pydantic import BaseModel, Field, Json, validator


class Gender(IntEnum):
    MALE = 0
    FEMALE = 1


class Device(IntEnum):
    WEB = 0
    MOBILE = 1


class ProfileBase(BaseModel):
    name: Optional[str] = None
    sex: Optional[Gender] = None
    number_of_purchases: Optional[int] = Field(default=0, ge=0)
    avg_price_of_cart: Optional[int] = Field(default=0, ge=0)
    days_since_last_purchase: Optional[int] = Field(default=0, ge=0)
    last_purchase_date: Optional[datetime] = None
    average_days_beetween_purchases: Optional[int] = Field(default=0, ge=0)
    average_number_of_purchases: Optional[int] = Field(default=0, ge=0)
    device_list: Optional[Device] = None
    locations_list: Optional[str] = None
    last_seen_location: Optional[Json] = None

    @validator("last_seen_location")
    def lot_lan_required(cls, v):
        if v is None:
            return v
        if "lon" not in v or "lat" not in v:
            raise ValueError("must contain keys: lon and lat")
        return v


class Profile(ProfileBase):
    id: int

    class Config:
        orm_mode = True


class ProfileCreate(ProfileBase):
    name: str


class ProfileUpdate(ProfileBase):
    pass


class ProfileResponse(BaseModel):
    id: int
