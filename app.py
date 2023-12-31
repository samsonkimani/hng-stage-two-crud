import uuid
from flask import Flask, render_template, request, jsonify
from models.user import User
from db.db import DB
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

load_dotenv()

db = DB()

db.reload()

app = Flask(__name__)
# setting up the database to support migrations
user = os.getenv('USER')
password = os.getenv('PASSWORD')
host = os.getenv('HOST')
db_name = os.getenv('DATABASE')

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user}:{password}@{host}/{db_name}'
dbase = SQLAlchemy(app)
migrate = Migrate(app, dbase)


def generate_uuid():
    return uuid.uuid4().hex

@app.route('/')
def index():
    return jsonify({'message': 'follow the documentation to use the API'})

# def user_exists(email):
#     user = db.query(User).filter_by(email=email).first()
#     if user:
#         return True
#     return False

@app.route('/api', methods=['POST'])
def add_user():
    id = generate_uuid()
    user_name = request.form.get('user_name')
    email = request.form.get('user_email')

    new_user = User(id=id, user_name=user_name, email=email)

    db.add(new_user)
    db.save()
    return jsonify(new_user.id), 200


@app.route('/api/<string:user_id>', methods=['GET'])
def get_user(user_id):
    id = user_id
    if id:
        user = db.query(User).filter_by(id=id).first()
        user_data = {
            'id': user.id,
            'user_name': user.user_name,
            'email': user.email
        }
        return jsonify(user_data), 200
    return jsonify({'message': 'user not found'}), 404

@app.route('/api/<string:user_id>', methods=['PUT'])
def update_user(user_id):
    id = user_id
    if id:
        user_name = request.form.get('user_name')
        email = request.form.get('user_email')

        user = db.query(User).filter_by(id=id).first()
        if user_name:
            user.user_name = user_name
        if email:
            user.email = email
        db.save()

        user_data = {
            'id': user.id,
            'user_name': user.user_name,
            'email': user.email
        }
        return jsonify(user_data), 200
    return jsonify({'message': 'user not found'}), 404

@app.route('/api/<string:user_id>', methods=['DELETE'])
def delete_user(user_id):
    id = user_id
    if id:
        user = db.query(User).filter_by(id=id).first()
        if user:
            db.delete(user)
            db.save()
            return jsonify({'message': 'user deleted'}), 200
        else:
            return jsonify({'message': 'user not found'}), 404

    return jsonify({'message': 'id is needed'}), 404

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
