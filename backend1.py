from flask import Flask, request, jsonify
from database import init_db, add_inventory_item, get_inventory
from model import predict_demand

app = Flask(__name__)
init_db()

@app.route('/inventory', methods=['GET', 'POST'])
def inventory():
    if request.method == 'POST':
        data = request.json
        add_inventory_item(data['item_id'], data['quantity'])
        return jsonify({'status': 'Item added/updated'}), 201
    else:
        items = get_inventory()
        return jsonify(items)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    item_id = data['item_id']
    current_quantity = data['current_quantity']
    forecast = predict_demand(item_id, current_quantity)
    return jsonify({'predicted_demand': forecast})

if __name__ == '__main__':
    app.run(debug=True)
