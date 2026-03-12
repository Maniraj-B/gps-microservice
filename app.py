from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/location')
def location():
    data = {
        "classroom": "IIIT Kottayam Cloud Computing Lab",
        "latitude": 9.7548898,
        "longitude": 76.6500927
    }
    return jsonify(data)

@app.route('/health')
def health():
    return "Service running"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)