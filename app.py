# S1: Import Flask
from flask import Flask, request

# S2: Initialize object:
app = Flask(__name__)

# S3: Route:
# Task: Takes 'name' from query parameter and converts to UPPER CASE
@app.route('/')
def home():
    # Looks for ?name=yourname in the URL
    user_name = request.args.get('name', 'Guest')
    upper_name = user_name.upper()
    
    return f"<h1>Hello, {upper_name}!</h1><p>Welcome to the Upper Case Home Page.</p>"

# S4: Run the Application:
if __name__ == '__main__':
    app.run(debug = True)

