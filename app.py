# # S1: Import Flask
# from flask import Flask, request

# # S2: Initialize object:
# app = Flask(__name__)

# # S3: Route:
# # Task: Takes 'name' from query parameter and converts to UPPER CASE
# @app.route('/')
# def home():
#     # Looks for ?name=yourname in the URL
#     user_name = request.args.get('name', 'Guest')
#     upper_name = user_name.upper()
    
#     return f"<h1>Hello, {upper_name}!</h1><p>Welcome to the Upper Case Home Page.</p>"

# # S4: Run the Application:
# if __name__ == '__main__':
#     app.run(debug = True)

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    # Get name from URL query parameter
    name = request.args.get('name')

    if name:
        return f"""
        <h1>Hello {name.upper()} 👋</h1>
        <p>Your name in UPPER CASE is: <b>{name.upper()}</b></p>
        """
    else:
        return """
        <h1>Welcome Intern 😄</h1>
        <p>Please provide your name in URL like this:</p>
        <p><b>?name=yourname</b></p>
        """

if __name__ == '__main__':
    app.run(debug=True)
