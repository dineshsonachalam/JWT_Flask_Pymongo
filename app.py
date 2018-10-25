from flask import Flask
from routes.authentication import authentication_blueprint
from flask_jwt_extended import JWTManager
app = Flask(__name__)

# Register the blueprints
app.register_blueprint(authentication_blueprint)

app.config['JWT_SECRET_KEY'] = 'admin'
app.config['SECRET_KEY'] = "admin" # to use session you need to set secret key

jwt = JWTManager(app)

# Register the blueprint

if __name__ == "__main__":
    app.run(host="localhost",port=5000,debug=True)