from flask import Flask, jsonify, request

app = Flask(__name__)

groceries = [
    {"id": 1, "name": "Apple", "category": "Fruits"},
    {"id": 2, "name": "Milk", "category": "Dairy"},
    {"id": 3, "name": "Carrot", "category": "Vegetables"},
    {"id": 4, "name": "Rice", "category": "Grains"},
    {"id": 5, "name": "Eggs", "category": "Protein"}
]

@app.route('/', methods=['GET'])
def home():
    return 'Welcome to the Grocery Store API'


# Route to get all grocery items
@app.route('/groceries', methods=['GET'])
def get_groceries():
    return jsonify(groceries)


# Route to get a specific grocery item by ID
@app.route('/groceries/<int:item_id>', methods=['GET'])
def get_grocery(item_id):
    for item in groceries:
        if item['id'] == item_id:
            return jsonify(item)
    return jsonify({'error': 'Item not found'})


# Route to add a new grocery item
@app.route('/groceries', methods=['POST'])
def add_grocery():
    new_item = {
        "id": request.json['id'],
        "name": request.json['name'],
        "category": request.json['category'],
    }
    groceries.append(new_item)
    return jsonify({'message': 'Grocery item added successfully'})


# Route to update an existing grocery item
@app.route('/groceries/<int:item_id>', methods=['PUT'])
def update_grocery(item_id):
    for item in groceries:
        if item['id'] == item_id:
            item['name'] = request.json['name']
            item['category'] = request.json['category']
            return jsonify({'message': 'Grocery item updated successfully'})
    return jsonify({'error': 'Item not found'})


# Route to delete a grocery item
@app.route('/groceries/<int:item_id>', methods=['DELETE'])
def delete_grocery(item_id):
    for item in groceries:
        if item['id'] == item_id:
            groceries.remove(item)
            return jsonify({'message': 'Grocery item deleted successfully'})
    return jsonify({'error': 'Item not found'})

if __name__ == '__main__':
    app.run(debug=True)
