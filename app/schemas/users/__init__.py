from datetime import datetime
from enum import Enum

#
from pydantic import Field

#
from app.schemas.base import CustomBaseSchema


class User(CustomBaseSchema):
    email: str
    password: str = Field(exclude=True)


class ProfileSexEnum(str, Enum):
    F: "F"
    M: "M"
    

class Profile(CustomBaseSchema):
    user_id: int = Field(ge=1, examples=[1])
    sex: ProfileSexEnum
    first_name: str = Field(...)
    last_name: str = Field(...)
    birthday: datetime
    current_city: str = Field(...)
    hometown: str = Field(...)
