"""
app1.py - Flask App with MongoDB Integration
===========================================

This file demonstrates a Flask web application that connects to a MongoDB database and handles form submissions. Below is an explanation of each section and the key components used:

1. Imports:
   - `from flask import Flask, request, render_template`: Imports Flask's core class, request object for handling incoming data, and render_template for rendering HTML templates.
   - `from datetime import datetime`: Used to get the current date and time.
   - `from pymongo.mongo_client import MongoClient`, `from pymongo.server_api import ServerApi`: Imports classes to connect to MongoDB using the official PyMongo driver.
   - `from dotenv import load_dotenv`: Loads environment variables from a `.env` file for secure configuration.
   - `import os`: Allows access to environment variables and file system operations.
   - `import pymongo`: Imports the main PyMongo package (not strictly needed if you use the above imports, but harmless).

2. Environment Setup:
   - `load_dotenv()`: Loads environment variables from a `.env` file in the project root. This is where your MongoDB URI is stored.
   - `mongo_uri = os.getenv("mongo_uri")`: Reads the MongoDB connection string from the environment. Keeps sensitive info out of your code.
   - Raises an error if the URI is missing.

3. MongoDB Client Setup:
   - `client = MongoClient(uri, server_api=ServerApi('1'))`: Connects to MongoDB using the URI and sets the server API version.
   - The `try/except` block pings the database to confirm a successful connection and prints a message.

4. Flask App Setup:
   - `app = Flask(__name__)`: Creates the Flask application instance.

5. Database and Collection:
   - `db = client["KjoCluster1"]`: Selects the database named `KjoCluster1`.
   - `collection = db["signups"]`: Selects the collection named `signups` (like a table in SQL).

6. Routes:
   - `@app.route('/')`: The home page route. When accessed, it:
     - Gets the current day of the week and time.
     - Prints the day to the console.
     - Renders the `index.html` template, passing the day and time as variables.
   - `@app.route('/submit', methods=['POST'])`: Handles form submissions via POST requests. It:
     - Converts form data to a dictionary.
     - Inserts the data into the `signups` collection in MongoDB.
     - Returns the inserted document's ID as a JSON response (converted to string for compatibility).

7. App Runner:
   - `if __name__ == '__main__': app.run(debug=True)`: Runs the Flask development server if the script is executed directly.

---

**Key Concepts:**
- **Flask**: A lightweight Python web framework for building web applications.
- **PyMongo**: The official MongoDB driver for Python, used to connect and interact with MongoDB databases.
- **dotenv**: Loads environment variables from a `.env` file, keeping sensitive info like database URIs out of your codebase.
- **Jinja2 Templates**: Used by Flask to render dynamic HTML pages (e.g., `index.html`).
- **MongoDB**: A NoSQL database where data is stored as documents in collections.

---

**Security Note:**
- Never commit your `.env` file or sensitive credentials to version control.
- This app is for learning/demo purposes and should not be used as-is in production.
"""

# This is a minimal Flask app that serves an HTML page.
from flask import Flask, request, render_template
from datetime import datetime

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

@app.route('/')
def home():
    
    day_of_week = datetime.now().strftime('%A')
    print(f"Today is: {day_of_week}")
    
    return render_template('index.html',day_of_week=day_of_week,current_time=datetime.now().strftime('%H:%M:%S'))
    
@app.route('/submit', methods=['POST'])
def submit():
    form_data = dict(request.form)    # Get form data as a dictionary
    result = collection.insert_one(form_data)
    # Return a JSON response without ObjectId
    return {'inserted_id': str(result.inserted_id)}
    # Here you can add logic to save the data to MongoDB or process it as needed
    # For demonstration, we will just return the received data
    return form_data
      
    

if __name__ == '__main__':
    app.run(debug=True)


