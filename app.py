"""
Flask Minimal App Example
========================

This file demonstrates a minimal Flask web application. Flask is a lightweight web framework for Python that allows you to build web applications quickly and with minimal code.

Line-by-line explanation:

1. `from flask import Flask`
   - Imports the Flask class from the flask package. Flask is the main class used to create a Flask web application.

2. `app = Flask(__name__)`
   - Creates an instance of the Flask application. The `__name__` variable tells Flask where to look for resources such as templates and static files. It helps Flask determine the root path of the application.

3. `@app.route('/')`
   - This is a route decorator. It tells Flask that the function immediately following it should be called when the root URL ('/') of the web application is accessed. In other words, it maps the URL path `/` to the `home` function.

4. `def home():`
   - Defines the view function for the root URL. When a user visits the root URL, this function is executed.

5. `return "Hello, Flask!"`
   - Returns the string "Hello, Flask!" as the HTTP response. This is what the user will see in their browser when they visit the root URL.

6. `if __name__ == '__main__':`
   - This line checks if the script is being run directly (not imported as a module). If so, it will execute the code inside the block.

7. `app.run(debug=True)`
   - Starts the Flask development server. The `debug=True` flag enables debug mode, which provides helpful error messages and automatically reloads the server when code changes are made.

How to run this app:
--------------------
1. Make sure Flask is installed in your Python environment.
2. Save this file as `app.py`.
3. Run the app using: `python3 app.py`
4. Open your browser and go to: http://127.0.0.1:5000/

You should see "Hello, Flask!" displayed in your browser.
"""

#This minimal app using Flask, Just a start to understand how Flask works

from flask import Flask, request
app= Flask(__name__)
@app.route('/')
def home():
    return "Hello, Flask!"
@app.route('/about')  
def about():
    return "This is the About page KJO."


# Below function for getting value from any url or api.
@app.route('/api/<name>')
def name(name):
    # Here you can implement logic to fetch data from an API or database
    # For demonstration, we will just return the name passed in the URL
    return f"You accessed the API with name: {name}"


#We can get data using request object in Flask.below is the example of how to get data from a URL or API.

@app.route('/url')
def kjo():
    name = request.values.get('name')
    age = request.values.get('age')
    age = int(age)
    if age > 18:
        return f"Hello {name}, you are an adult."
    else:
        return f"Hello {name}, you are a minor and this site isn't for you."

if __name__ == '__main__':
    app.run(debug=True)
# you need to give name and age in the URL like this: http://127.0.0.1:5000/url?name=kjo&age=1
# You can then access it in your web browser at http://127.0.0.
# 5000/get_value/some_url 

# To run this app, save it as app.py and run it using the command: python3 app.py
# You can then access it in your web browser at http://127.0.0.
