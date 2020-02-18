import logging
import os
import uuid
import json
from flask_cors import CORS

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

from google.cloud.language import enums
from google.cloud.language import types
from google.cloud import language


app = Flask(__name__)
CORS(app)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://database-user:1234@/database_scheme'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Users(db.Model):
    user_id = db.Column(db.String(36), primary_key=True, unique=True, nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    gender = db.Column(db.String(6), nullable=False)

    def __init__(self, first_name, last_name, password, email, gender):
        self.user_id = str(uuid.uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = email
        self.gender = gender


class Sessions(db.Model):
    session_id = db.Column(db.String(36), primary_key=True, unique=True, nullable=False)
    user_id = db.Column(db.String(36), nullable=False)
    expiry_date = db.Column(db.DATETIME, db.ForeignKey('users.user_id'))

    def __init__(self, user_id, expiry_date):
        self.session_id = str(uuid.uuid4())
        self.user_id = user_id
        self.expiry_date = str(expiry_date)


@app.route('/user', methods=['GET'])
def get_user():

    print("LOGIN")

    email = request.args.get('email')
    password = request.args.get('password')

    user = Users.query.filter_by(email=email, password=password).first()

    if user is None:
        response = {
            "user_id": None,
            "first_name": None,
            "last_name": None,
            "password": None,
            "email": None,
            "gender": None
        }
        print(response)

        return json.dumps(response), 404, {'Content-Type': 'application/json'}

    else:
        response = {
            "user_id": user.user_id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "password": user.password,
            "email": user.email,
            "gender": user.gender
        }

        print(response)

        return json.dumps(response), 200, {'Content-Type': 'application/json'}


@app.route('/session', methods=['GET'])
def get_session():

    print("GET COOCKIE")

    session_id = request.args.get("session_id")

    session = Sessions.query.filter_by(session_id=session_id).first()

    if session is None:
        response = {
            "session_id": None,
            "user_id": None,
            "expiry_date": None
        }

        print(response)

        return json.dumps(response), 404, {'Content-Type': 'application/json'}
    else:
        response = {
            "session_id": session.session_id,
            "user_id": session.user_id,
            "expiry_date": str(session.expiry_date)
        }

        print(response)

        return json.dumps(response), 200, {'Content-Type': 'application/json'}


@app.route('/user', methods=['POST'])
def insert_user():

    print("REGISTER")

    content = json.loads(json.loads(request.data)["body"])

    first_name = content["first_name"]
    last_name = content["last_name"]
    password = content["password"]
    email = content["email"]
    gender = content["gender"]

    user = Users(
        first_name=first_name,
        last_name=last_name,
        password=password,
        email=email,
        gender=gender
    )

    db.session.add(user)
    db.session.commit()

    response = {
        "user_id": user.user_id,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "password": user.password,
        "email": user.email,
        "gender": user.gender
    }

    print(response)

    return json.dumps(response), 200, {'Content-Type': 'application/json'}


@app.route('/session', methods=['POST'])
def insert_session():
    content = json.loads(json.loads(request.data)["body"])

    user_id = content["user_id"]
    expiry_date = content["expiry_date"]

    session = Sessions(
        user_id=user_id,
        expiry_date=expiry_date
    )

    db.session.add(session)
    db.session.commit()

    response = {
        "session_id": session.session_id,
        "user_id": session.user_id,
        "expiry_date": str(session.expiry_date)
    }

    return json.dumps(response), 200, {'Content-Type': 'application/json'}


@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request.')
    return """
    An internal error occurred: <pre>{}</pre>
    See logs for full stacktrace.
    """.format(e), 500


@app.route('/analize-text', methods=['POST'])
def analize_text():

    content = json.loads(json.loads(request.data)["body"])["text"]

    print(analyze(content))

    if analyze(content) < 0.3:
        score = -1
    elif analyze(content) > 0.6:
        score = 1
    else:
        score = 0

    response = {
        "score": score
    }

    return json.dumps(response), 200, {'Content-Type': 'application/json'}


def get_result(annotations):
    score = annotations.document_sentiment.score
    return score


def analyze(content):
    client = language.LanguageServiceClient()
    document = types.Document(
        content=content,
        type=enums.Document.Type.PLAIN_TEXT)
    annotations = client.analyze_sentiment(document=document)

    return get_result(annotations)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
