import requests
import pymongo

#setting the database pre-prerequirements

connection_params = {
'user' : 'mohamad-aref',
'password' : '37788570b',
'host' : 'ds121624.mlab.com',
'port': 21624,
'namespace' = 'users'
}

#the request that should be made to connect to our mongo database

connection = MongoClient(
'mongodb://{user}:{password}@{host}:'
'{port}/{namespace}'.format(**connection_params)
)

db = connection.users

#a function for saving datas in database

def savetodb(user):
    db.members.insert(user)
