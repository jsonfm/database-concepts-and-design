import datetime

# typing
from typing import Annotated

# SQLAlchemy
from sqlalchemy import func
from sqlalchemy.orm import mapped_column

# Int
intpk = Annotated[int, mapped_column(primary_key=True)]

# Timestamps
timestamp = Annotated[
    datetime.datetime,
    mapped_column(nullable=False, server_default=func.CURRENT_TIMESTAMP()),
]


timestamp_update = Annotated[
    datetime.datetime,
    mapped_column(
        nullable=False,
        server_default=func.CURRENT_TIMESTAMP(),
        onupdate=func.CURRENT_TIMESTAMP(),
    ),
]
