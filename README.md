## Flask Task 1 – Query Parameter to Upper Case

#### 📌 `Project Description`

This is a simple Flask web application that takes a name from the URL as a query parameter and displays it in UPPER CASE on the web page.
The project helps beginners understand:
- How Flask works
- How to create routes
- How to use query parameters in Flask

#### 🚀 `Features`

- Built using Python Flask
- Accepts input using URL query parameters
- Converts the input name to uppercase
- Displays a dynamic HTML response

#### 🛠️ `Technologies Used`

1. Python
2. Flask
3. HTML (via Flask response)

#### ▶️ `How to Run the Project`

1️⃣ Clone the Repository
git clone https://github.com/mrugakshiharkare/Flask--Task-1.git

2️⃣ Navigate to Project Folder
cd Flask--Task-1

3️⃣ Install Flask (if not installed)
pip install flask

4️⃣ Run the Application
python app.py

🌐 How to Use the Application
After running the app, open your browser and visit:
http://127.0.0.1:5000/?name=Mrugakshi

#### ✅ `Output:`
Hello, MRUGAKSHI!
Welcome to the Upper Case Home Page.

🔁 If no name is provided:
http://127.0.0.1:5000/

Output will be:
Hello, GUEST!

#### 🧠 `Key Concepts Used`

1. Flask application setup
2. Routing using @app.route()
3. Query parameters using request.args.get()
4. String manipulation in Python
5. Debug mode for development

#### 🎯 `Learning Outcome`

By completing this task, you will understand:
- How to build a basic Flask app
- How to pass data through URLs
- How backend logic interacts with frontend output
