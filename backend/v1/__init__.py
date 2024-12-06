from flask import Flask
from flask_jwt_extended import JWTManager
from .models import db, bcrypt
from .models.user import User
from .config import config

# routes
from .routes.auth import auth
from .routes.user import user
jwt = JWTManager()

app = Flask(__name__)
app.config.from_object(config)

app.register_blueprint(auth)
app.register_blueprint(user)


def create_app():
    jwt.init_app(app)
    db.init_app(app)
    bcrypt.init_app(app)

    with app.app_context():
        db.create_all()

    return app
