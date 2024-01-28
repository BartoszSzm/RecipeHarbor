from flask import Blueprint, render_template


index_bp: Blueprint = Blueprint(
    name="index",
    import_name=__name__,
    template_folder="templates"
)

@index_bp.route("/")
def index() -> str:
    return render_template(
        'index.html'
    )