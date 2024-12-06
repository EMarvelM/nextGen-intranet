from flask import Flask
from flask_jwt_extended import JWTManager
from .models import db
from .models.user import User
from .config import config

# routes
from .routes.auth import auth
jwt = JWTManager()

app = Flask(__name__)
app.config.from_object(config)

app.register_blueprint(auth)


def create_app():
    jwt.init_app(app)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app
