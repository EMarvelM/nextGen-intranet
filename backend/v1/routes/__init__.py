from flask import Blueprint

auth = Blueprint("auth", __name__, url_prefix='/auth')
user = Blueprint("user", __name__, url_prefix='/user')
course = Blueprint("course", __name__, url_prefix='/course')