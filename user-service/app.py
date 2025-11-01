from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "service": "User Service",
        "status": "running",
        "message": "User service is working fine!"
    })

@app.route('/users')
def users():
    users_data = [
        {"id": 1, "name": "Aryan"},
        {"id": 2, "name": "Ravi"},
        {"id": 3, "name": "Neha"}
    ]
    return jsonify(users_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
