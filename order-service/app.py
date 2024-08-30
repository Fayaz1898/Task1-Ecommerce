from flask import Flask, request, jsonify

app = Flask(__name__)
orders = {}

@app.route('/orders', methods=['POST'])
def create_order():
    data = request.json
    order_id = len(orders) + 1
    orders[order_id] = data
    return jsonify({"order_id": order_id}), 201

@app.route('/orders/<int:order_id>', methods=['GET'])
def get_order(order_id):
    order = orders.get(order_id)
    if order:
        return jsonify(order)
    return jsonify({"error": "Order not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)

