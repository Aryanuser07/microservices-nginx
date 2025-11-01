from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "service": "Order Service",
        "status": "running",
        "message": "Order service is operational!"
    })

@app.route('/orders')
def orders():
    orders_data = [
        {"order_id": 1, "user_id": 1, "product_id": 101},
        {"order_id": 2, "user_id": 2, "product_id": 103},
        {"order_id": 3, "user_id": 3, "product_id": 102}
    ]
    return jsonify(orders_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
