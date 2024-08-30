from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/payment', methods=['POST'])
def process_payment():
    data = request.json
    return jsonify({"status": "Payment processed", "details": data}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)

