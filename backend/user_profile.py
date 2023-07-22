from flask import request, jsonify
from models import User
from database_config import db

@app.route('/userProfile', methods=['GET'])
def get_user_profile():
    authToken = request.headers.get('authToken')
    user = User.query.filter_by(auth_token=authToken).first()
    if user:
        userProfile = {
            'username': user.username,
            'email': user.email,
            'podcastList': user.podcasts
        }
        return jsonify(userProfile), 200
    else:
        return jsonify({'message': 'User not found'}), 404

@app.route('/userProfile', methods=['PUT'])
def update_user_profile():
    authToken = request.headers.get('authToken')
    user = User.query.filter_by(auth_token=authToken).first()
    if user:
        data = request.get_json()
        user.username = data.get('username', user.username)
        user.email = data.get('email', user.email)
        db.session.commit()
        return jsonify({'message': 'User profile updated successfully'}), 200
    else:
        return jsonify({'message': 'User not found'}), 404