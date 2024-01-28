import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class Category(Base):
    __tablename__ = "category"
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True)
    name: Mapped[str] = mapped_column(sa.String(100), nullable=True)
