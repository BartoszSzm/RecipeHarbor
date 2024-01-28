from typing import Any, NoReturn, Sequence

from flask_restful import fields  # type: ignore
from flask_restful import Resource, abort, marshal_with, reqparse
from sqlalchemy import select
from sqlalchemy.exc import MultipleResultsFound, NoResultFound

from src.database import db_session
from src.models.CategoryModel import Category
from src.models.RecipeIngredientModel import RecipeIngredient
from src.models.RecipeModel import Recipe


class RecipiesList(Resource):
    """CRUD for recipe"""

    recipe_fields = {
        "Recipe.id": fields.Integer,
        "Recipe.name": fields.String,
        "Recipe.date_added": fields.DateTime,
        "Recipe.meal_type": fields.String,
        "Recipe.user_id": fields.Integer,
        "Category.name": fields.String,
    }

    parser = reqparse.RequestParser()
    parser.add_argument("name", type=str)
    parser.add_argument("meal_type", type=str)
    parser.add_argument("user_id", type=int, default=1)
    parser.add_argument("category_id", type=int, default=0)

    @marshal_with(recipe_fields)
    def get(self) -> Sequence[Any]:
        return db_session.execute(
            select(Recipe, Category).join(Category, Recipe.category_id == Category.id)
        ).all()

    def post(self) -> None:
        args = self.parser.parse_args(strict=True)
        try:
            recipe = Recipe(
                name=args["name"],
                meal_type=args["meal_type"],
                category_id=args["category_id"],
                user_id=args["user_id"],
            )
            db_session.add(recipe)
            db_session.commit()
        except Exception as exc:
            db_session.rollback()
            print(exc)
            raise


class RecipeSingle(Resource):
    """CRUD for single recipe data"""

    parser = reqparse.RequestParser()
    parser.add_argument("name", type=str)
    parser.add_argument("preparation", type=str)
    parser.add_argument("meal_type", type=str)

    single_recipe_fields = {
        "id": fields.Integer,
        "name": fields.String,
        "preparation": fields.String,
        "date_added": fields.DateTime,
        "meal_type": fields.String,
        "user_id": fields.Integer,
    }

    @marshal_with(single_recipe_fields)
    def get(self, recipe_id: int) -> Any | None:
        return db_session.scalar(select(Recipe).where(Recipe.id == recipe_id))

    def put(self, recipe_id: int) -> dict[str, str] | NoReturn:
        args = self.parser.parse_args(strict=True)
        recipe = db_session.query(Recipe).filter(Recipe.id == recipe_id).one()
        try:
            [setattr(recipe, arg, args[arg]) for arg in args if args.get(arg)]  # type: ignore
            db_session.commit()
            return {"message": "Success"}
        except Exception as exc:
            db_session.rollback()
            print(exc)
            return abort(500)

    def delete(self, recipe_id: int) -> dict[str, str]:
        try:
            db_session.delete(db_session.query(Recipe).filter_by(id=recipe_id).one())
            db_session.query(RecipeIngredient).filter_by(recipe_id=recipe_id).delete()
            db_session.commit()
            return {"message": "Success"}
        except NoResultFound:
            return {"message": f"Record {recipe_id} not found"}
        except MultipleResultsFound:
            return {"message": "Multiple results found, database error"}
        except:
            return {"message": "Unknown database error"}
