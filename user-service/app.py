from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "User service root route!",
        "status": "running"
    })

@app.route('/api/users/', methods=['GET'])
def users_home():
    return jsonify({
        "message": "User service is operational!",
        "service": "User Service",
        "status": "running"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
