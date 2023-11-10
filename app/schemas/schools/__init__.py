from enum import Enum

from pydantic import Country, Field

#
from app.schemas.base import CustomBaseSchema


class SchoolType(str, Enum):
    UNIVERSITY = "UNIVERSITY"
    INSTITUTE = "INSTITUTE"
    PLATFORM = "PLATFORM"
    OTHER = "OTHER"

class School(CustomBaseSchema):
    name: str = Field(...)
    country: Country
    type: SchoolType