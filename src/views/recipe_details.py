from flask import Blueprint, render_template


recipe_details_bp: Blueprint = Blueprint(
    name="recipe_details",
    import_name=__name__,
    template_folder="templates"
)

@recipe_details_bp.route("/recipedetails/<int:recipe_id>")
def recipe_details(recipe_id: int) -> str:
    return render_template(
        'recipe_details.html',
    )