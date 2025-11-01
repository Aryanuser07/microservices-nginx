from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Product service root route!",
        "status": "running"
    })

@app.route('/api/products/', methods=['GET'])
def products_home():
    return jsonify({
        "message": "Product service is operational!",
        "service": "Product Service",
        "status": "running"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
