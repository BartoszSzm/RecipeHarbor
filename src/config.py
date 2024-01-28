import os
from dotenv import load_dotenv



class Config:
    def __init__(self, config_path: str | os.PathLike ="") -> None:
        default_config_path = os.path.join(os.path.dirname(__file__), ".env")
        load_dotenv(default_config_path or config_path)
        self.load_config()
        
    def load_config(self) -> None:
        self.SQLALCHEMY_DATABASE_URI = os.environ['DB_CONN_STRING']
        self.SECRET_KEY = os.environ['SECRET_KEY']
        self.SQLALCHEMY_TRACK_MODIFICATIONS = False