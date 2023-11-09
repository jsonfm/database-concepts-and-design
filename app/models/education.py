from sqlalchemy import ForeignKey, Integer, String
# orm
from sqlalchemy.orm import Mapped, mapped_column, relationship

# models
from app.common.models.base import CustomBaseModel
#schemas
from app.schemas.education import Education as EducationSchema


class Education(CustomBaseModel):
    __tablename__ = "educations"
    schema = EducationSchema
    
    #
    title: Mapped[str] = mapped_column(String(255), unique=True, nullable=False, index=True)
    start_year: Mapped[int] = mapped_column(Integer, nullable=False)
    end_year: Mapped[int] = mapped_column(Integer, nullable=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="educations")

    @classmethod
    def get_by_user_id(cls, user_id: int, limit: int = 20, offset: int = 0):
        with cls.db.session() as session:
            item = session.query(cls).filter_by(user_id=user_id).limit(limit).offset(offset).all()
            item = cls._validate(item)
        return item