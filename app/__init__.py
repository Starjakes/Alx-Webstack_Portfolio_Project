from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
login_manager = LoginManager(app)
login_manager.login_view = 'login_page'

# Load environment variables from .env file
load_dotenv()

# Load secret key from environment variable
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")

# Load database URI from environment variable
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')

# Disable modification tracking for better performance
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy extension
db = SQLAlchemy(app)

# Import routes after initializing the database
from app.routes.root import *
from app.routes.admin import *
from app.models.user import *
from app.models.admin import *

