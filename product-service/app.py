from flask import Flask, request, jsonify

app = Flask(__name__)
products = {}

@app.route('/products', methods=['POST'])
def create_product():
    data = request.json
    product_id = len(products) + 1
    products[product_id] = data
    return jsonify({"product_id": product_id}), 201

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = products.get(product_id)
    if product:
        return jsonify(product)
    return jsonify({"error": "Product not found"}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)

