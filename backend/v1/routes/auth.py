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

        email =data.get('email')
        user = User.query.filter_by(email=email).first()
        if not user:
            return jsonify({'error': f'Account {email} does not exist!'}), 404
        
        if not user.check_password_hash(data.get('password')):        
            return jsonify({'error': 'Incorrect password'}), 400

        # generate jwt token
        token = create_access_token(user.id)

        return jsonify({
            'message': 'login successful',
            'token': token
        })

    except Exception as e:
        print(e)
        return jsonify({'error': 'An unexpected error occurred'}), 500
