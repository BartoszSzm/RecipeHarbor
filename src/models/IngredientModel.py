import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base


class Ingredient(Base):
    __tablename__ = "ingredient"
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(sa.String(500), nullable=True, unique=True)

    def __str__(self) -> str:
        return f"Ingredient: {self.name[:15]}" if self.name else ""

    def __repr__(self) -> str:
        return f"Recipe:{self.name[:15]}" if self.name else ""
