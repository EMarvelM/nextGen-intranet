from flask import request, jsonify
from flask_jwt_extended import create_access_token
from ..models.user import db, User
from ..models.course import Course
from ..views.user import generate_username
from . import user

@user.route("/", strict_slashes=False, methods=["POST"])
def register():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Missing registration data"}), 400
        
        user = User()

        err = user.validate_fields(['firstname', 'lastname', 'email', 'password', 'course'], data=data)
        if err:
            return jsonify(err), 400

        existing_user = User.query.filter_by(email=data.get('email')).first()
        if existing_user:
            return jsonify({'error': f'Email {existing_user.email} already exists'}), 401

        if 'username' not in data:
            while True:
                username = generate_username(firstname=data['firstname'])
                userUsername = User.query.filter_by(username=username).first()
                if not userUsername:
                    data['username'] = username
                    break
        else:
            userUsername = User.query.filter_by(username=username)
            if userUsername:
                return jsonify({'error': f'Username {username} already exists'}), 401


        for key, value in data.items():
            # must be a strong password before hashing and storing
            if key == 'password':
                pass_err =  user.validate_password(value)
                if pass_err:
                    return jsonify(pass_err), 400
                value = user.hash_password(key)

            # check for course availability before setting
            elif key == 'course':
                course = Course.query.filter_by(name=value).first()
                if not course:
                    return jsonify({'error': f'Course {value} does not exits - Report to an admin.'})
                value = course.id

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
