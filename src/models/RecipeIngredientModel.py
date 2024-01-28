import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database import Base

from .IngredientModel import Ingredient
from .RecipeModel import Recipe


class RecipeIngredient(Base):
    __tablename__ = "recipe_ingredient"
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True, autoincrement=True)
    recipe_id: Mapped[int] = mapped_column(sa.Integer, sa.ForeignKey(Recipe.id))
    ingredient_id: Mapped[int] = mapped_column(sa.Integer, sa.ForeignKey(Ingredient.id))
    quantity: Mapped[float] = mapped_column(sa.Float, nullable=True)
    unit: Mapped[str] = mapped_column(sa.String(50), nullable=True)
    alt_quantity: Mapped[float] = mapped_column(sa.Float, nullable=True)
    alt_unit: Mapped[float] = mapped_column(sa.String(50), nullable=True)
    comment: Mapped[str] = mapped_column(sa.String(500), nullable=True)

    ingredient = relationship("Ingredient")
    recipe = relationship("Recipe")

    def __str__(self) -> str:
        return f"RecipeIngredient, recipe:{self.recipe_id}, ingredient:{self.ingredient_id}"

    def __repr__(self) -> str:
        return f"RecipeIngredient, recipe:{self.recipe_id}, ingredient:{self.ingredient_id}"
