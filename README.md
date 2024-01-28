## Description

RecipeHarbor is a simple app created to organize recipies and to have quick access for it.
For now, app allows you to add new recipe, search for recipe and delete it. To each recipe
you can add description, name and ingredients list + each ingredient can be removed.

When using during cooking, it can be frustrating that your phone screen goint out.
The problem is solved with NoSleep.js - https://github.com/richtr/NoSleep.js

The app is built using Flask with REST api (Flask-RESTfull) + some Bootstrap and Vanilla JS on the frontend. At the moment, because app is meant to be run locally, SQLite3 was used with SQLAlchemy ORM.

![image](https://github.com/BartoszSzm/RecipeHarbor/assets/65613527/da0c7090-b994-4f1b-bf36-777c7be09b59)

![image](https://github.com/BartoszSzm/RecipeHarbor/assets/65613527/7d34e408-ba0d-4415-a703-ab0e90d24688)

![image](https://github.com/BartoszSzm/RecipeHarbor/assets/65613527/a012057a-534d-4602-8df5-d64b496cc286)

![image](https://github.com/BartoszSzm/RecipeHarbor/assets/65613527/07611c5a-4c83-4a15-a363-9bd3c23fc63d)

## Running

App is meant to be run locally for household purposes (for now). You can host it
yourself on machine with limited access - eg RPI, VPS.

1. Create .env file with:
   `DB_CONN_STRING = sqlite:///recipies.db
SECRET_KEY =`

2. `docker compose up --build -d`

## TODOs

- User management
- API security (JWT)
- Ingredient editing
- Shopping list module
