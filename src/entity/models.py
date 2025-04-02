from datetime import datetime

from sqlalchemy import String, DateTime, func
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column

from src.conf import constants


class Base(DeclarativeBase):
    pass


class Contact_Book(Base):
    __tablename__ = "Contact_Book"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(constants.USER_NAME_MAX_LENGTH), nullable=False)
    surname: Mapped[str] = mapped_column(String(constants.USER_SURNAME_MAX_LENGTH), nullable=False)
    email: Mapped[str] = mapped_column(String(constants.USER_EMAIL_MAX_LENGTH), nullable=False)
    phone: Mapped[str] = mapped_column(String(constants.PHONE_NUMBER_MAX_LENGTH), nullable=False)
    date_of_birth: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=func.now(), onupdate=func.now()
    )