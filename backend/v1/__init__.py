from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
# db models
from .models import db, bcrypt
from .models.user import User
from .models.course import Course

from .config import config
# routes
from .routes.auth import auth
from .routes.user import user
from .routes.course import course

jwt = JWTManager()
cors = CORS()

app = Flask(__name__)
app.config.from_object(config)

app.register_blueprint(auth)
app.register_blueprint(user)
app.register_blueprint(course)


def create_app():
    cors.init_app(app, resources={'*': {'origin': '*'}}, supports_credentials=True)
    jwt.init_app(app)
    db.init_app(app)
    bcrypt.init_app(app)

    with app.app_context():
        db.create_all()

    return app
