from pymongo import MongoClient
from bson.objectid import ObjectId

# Creating a client connection to mongodb instance
client = MongoClient('localhost:27017')

# Creating a database object to insert data to mongodb instance.
db = client.user_details

# Create new users
def register_new_users(username,password):
    # check if username already exists
    if( (db.users.find({'username':username})).count() > 0 ):
        # username already exists in the database
        return {'message': 'User {} already exists'.format(username)},500
    else: # insert document to collection
        db.users.insert_one({'username':username,'password':password})
        return {'message':'User {} created successfully.'.format(username)},200


def user_login(username,password):
    # check if username exits in db
    if( db.users.find({'username':username}).count()>0 ):
        if(db.users.find({'username':username,'password':password}).count()>0):
            return {'message':'User {} logged in successfully'.format(username)},200
        else:
            return {'message':'Password is incorrect'},500
    else:
        return {'message':'User {} doesnt exist. Please register.'.format(username)},500


