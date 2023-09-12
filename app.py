import uuid
from flask import Flask, render_template, request, jsonify
from models.user import User
from db.db import DB
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv

load_dotenv('.env')

db = DB()

db.reload()

app = Flask(__name__)
# setting up the database to support migrations
user = getenv('USER')
password = getenv('PASSWORD')
host = getenv('HOST')
db_name = getenv('DATABASE')
port = getenv('PORT')

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
dbase = SQLAlchemy(app)
migrate = Migrate(app, dbase)


def generate_uuid():
    return uuid.uuid4().hex

@app.route('/')
def index():
    return jsponify({'message': 'follow the documentation to use the API'})

def user_exists(email):
    user = db.query(User).filter_by(email=email).first()
    if user:
        return True
    return False

@app.route('/api', methods=['POST'])
def add_user():
    id = generate_uuid()
    f_name = request.args.get('f_name')
    l_name = request.args.get('l_name')
    email = request.args.get('user_email')
    user = user_exists(email)
    if user is False:
        new_user = User(id=id, f_name=f_name, l_name=l_name, email=email)

        db.add(new_user)
        db.save()
        return jsonify(new_user.id), 200
    else:
        return jsonify({'message': 'user already exists'}), 400

@app.route('/api/<string:user_id>', methods=['GET'])
def get_user(user_id):
    id = user_id
    if id:
        user = db.query(User).filter_by(id=id).first()
        user_data = {
            'id': user.id,
            'f_name': user.f_name,
            'l_name': user.l_name,
            'email': user.email
        }
        return jsonify(user_data), 200
    return jsonify({'message': 'user not found'}), 404

@app.route('/api/<string:user_id>', methods=['PUT'])
def update_user(user_id):
    id = user_id
    if id:
        f_name = request.form.get('f_name')
        l_name = request.form.get('l_name')
        email = request.form.get('user_email')

        user = db.query(User).filter_by(id=id).first()
        if f_name:
            user.f_name = f_name
        if l_name:
            user.l_name = l_name
        if email:
            user.email = email
        db.save()

        user_data = {
            'id': user.id,
            'f_name': user.f_name,
            'l_name': user.l_name,
            'email': user.email
        }
        return jsonify(user_data), 200
    return jsonify({'message': 'user not found'}), 404

@app.route('/api/<string:user_id>', methods=['DELETE'])
def delete_user(user_id):
    id = user_id
    if id:
        user = db.query(User).filter_by(id=id).first()
        db.delete(user)
        db.save()
        return jsonify({'message': 'user deleted'}), 200
    return jsonify({'message': 'user not found'}), 404

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
