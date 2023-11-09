from typing import List

# sqlaclhemy
from sqlalchemy import String
# orm
from sqlalchemy.orm import Mapped, mapped_column, relationship

# models
from app.common.models.base import CustomBaseModel


class User(CustomBaseModel):
    __tablename__ = "users"
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False, index=True)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    educations: Mapped[List["Education"]] = relationship()

    @classmethod
    def get_by_email(cls, email: str):
        with cls.db.session() as session:
            item = session.query(cls).filter_by(email=email).first()
        return item