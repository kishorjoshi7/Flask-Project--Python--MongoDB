"""
backend/app.py - Backend Flask Microservice
==========================================

This Flask app acts as the backend microservice for the project.

**Key Responsibilities:**
- Runs on port 5001 (default for backend in this project).
- Receives form data from the frontend (via POST to /submit), stores it in MongoDB Atlas, and returns the inserted document's ID as a JSON response.
- Exposes /submit (POST) for data insertion and /view (GET) for viewing all signups in the database.
- Converts MongoDB ObjectId to string for JSON compatibility (since ObjectId is not natively serializable).
- Handles MongoDB connection errors and authentication issues gracefully, printing errors to the console.
- Enable CORS if frontend and backend are on different origins/ports (see flask-cors package).

**How it Works:**
- On startup, loads environment variables from `.env` (using python-dotenv) to get the MongoDB URI.
- Connects to MongoDB Atlas using PyMongo and verifies the connection with a ping.
- Defines a `/submit` route that accepts JSON data, inserts it into the `signups` collection, and returns the new document's ID.
- Defines a `/view` route that returns all signups (with `_id` fields removed for privacy).

**Key Concepts for Beginners:**
- **Flask:** A Python web framework for building web apps and APIs. Each route (e.g., `/submit`, `/view`) is a Python function.
- **PyMongo:** The official MongoDB driver for Python, used to connect and interact with MongoDB databases.
- **Environment Variables:** Used to keep sensitive info (like database URIs) out of your code. Loaded from `.env` using `python-dotenv`.
- **CORS:** Cross-Origin Resource Sharing. Needed if your frontend and backend run on different ports or domains.
- **Error Handling:** Always check for connection errors and handle them gracefully.

**Security Note:**
- Never commit your `.env` file or sensitive credentials to version control.
- This app is for learning/demo purposes and should not be used as-is in production.
- Always validate and sanitize user input in production apps.

**How to Run:**
1. Make sure your virtual environment is activated and dependencies are installed.
2. Ensure your `.env` file contains a valid `mongo_uri` for MongoDB Atlas.
3. Start this backend service (`python backend/app.py` on port 5001).
4. Start the frontend service separately (`python Frontend/app.py` on port 5000).
5. The frontend will send data to this backend for storage and retrieval.

For more details, see the README and comments in each file.
"""

# This is a minimal Flask app that serves an HTML page.
from flask import Flask, request


from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
# Load environment variables from .env file
from dotenv import load_dotenv
import os
import pymongo

load_dotenv()
# MongoDB connection URI
mongo_uri = os.getenv("mongo_uri")
if not mongo_uri:
    raise ValueError("MongoDB URI not found in environment variables.")

uri = mongo_uri

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
app = Flask(__name__)

db = client["KjoCluster1"]
collection = db["signups"]


    
@app.route('/submit', methods=['POST'])
def submit():
    form_data = dict(request.json)    # Get form data as a dictionary
    result = collection.insert_one(form_data)
    # Return a JSON response without ObjectId
    return {'inserted_id': str(result.inserted_id)}
    # Here you can add logic to save the data to MongoDB or process it as needed
    # For demonstration, we will just return the received data
    return form_data

@app.route('/view')
def view():
    data = collection.find()
    data = list(data)
    for item in data:
        print(item)
        if '_id' in item:
            del item['_id']
    return {'data': data}
    
if __name__ == '__main__':
    app.run(debug=True, port=5001)


