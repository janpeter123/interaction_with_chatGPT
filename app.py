#Importing necessary libraries
import os
from flask_cors import CORS, cross_origin
from flask import Flask, request, abort

#Importing dotenv library
from dotenv import load_dotenv

#Loading Environment Variables
load_dotenv()

#Using a enrivonment variable
user = os.getenv('USER')


#Initializing Flask Application
app = Flask(__name__)

#Enabling CORS
CORS(app, support_credentials=True)


# ====== Routes ======

# Index Route -  Test route
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

#POST Route sample
@app.route("/api/v2/post",methods=['POST'])
def post_route():
    
    #Getting request data as JSON object
    data = request.get_json()

    #Returning request body and code 200.
    return data,200