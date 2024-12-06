from flask import jsonify
from . import auth

@auth.route("/", strict_slashes=False)
def login():
    return jsonify({"status": "ok"})
