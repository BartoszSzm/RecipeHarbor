import sqlalchemy
from flask import Flask
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from sqlalchemy.orm.scoping import scoped_session

engine = sqlalchemy.create_engine("sqlite:///recipies.db")

db_session = scoped_session(
    sessionmaker(bind=engine, autocommit=False, autoflush=False)
)


class Base(DeclarativeBase):
    pass


def init_db(app: Flask) -> None:
    from .models.CategoryModel import Category
    from .models.IngredientModel import Ingredient
    from .models.RecipeIngredientModel import RecipeIngredient
    from .models.RecipeModel import Recipe
    from .models.UserModel import User

    with app.app_context():
        Base.metadata.create_all(engine)
        db_session.commit()
        all_categories = db_session.query(Category).all()
        if len(all_categories) == 0:
            db_session.add(Category(id=0, name="Other"))
            db_session.commit()
