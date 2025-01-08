from flask import Flask, request, render_template
import datetime

from flask_user import current_user, UserManager
from flask_babelex import Babel
from flask_login import LoginManager

from database import db, User
from views.login import login
from views.item import item
from views.cart import cart
from views.location import location

app = Flask(__name__)


# Class-based application configuration
class ConfigClass(object):
    """ Flask application config """

    # Flask settings
    SECRET_KEY = "SECRET_KEY" # Update key

    # Flask-SQLAlchemy settings

    # NOTE: database no longer hosted on elephantsql.com, use localhost instead
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:password@localhost:5432/smartkart" # Enter db URI here
    SQLALCHEMY_TRACK_MODIFICATIONS = False    # Avoids SQLAlchemy warning

    # Flask-Mail SMTP server settings
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
    MAIL_USERNAME = 'email@example.com'
    MAIL_PASSWORD = 'password'
    MAIL_DEFAULT_SENDER = '"MyApp" <noreply@example.com>'

    # Flask-User settings
    USER_APP_NAME = "SmartKart"      # Shown in and email templates and page footers
    USER_ENABLE_EMAIL = True        # Enable email authentication
    USER_ENABLE_USERNAME = False    # Disable username authentication
    USER_EMAIL_SENDER_NAME = USER_APP_NAME
    USER_EMAIL_SENDER_EMAIL = "noreply@example.com"


# Create Flask app load app.config
app = Flask(__name__)
app.config.from_object(__name__+'.ConfigClass')

# Add app blueprints
app.register_blueprint(login)
app.register_blueprint(item)
app.register_blueprint(cart)
app.register_blueprint(location)

# Initialize Flask-BabelEx
babel = Babel(app)

# Initialize Flask-SQLAlchemy
db.init_app(app)

# Initialize flask_login
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

# Setup Flask-User and specify the User data-model
user_manager = UserManager(app, db, User)

# Create all database tables
with app.app_context():
    db.create_all()

# Add routing to home page with redirect
@app.route("/")
def mainPage():
    return render_template("index.html")

# Start development web server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
