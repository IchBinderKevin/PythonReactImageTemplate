from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from models.domain.base import Base


class Example(Base):
    """
    Example Domain Model for SQLAlchemy and Alembic.
    """
    __tablename__ = "example"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, unique=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
