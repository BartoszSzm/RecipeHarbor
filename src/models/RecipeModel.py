from datetime import datetime

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from src.database import Base

from .CategoryModel import Category
from .UserModel import User


class Recipe(Base):
    __tablename__ = "recipe"
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(sa.Text(), nullable=True)
    preparation: Mapped[str] = mapped_column(sa.Text(), nullable=True)
    date_added: Mapped[datetime] = mapped_column(
        sa.DateTime, default=datetime.now(), nullable=True
    )
    meal_type: Mapped[str] = mapped_column(sa.String(100), nullable=True)
    user_id: Mapped[int] = mapped_column(sa.ForeignKey(User.id))
    category_id: Mapped[int] = mapped_column(sa.ForeignKey(Category.id), nullable=True)

    def __str__(self) -> str:
        return f"Recipe:{self.name[:10]}..." if self.name else ""

    def __repr__(self) -> str:
        return f"Recipe:{self.name[:10]}..." if self.name else ""
