from flask import Flask, render_template, jsonify
from werkzeug.utils import quote

app = Flask(__name__)

# Home Route
@app.route('/')
def home():
    return render_template('home.html')

# About Route
@app.route('/about')
def about():
    return render_template('about.html')

# Contact Route
@app.route('/contact')
def contact():
    return render_template('contact.html')

# API Route - Returns JSON Data
@app.route('/api/data')
def api_data():
    sample_data = {
        "temperature": 25.5,
        "humidity": 60,
        "status": "running"
    }
    return jsonify(sample_data)

# Dynamic Route - Profile Page
@app.route('/profile/<username>')
def profile(username):
    safe_username = quote(username)  # Encode special characters
    return render_template('profile.html', username=safe_username)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
