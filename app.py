from flask import Flask, jsonify, send_from_directory
import requests

app = Flask(__name__, static_folder='nginx', static_url_path='')

# Define your service endpoints (microservices URLs)
SERVICES = {
    "User Service": "http://user-service:5001/status",
    "Order Service": "http://order-service:5002/status",
    "Product Service": "http://product-service:5003/status"
}


@app.route('/')
def home():
    """Serve the dashboard HTML file."""
    return send_from_directory('nginx', 'index.html')


@app.route('/api/status')
def api_status():
    """Fetch health/status data from all services."""
    data = {}
    for name, url in SERVICES.items():
        try:
            resp = requests.get(url, timeout=3)
            if resp.status_code == 200:
                json_data = resp.json()
                details = "<br>".join([f"<b>{k}</b>: {v}" for k, v in json_data.items()])
                data[name] = {
                    "status": "✅ Running",
                    "color": "green",
                    "details": details
                }
            else:
                data[name] = {
                    "status": f"❌ Error {resp.status_code}",
                    "color": "red",
                    "details": "Invalid response"
                }
        except Exception as e:
            data[name] = {
                "status": "❌ Down",
                "color": "red",
                "details": str(e)
            }
    return jsonify(data)


@app.route('/<path:path>')
def serve_static(path):
    """Serve static files like CSS/JS if needed."""
    return send_from_directory('nginx', path)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
