from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Order service root route!",
        "status": "running"
    })

@app.route('/api/orders/', methods=['GET'])
def orders_home():
    return jsonify({
        "message": "Order service is operational!",
        "service": "Order Service",
        "status": "running"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
