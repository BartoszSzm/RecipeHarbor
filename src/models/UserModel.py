import flask_login  # type: ignore
import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column
from werkzeug.security import check_password_hash, generate_password_hash

from src.database import Base, db_session

login_manager = flask_login.LoginManager()


class User(Base, flask_login.UserMixin):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(sa.String(100), unique=True)
    email: Mapped[str] = mapped_column(sa.String(100), unique=True)
    password_hash: Mapped[str] = mapped_column(sa.String(1000))

    def __str__(self) -> str:
        return f"User:{self.username}"

    def __repr__(self) -> str:
        return f"User:{self.username}"

    def verify_password(self, password_plaintext: str) -> bool:
        """Return true if given password is correct, false otherwise"""
        return check_password_hash(self.password_hash, password_plaintext)

    @property
    def password(self) -> None:
        raise AttributeError("Password is not a readable value")

    @password.setter
    def password(self, password_plaintext: str) -> None:
        self.password_hash = generate_password_hash(password_plaintext)


@login_manager.user_loader
def load_user(user_id: int) -> User | None:
    return db_session.get(User, user_id)
