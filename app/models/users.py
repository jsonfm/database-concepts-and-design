from typing import List

# sqlaclhemy
from sqlalchemy import ForeignKey, String
# orm
from sqlalchemy.orm import Mapped, mapped_column, relationship

# models
from app.common.models.base import CustomBaseModel
#schemas
from app.schemas.users import Profile as ProfileSchema
from app.schemas.users import User as UserSchema


class User(CustomBaseModel):
    __tablename__ = "users"
    schema = UserSchema
    validate = True

    #
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False, index=True)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    educations: Mapped[List["Education"]] = relationship()
    professional_positions: Mapped[List["ProfessionalPosition"]] = relationship()
    profile: Mapped["Profile"] = relationship(back_populates="user")

    @classmethod
    def get_by_email(cls, email: str):
        with cls.db.session() as session:
            item = session.query(cls).filter_by(email=email).first()
            item = cls._validate(item)
        return item


class Profile(CustomBaseModel):
    __tablename__ = "profiles"
    schema = ProfileSchema
    validate = True

    #
    first_name: Mapped[str] = mapped_column(String(128))
    last_name: Mapped[str] = mapped_column(String(128))
    sex: Mapped[str] = mapped_column(String(10))
    current_city: Mapped[str] = mapped_column(String(255))
    hometown: Mapped[str] = mapped_column(String(255))

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="profile")