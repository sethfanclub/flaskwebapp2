from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_debugtoolbar import DebugToolbarExtension
from flask_mail import Mail
from flask_socketio import SocketIO

db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()
toolbar = DebugToolbarExtension()
mail = Mail()
socketio = SocketIO(cors_allowed_origins='*', manage_session=False, logger=True)