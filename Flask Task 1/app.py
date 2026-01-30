from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    name = request.args.get('name', '')
    upper_name = name.upper()

    # Get current hour
    hour = datetime.now().hour

    # Decide greeting
    if hour < 12:
        greeting = "Good Morning"
    elif hour < 17:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Evening"

    return f"<h1>{greeting}, {upper_name}!</h1>"

if __name__ == '__main__':
    app.run(debug=True)