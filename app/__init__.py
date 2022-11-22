from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
app.app_context().push()
CORS(app, supports_credentials=True)
app.config.from_object('config')
db = SQLAlchemy(app)
ma = Marshmallow(app)

from .models import lobby
from .routes import routes


