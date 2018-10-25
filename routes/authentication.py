from flask import Blueprint,request,jsonify
from utility.pymongo_crud import register_new_users,user_login
from flask_jwt_extended import (jwt_required, create_access_token,create_refresh_token,get_jwt_identity, jwt_refresh_token_required,
    get_jwt_claims,get_raw_jwt
)

authentication_blueprint = Blueprint('authentication',__name__,template_folder='templates')


@authentication_blueprint.route('/',methods=['GET'],endpoint='read_all_user_names')
def read_all_user_names():
    return "Umm digital"


@authentication_blueprint.route('/signin',methods=['POST'],endpoint='registration')
def registration():
    content = request.get_json()
    username = content['username']
    password = content['password']
    message,status_code = register_new_users(username,password)
    print("Status code:",status_code)
    return jsonify(message)


@authentication_blueprint.route('/login',methods=['POST'],endpoint='login')
def login():
    content = request.get_json()
    username = content['username']
    password = content['password']
    message, status_code = user_login(username, password)
    #print("Access token: ",create_access_token(username))
    print("Status code:", status_code)
    if status_code == 200: # success
       message['access_token'] = create_access_token(username)
       message['refresh_token'] = create_refresh_token(username)
    return jsonify(message)

@authentication_blueprint.route('/dashboard',methods=['GET'],endpoint='dashboard')
@jwt_required
def dashboard():
    username = get_jwt_identity()
    return jsonify(logged_in_as=username), 200

@authentication_blueprint.route('/logout',methods=['GET'],endpoint='logout')
@jwt_required
def logout():
    return jsonify({'message':'Logged out successfully'})

# This method is used to make a new access token by using refresh token.
@authentication_blueprint.route('/refresh',methods=['GET'],endpoint='refresh_token')
@jwt_refresh_token_required
def refresh_token():
    current_user = get_jwt_identity()
    access_token = create_access_token(identity=current_user)
    return jsonify({'access_token': access_token})