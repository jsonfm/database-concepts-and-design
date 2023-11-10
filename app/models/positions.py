from sqlalchemy import ForeignKey, Integer, String
# orm
from sqlalchemy.orm import Mapped, mapped_column, relationship

# models
from app.common.models.base import CustomBaseModel
# schemas
from app.schemas.positions import ProfessionalPosition


class ProfessionalPosition(CustomBaseModel):
    __tablename__ = "professional_positions"
    schema = ProfessionalPosition
    validate = True

    #
    title: Mapped[str] = mapped_column(String(255))
    start_year: Mapped[int] = mapped_column(Integer, nullable=False)
    end_year: Mapped[int] = mapped_column(Integer, nullable=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="professional_positions")