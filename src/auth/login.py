import flask
from werkzeug.wrappers import Response
import flask_login #type: ignore
from .forms import LoginForm
from src import models


login_manager = flask_login.LoginManager()

login_bp = flask.Blueprint(
    name="login",
    import_name=__name__,
    template_folder="templates"
)

# Need to be fixed

# @login_bp.before_app_request
# def require_login() -> Response | None:
    
#     allowed_paths = [
#         "/login",
#         "/static/css/styles.css",
#         "/static/assets/favicon.ico",
#         "/static/js/scripts.js"
#     ]
    
#     if not flask_login.current_user.is_authenticated:
#         if flask.request.path not in allowed_paths:
#             return flask.redirect(flask.url_for('login.login'))



# @login_bp.route("/login", methods=["GET", "POST"])
# def login() -> Response | str | None:
#     """ View function for users login """
#     form = LoginForm()
    
#     if flask.request.method == "POST":
#         if form.validate_on_submit():
#             user = models.User.query.filter_by(email=form.email.data.lower()).first()
#             if user.verify_password(form.password.data):
#                 print("Password ok, logging...")
#                 flask_login.login_user(user)
#                 _next: str | None = flask.request.args.get('next')
#                 if _next is None or not _next.startswith('/'):
#                     _next = flask.url_for('index.index')
#                 return flask.redirect(_next)
#             else:
#                 flask.flash("Invalid email or password")
#         else:
#             flask.flash("Invalid data passed in form")
#         return flask.render_template('login.html', form=form)
                
#     if flask.request.method == "GET":
#         return flask.render_template('login.html', form=form)


@login_bp.route("/logout")
def logout() -> Response:
    flask_login.logout_user()
    flask.flash("Logged out")
    return flask.redirect(flask.url_for('login.login'))

