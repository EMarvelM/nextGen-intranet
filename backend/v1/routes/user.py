from flask import request, jsonify
from flask_jwt_extended import create_access_token
from ..models import db
from ..models.user import User
from . import user

@user.route("/", strict_slashes=False, methods=["POST"])
def register():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "missing data"})
        
        user = User()
        db.session.add(user)
        db.session.commit()

        token = create_access_token(identity=user.id)
        return jsonify({
            "token": token,
            "message": "Account created successfully"
        })

    except:
        return jsonify({"error": "An unexpected error occured"})
