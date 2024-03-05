from flask import Flask
from dynaconf import FlaskDynaconf

app = Flask(__name__)

FlaskDynaconf(app, settings_files=["settings.toml"])


@app.route("/a_view")
def a_view():
    app.config.NAME == "BRUNO"
    app.config['DEBUG'] is True
    app.config.SQLALCHEMY_DB_URI == "sqlite://data.db"