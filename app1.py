# This is a minimal Flask app that serves an HTML page.
from flask import Flask, request, render_template
from datetime import datetime
app = Flask(__name__)
@app.route('/')
def home():
    
    day_of_week = datetime.now().strftime('%A')
    print(f"Today is: {day_of_week}")
    
    return render_template('index.html',day_of_week=day_of_week,current_time=datetime.now().strftime('%H:%M:%S'))
    
@app.route('/submit', methods=['POST'])
def submit():
    from flask import jsonify
    if request.is_json:
        form_data = request.get_json()
        print(f"Received JSON data: {form_data}")
        name = form_data.get('name', 'Guest')
        print(f"Welcome {name}.")
        return jsonify(form_data)
    elif request.form:
        form_data = request.form.to_dict()
        print(f"Received form data: {form_data}")
        name = form_data.get('name', 'Guest')
        print(f"Welcome {name}.")
        return jsonify(form_data)
    else:
        return jsonify({"error": "No data received"}), 400
      
    

if __name__ == '__main__':
    app.run(debug=True)


