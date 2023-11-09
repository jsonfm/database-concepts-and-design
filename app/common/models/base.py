# sqlalchemy
from sqlalchemy import Boolean
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy_serializer import SerializerMixin

# crud
from app.common.models.crud import CRUD
# types
from app.common.types.sqlalchemy import intpk, timestamp, timestamp_update
# database
from app.db import Base


class CommonFields(Base, SerializerMixin):
    """Common Fields for an SQLAlchemy Model."""

    __abstract__ = True

    id: Mapped[intpk]
    created_at: Mapped[timestamp]
    updated_at: Mapped[timestamp_update]
    active: Mapped[bool] = mapped_column(Boolean, default=False)
    deleted: Mapped[bool] = mapped_column(Boolean, default=False)


class CustomBaseModel(CommonFields, CRUD):
    """Custom Base SQLAlchemy model, with common crud operations and common fields."""

    __abstract__ = True