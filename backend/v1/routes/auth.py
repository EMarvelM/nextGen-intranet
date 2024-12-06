from flask import jsonify, request
from flask_jwt_extended import create_access_token
from . import auth
from ..models.user import User

@auth.route("/login", strict_slashes=False, methods=['POST'])
def login():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Missing registration data'}), 400

        err = User.validate_fields(['email', 'password'], data=data)
        if err:
            return jsonify(err), 400

        user = User.query.filter_by(email=data.get('email')).first()
        if not user:
            return jsonify({'error': 'Account does not exist!'})
        

        token = create_access_token(user.id)

        return jsonify({
            'message': 'login successful',
            'token': token
        })
        
    except Exception as e:
        print(e)
        return jsonify({'error': 'An unexpected error occurred'}), 500
