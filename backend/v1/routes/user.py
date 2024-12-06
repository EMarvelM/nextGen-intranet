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
            return jsonify({"error": "Missing registration data"}), 400
        
        user = User()

        err = user.validate_fields(['firstname', 'lastname', 'email', 'password'], data=data)
        if err:
            return jsonify(err), 400
        
        existing_user = User.query.filter_by(email=data.get('email')).first()
        if existing_user:
            return jsonify({'error': f'Email {existing_user.email} already exists'})

        for key, value in data.items():
            if key == 'password':
                pass_err =  user.validate_password(value)
                if pass_err:
                    return jsonify(pass_err), 400
                value = user.hash_password(key)

            if hasattr(user, key):
                setattr(user, key, value)

        db.session.add(user)
        db.session.commit()

        token = create_access_token(identity=user.id)
        return jsonify({
            "token": token,
            "message": "Account created successfully"
        })

    except Exception as e:
        db.session.rollback()
        print(e)
        return jsonify({"error": "An unexpected error occurred"}), 500
