from datetime import datetime
from sqlalchemy import Integer, String, func, JSON
from sqlalchemy.orm import mapped_column, Mapped, DeclarativeBase
from sqlalchemy.sql.sqltypes import DateTime


class Base(DeclarativeBase):
    created_at: Mapped[datetime] = mapped_column(DateTime, default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=func.now(), onupdate=func.now()
    )


class Contact(Base):
    __tablename__ = "contacts"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    email: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    phone_number: Mapped[str] = mapped_column(String(100), nullable=False)
    birthday: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    additional_data: Mapped[str] = mapped_column(String(150), nullable=False)
    tags: Mapped[dict] = mapped_column(JSON, nullable=True)