from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "service": "Product Service",
        "status": "running",
        "message": "Product service is active!"
    })

@app.route('/products')
def products():
    products_data = [
        {"id": 101, "name": "Laptop", "price": 65000},
        {"id": 102, "name": "Headphones", "price": 2500},
        {"id": 103, "name": "Keyboard", "price": 1200}
    ]
    return jsonify(products_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
