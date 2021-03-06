from flask import Flask, g
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager, current_user
from flask.ext.bcrypt import Bcrypt

from config import Configuration

SQLALCHEMY_TRACK_MODIFICATIONS=True

app = Flask(__name__)
#app = Flask(__name__, template_folder="views")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config.from_object(Configuration)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

login_manager = LoginManager(app)
login_manager.login_view = "login"

@app.before_request
def _before_request():
    g.user = current_user

@app._before_request
def _last_page_visited():
    if "current_page" in session:
        session["last_page"] = session["current_page"]
    session["current_page"] = request.path


bcrypt = Bcrypt(app)
