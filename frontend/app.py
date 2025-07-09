"""
Frontend/app.py - Frontend Flask Microservice
============================================

This Flask app acts as the frontend microservice for the project.

**Key Responsibilities:**
- Runs on port 5000 (default Flask port).
- Renders the main HTML form and user interface using Jinja2 templates (see `templates/index.html`).
- Receives user input from the form and proxies (forwards) form submissions to the backend microservice at http://localhost:5001/submit using an HTTP POST request.
- Receives and displays backend responses (including MongoDB document IDs) to the user.
- Handles errors gracefully if the backend is unreachable or returns an error.

**How it Works:**
- When a user visits the home page (`/`), the app renders `index.html` and passes the current day and time for display.
- When a user submits the form, the `/submit` route collects the form data, sends it to the backend, and returns the backend's response to the user.
- The backend is responsible for storing the data in MongoDB and returning a unique document ID.

**Key Concepts for Beginners:**
- **Flask:** A Python web framework for building web apps and APIs. Each route (e.g., `/`, `/submit`) is a Python function.
- **Jinja2 Templates:** Used by Flask to render dynamic HTML pages. Variables like `day_of_week` and `current_time` are passed from Flask to the template.
- **requests Library:** Used to make HTTP requests from Python (here, to send data from frontend to backend).
- **Microservices:** This app is one of two independent Flask services (frontend and backend) that communicate over HTTP.
- **Error Handling:** Always check for errors when making requests to other services and provide user-friendly feedback.

**Security Note:**
- Never commit your `.env` file or sensitive credentials to version control.
- This app is for learning/demo purposes and should not be used as-is in production.
- Always validate and sanitize user input in production apps.

**How to Run:**
1. Make sure your virtual environment is activated and dependencies are installed.
2. Start the backend service first (`python backend/app.py` on port 5001).
3. Start this frontend service (`python Frontend/app.py` on port 5000).
4. Open your browser at `http://localhost:5000`.

For more details, see the README and comments in each file.
"""

# This is a minimal Flask app that serves an HTML page.
from flask import Flask, request, render_template
from datetime import datetime
import requests

app = Flask(__name__)
BACKEND_URL = "http://localhost:5001/submit"

@app.route('/')
def home():
    
    day_of_week = datetime.now().strftime('%A')
    print(f"Today is: {day_of_week}")
    
    return render_template('index.html',day_of_week=day_of_week,current_time=datetime.now().strftime('%H:%M:%S'))
    
@app.route('/submit', methods=['POST'])
def submit():
    form_data = request.form.to_dict()
    requests.post(BACKEND_URL, json=form_data)
   
    # Here you would typically send the data to the backend
    # For demonstration, we will just return the data as a JSON response
    return {"status": "success", "data": form_data}, 200
      
if __name__ == '__main__':
    app.run(debug=True, port=5000)


