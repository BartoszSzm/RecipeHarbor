from typing import Any

from flask_restful import Resource, fields, marshal_with  # type: ignore
from sqlalchemy import select

from src.database import db_session
from src.models.CategoryModel import Category


class CategoriesList(Resource):
    """CRUD for categories"""

    categories_fields = {"id": fields.Integer, "name": fields.String}

    @marshal_with(categories_fields)
    def get(self, category_id: int) -> Any | None:
        return db_session.execute(
            select(Category).where(Category.id == category_id)
        ).scalar()
