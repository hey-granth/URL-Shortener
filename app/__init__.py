from flask import Flask
from hashids import Hashids
from dotenv import load_dotenv
import os
from app.config import Config

load_dotenv()
hashids = Hashids(min_length=5, salt=os.environ.get("HASHID_SALT"))

from app.routes import main


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    # This line tells Flask to load configuration variables from the Config class, which is defined in app/config.py. This allows the application to use these settings throughout its runtime.

    app.register_blueprint(main)
    # This line registers the main blueprint with the Flask application instance.

    return app
