import flask


def create_app() -> flask.Flask:
    """Return configured app object"""

    # Initialize app and configure
    from src.config import Config

    app: flask.Flask = flask.Flask(__name__)
    config = Config()
    app.config.from_object(config)

    from src.views import index, recipe_details

    # Register blueprints
    app.register_blueprint(index.index_bp)
    app.register_blueprint(recipe_details.recipe_details_bp)

    # API
    from src.api.api import api_obj

    api_obj.init_app(app)

    # DB
    from src.database import init_db

    init_db(app)

    return app
