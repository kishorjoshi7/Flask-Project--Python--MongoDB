# Flask-Tutorial Documentation

This repository demonstrates how to build a minimal Flask web application with MongoDB integration. Below is a detailed explanation of each file and its purpose in the project.

---

## 1. `app.py`
A minimal Flask app that demonstrates basic routing and returning simple responses. It includes:
- A root route (`/`) that returns a welcome message.
- An about route (`/about`) for demonstration.
- An API route (`/api/<name>`) that returns a message with the name provided in the URL.
- Extensive docstring at the top explaining each line and how Flask works.

**Purpose:**
- To help beginners understand the basics of Flask routing and responses.

---

## 2. `app1.py`
A more advanced Flask app that:
- Connects to a MongoDB database using credentials from a `.env` file.
- Uses the `python-dotenv` package to load environment variables.
- Uses `pymongo` to connect to MongoDB, select a database (`KjoCluster1`), and a collection (`signups`).
- Has a root route (`/`) that renders `index.html` and passes the current day and time.
- Has a `/submit` route that accepts POST requests, saves form data to MongoDB, and returns the inserted document's ID as a JSON response.
- Handles MongoDB connection errors and authentication issues gracefully.

**Purpose:**
- To demonstrate how to integrate Flask with MongoDB for data storage.
- To show how to handle form submissions and return JSON responses.

---

## 3. `templates/index.html`
A simple HTML template for the signup page. Features:
- Uses Bulma CSS for styling.
- Sets the background color and text color using internal CSS.
- Displays a welcome message and can be extended to include a signup form.
- Receives variables from Flask (e.g., `day_of_week`, `current_time`).

**Purpose:**
- To provide a user interface for the Flask app.
- To demonstrate how to use Jinja2 templating with Flask.

---

## 4. `.env` (not included in repo, but required)
A file to store sensitive environment variables, such as your MongoDB connection string:
```
mongo_uri=mongodb+srv://<username>:<password>@<cluster-url>/<dbname>?retryWrites=true&w=majority
```
**Purpose:**
- Keeps credentials and configuration out of source code for security.

---

## 5. `flaskenv/` (virtual environment folder)
Contains the Python virtual environment for the project, including all installed packages (Flask, pymongo, python-dotenv, etc.).

**Purpose:**
- Isolates project dependencies from your global Python installation.

---

## 6. `requirements.txt`
A file listing all Python packages required to run this project. Example contents:
```
Flask
pymongo
python-dotenv
```
**Purpose:**
- Allows users to install all dependencies at once using:
  ```
  pip install -r requirements.txt
  ```

---

## Key Packages Used
- **Flask:** Web framework for Python.
- **pymongo:** MongoDB driver for Python.
- **python-dotenv:** Loads environment variables from a `.env` file.
- **Bulma:** CSS framework for styling HTML pages.

---

## How to Run the Project
1. Clone the repository.
2. Create a `.env` file with your MongoDB URI.
3. Activate the virtual environment: `source flaskenv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt` (if available)
5. Run the app: `python3 app1.py`
6. Open your browser at `http://127.0.0.1:5000`

---

## Notes
- Make sure your MongoDB credentials are correct and your IP is whitelisted if using MongoDB Atlas.
- The `/submit` route expects form data and will store it in the `signups` collection.
- The project is for educational/demo purposes and should not be used as-is in production.

---

## More Details

### `templates/index.html`
This file is the main HTML template rendered by Flask for the signup page. It uses Jinja2 templating to display dynamic content passed from Flask (like `day_of_week` and `current_time`).
- Uses Bulma CSS for modern styling.
- Contains internal CSS for background and text color.
- Can be extended to include forms and more interactive elements.
- Example usage in Flask: `render_template('index.html', day_of_week=..., current_time=...)`

### `flaskenv/` (Virtual Environment Folder)
This directory contains your Python virtual environment. It includes all installed packages and Python binaries specific to this project.
- You should not edit files in this folder manually.
- To activate: `source flaskenv/bin/activate`
- Not included in version control (see `.gitignore`).

### `.gitignore`
A file that tells Git which files and folders to ignore in version control. Typical contents for a Flask project:
```
flaskenv/
.env
__pycache__/
*.pyc
```
- Prevents sensitive files (like `.env`) and unnecessary files (like virtual environments and Python cache) from being committed to your repository.

---

For further questions, see the comments in each file or ask for more detailed documentation on any part of the codebase.
