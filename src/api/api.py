import flask_restful  #type: ignore

from .recipe import RecipiesList, RecipeSingle
from .ingredient import (
    RecipeIngredientsList, 
    RecipeIngredientSingle, 
    )
from .category import CategoriesList

api_obj: flask_restful.Api = flask_restful.Api()

# Recipies
api_obj.add_resource(RecipiesList, "/recipies")
api_obj.add_resource(RecipeSingle, "/recipe/<recipe_id>")


# Ingredients
api_obj.add_resource(RecipeIngredientsList, "/ingredients/<int:recipe_id>")
api_obj.add_resource(RecipeIngredientSingle, "/ingredient/<int:recipe_ingredient_id>")


# Categories
api_obj.add_resource(CategoriesList, "/categories/<category_id>")
