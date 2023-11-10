# models
from app.common.models.base import CustomBaseModel
# schemas
from app.schemas.schools import School as SchoolSchema


class Schools(CustomBaseModel):
    __tablename__ = "professional_positions"
    schema = SchoolSchema
    validate = True