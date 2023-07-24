# backend/routes.py

from wtforms import ValidationError
from flask import Flask, request, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField
from sqlalchemy import text
from markupsafe import escape


app = Flask(__name__)


def validate_username(form, field):
    if '<' in field.data:
        raise ValidationError('No < allowed in username')


class SignUpForm(FlaskForm):
    username = StringField('Username', validators=[validate_username])


@app.route('/users/<int:user_id>', methods=['POST'])

def set_user_roles(user_id):
    user = User.query.get(user_id)
    user.roles = request.json['roles']
    db.session.commit()

    return {'message': 'Roles updated'}


@app.route('/analytics')
@rbac.allow('admin')

def analytics():
    # return analytics data


@app.after_request

def add_csp_header(response):
    response.headers['Content-Security-Policy'] = "default-src 'self'"
    return response


@app.route('/submit', methods=['POST'])
@csrf.exempt

def submit():
    # handle form submit


@app.route('/get_user/<int:user_id>', methods=['GET'])

def get_user(user_id):
    user = User.query.get(user_id)
    if user:
        return jsonify(user.to_dict())
    else:
        return jsonify({'error': 'User not found'})


@app.route('/get_posts', methods=['GET'])

def get_posts():
    posts = Post.query.all()
    return jsonify({'posts': [p.to_dict() for p in posts]})


@app.route('/get_post/<int:post_id>', methods=['GET'])

def get_post(post_id):
    post = Post.query.get(post_id)
    if post:
        return jsonify(post.to_dict())
    else:
        return jsonify({'error': 'Post not found'})