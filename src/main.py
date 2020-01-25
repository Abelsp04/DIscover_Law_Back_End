"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from models import db, User, Lawyer
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['POST', 'GET'])
def get_user():

#Create a contact and retrieve all contacts!!

    if request.method == 'POST':
        body = request.get_json()

        if body is None:
            raise APIException("You need to specify the request body as a json object", status_code=400)
        if "name" not in body:
            raise APIException('You need to specify the name', status_code=400)
        if 'password' not in body:
            raise APIException('You need to specify the password', status_code=400)
        if 'email' not in body:
            raise APIException('You need to specify the email', status_code=400)
        if 'zipcode' not in body:
            body['zipcode'] = None

        user1 = User(name=body['name'], password = body['password'], email = body['email'], zipcode = body['zipcode'])
        db.session.add(user1)
        db.session.commit()

        return "ok", 200
    
    # GET request
    if request.method == 'GET':
        all_user = User.query.all()
        all_user = list(map(lambda x: x.serialize(), all_user))
        return jsonify(all_user), 200

    return "Invalid Method", 404

@app.route('/user/<int:user_id>', methods=['PUT', 'GET', 'DELETE'])
def get_single_contact(user_id):
    """
    Single contact
    """

    # PUT request
    if request.method == 'PUT':
        body = request.get_json()
        if body is None:
            raise APIException("You need to specify the request body as a json object", status_code=400)

        user1 = User.query.get(user_id)
        if user1 is None:
            raise APIException('User not found', status_code=404)

        if "name" in body:
            user1.name = body["name"]
        if "password" in body:
            user1.password = body["password"]
        if "email" in body:
            user1.email = body["email"]
        if "zipcode" in body:
            user1.zipcode = body["zipcode"]
        db.session.commit()

        return jsonify(user1.serialize()), 200

    # GET request
    if request.method == 'GET':
        user1 = User.query.get(user_id)
        if user1 is None:
            raise APIException('User not found', status_code=404)
        return jsonify(user1.serialize()), 200

    # DELETE request
    if request.method == 'DELETE':
        user1 = User.query.get(user_id)
        if user1 is None:
            raise APIException('User not found', status_code=404)
        db.session.delete(user1)
        db.session.commit()
        return "ok", 200

    return "Invalid Method", 404


# tables for lawyer


@app.route('/lawyer', methods=['POST', 'GET'])
def get_lawyer():

#Create a contact and retrieve all contacts!!

    if request.method == 'POST':
        body = request.get_json()

        if body is None:
            raise APIException("You need to specify the request body as a json object", status_code=400)
        if "name" not in body:
            raise APIException('You need to specify the name', status_code=400)
        if 'password' not in body:
            raise APIException('You need to specify the password', status_code=400)
        if 'email' not in body:
            raise APIException('You need to specify the email', status_code=400)
        if 'zipcode' not in body:
            body['zipcode'] = None

        lawyer1 = Lawyer(name=body['name'], password = body['password'], email = body['email'], zipcode = body['zipcode'], lawfirm= body['lawfirm'])
        db.session.add(lawyer1)
        db.session.commit()

        return "ok", 200
    
    # GET request
    if request.method == 'GET':
        all_lawyer = Lawyer.query.all()
        all_lawyer = list(map(lambda x: x.serialize(), all_lawyer))
        return jsonify(all_lawyer), 200

    return "Invalid Method", 404









# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 4000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
