from typing import Any, NoReturn, Sequence

from flask_restful import fields  # type: ignore
from flask_restful import Resource, abort, marshal_with, reqparse
from sqlalchemy import select
from sqlalchemy.exc import MultipleResultsFound, NoResultFound
from werkzeug.exceptions import NotFound

from src.database import db_session as db
from src.models.IngredientModel import Ingredient
from src.models.RecipeIngredientModel import RecipeIngredient


class RecipeIngredientSingle(Resource):
    single_ingredient_fields = {
        "id": fields.Integer,
        "recipe_id": fields.String,
        "ingredient_id": fields.Integer,
        "ingredient.name": fields.String,
        "quantity": fields.Float,
        "unit": fields.String,
    }

    # Arguments available to pass
    parser = reqparse.RequestParser()
    parser.add_argument("name", type=str)
    parser.add_argument("quantity", type=float)
    parser.add_argument("unit", type=str)
    parser.add_argument("alt_quantity", type=float)
    parser.add_argument("alt_unit", type=str)
    parser.add_argument("comment", type=str)

    @marshal_with(single_ingredient_fields)
    def get(self, recipe_ingredient_id: int) -> RecipeIngredient | NotFound:
        """Get specific ingredient for specific recipe"""
        return (
            db.query(RecipeIngredient)
            .filter(RecipeIngredient.id == recipe_ingredient_id)
            .one()
        )

    def put(self, recipe_ingredient_id: int) -> dict[str, str] | NoReturn:
        """Update ingredient for specific recipe"""

        args = self.parser.parse_args(strict=True)

        recipe_ingredient = (
            db.query(RecipeIngredient)
            .filter(RecipeIngredient.id == recipe_ingredient_id)
            .one()
        )

        try:
            for arg in args:
                if args.get(arg):
                    if arg == "name":
                        recipe_ingredient.ingredient.name = args["name"]
                    setattr(recipe_ingredient, arg, args[arg])
            db.commit()
            return {"message": "Success"}
        except Exception as exc:
            db.rollback()
            print(exc)
            return abort(500)

    def delete(self, recipe_ingredient_id: int) -> dict[str, str] | NoReturn:
        """Delete ingredient for specyfic recipe"""
        try:
            db.delete(
                db.query(RecipeIngredient)
                .filter(RecipeIngredient.id == recipe_ingredient_id)
                .one()
            )
            db.commit()
            return {"message": "Success"}
        except NoResultFound:
            return {"message": f"Record {recipe_ingredient_id} not found"}
        except MultipleResultsFound:
            return {"message": "Multiple results found, database error"}
        except:
            return {"message": f"Unknown database error"}


class RecipeIngredientsList(Resource):
    """CRUD for a list of ingredients for specified recipe_id"""

    # Arguments available to pass
    parser = reqparse.RequestParser()
    parser.add_argument("name", type=str)
    parser.add_argument("quantity", type=float)
    parser.add_argument("unit", type=str)
    parser.add_argument("alt_quantity", type=float)
    parser.add_argument("alt_unit", type=str)
    parser.add_argument("comment", type=str)

    recipe_ingredients_fields = {
        "RecipeIngredient.id": fields.Integer,
        "Ingredient.name": fields.String,
        "RecipeIngredient.quantity": fields.Float,
        "RecipeIngredient.unit": fields.String,
        "RecipeIngredient.alt_quantity": fields.Float,
        "RecipeIngredient.alt_unit": fields.String,
        "RecipeIngredient.comment": fields.String,
    }

    @marshal_with(recipe_ingredients_fields)
    def get(self, recipe_id: int) -> Sequence[Any]:
        """Get ingredients list for specific recipe"""
        return db.execute(
            select(RecipeIngredient, Ingredient)
            .join(Ingredient, RecipeIngredient.ingredient_id == Ingredient.id)
            .where(RecipeIngredient.recipe_id == recipe_id)
        ).all()

    def post(self, recipe_id: int) -> dict[str, str] | NoReturn:
        """Add new ingredient to the recipie's ingredients list"""

        args = self.parser.parse_args(strict=True)

        try:
            # First try to add new ingredient to ingredients table
            recipe_name = args.pop("name")
            existing_ingredient = (
                db.query(Ingredient).filter(Ingredient.name == recipe_name).first()
            )
            if not existing_ingredient:
                new_ingredient = Ingredient(name=recipe_name)
                db.add(new_ingredient)
                db.commit()
                args["ingredient_id"] = new_ingredient.id
            else:
                args["ingredient_id"] = existing_ingredient.id

            # Then try to add RecipeIngredient record
            args["recipe_id"] = recipe_id
            db.add(RecipeIngredient(**args))

            db.commit()
            return {"message": "Success"}

        except Exception as exc:
            print(exc)
            db.rollback()
            return abort(500)
