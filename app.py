import uuid
from flask import Flask, render_template, request, jsonify
from models.user import User
from db.db import DB

db = DB()

db.reload()

app = Flask(__name__)

def generate_uuid():
    return uuid.uuid4().hex

@app.route('/')
def index():
    return jsponify({'message': 'follow the documentation to use the API'})

@app.route('/api', methods=['POST'])
def add_user():
    id = generate_uuid()
    user = request.args.get('user_name')
    email = request.args.get('user_email')
    if user and email:
        new_user = User(id=id, name=user, email=email)

        db.add(new_user)
        db.save()
    return jsonify(new_user.id), 200

if __name__ == '__main__':
    app.run(host='localhost', port=5000)
