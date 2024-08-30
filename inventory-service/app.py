from flask import Flask, request, jsonify

app = Flask(__name__)
inventory = {}

@app.route('/inventory', methods=['POST'])
def update_inventory():
    data = request.json
    product_id = data['product_id']
    quantity = data['quantity']
    inventory[product_id] = quantity
    return jsonify({"status": "Inventory updated"}), 200

@app.route('/inventory/<int:product_id>', methods=['GET'])
def get_inventory(product_id):
    quantity = inventory.get(product_id)
    if quantity is not None:
        return jsonify({"product_id": product_id, "quantity": quantity})
    return jsonify({"error": "Inventory not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5004)

