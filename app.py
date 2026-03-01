import logging
from flask import Flask, request, jsonify

app = Flask(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

@app.route('/error', methods=['GET'])
def error():
    app.logger.error("Simulated server error on /error route")
    return jsonify({"error": "Something went wrong"}), 500

@app.route('/user', methods=['POST'])
def user():
    data = request.get_json()

    if not data or "username" not in data:
        app.logger.warning("Username not provided in /user request")
        return jsonify({"error": "Username is required"}), 400

    app.logger.info(f"User {data['username']} accessed /user endpoint")
    return jsonify({"message": f"Hello, {data['username']}!"}), 200

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if data.get("username") == "admin" and data.get("password") == "secret":
        app.logger.info("Successful login attempt")
        return jsonify({"message": "Login successful"}), 200

    app.logger.warning("Invalid login attempt")
    return jsonify({"message": "Invalid credentials"}), 401

if __name__ == '__main__':
    app.run(debug=True)
