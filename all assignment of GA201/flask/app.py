from flask import Flask, request, jsonify

app = Flask(__name__)

# Initialize the menu with some sample dishes
menu = [
    {'id': 1, 'name': 'Pasta', 'price': 10.99, 'available': True},
    {'id': 2, 'name': 'Pizza', 'price': 12.99, 'available': True},
    {'id': 3, 'name': 'Burger', 'price': 8.99, 'available': False},
    {'id': 4, 'name': 'Salad', 'price': 7.99, 'available': True},
]

@app.route('/menu', methods=['GET'])
def get_menu():
    return jsonify(menu)

@app.route('/menu', methods=['POST'])
def add_dish():
    new_dish = {
        'id': request.json['id'],
        'name': request.json['name'],
        'price': request.json['price'],
        'available': request.json['available']
    }
    menu.append(new_dish)
    return jsonify({'message': 'Dish added successfully'})

@app.route('/menu/<int:dish_id>', methods=['DELETE'])
def remove_dish(dish_id):
    dish = next((dish for dish in menu if dish['id'] == dish_id), None)
    if dish:
        menu.remove(dish)
        return jsonify({'message': 'Dish removed successfully'})
    else:
        return jsonify({'message': 'Dish not found'})

@app.route('/menu/<int:dish_id>', methods=['PUT'])
def update_dish(dish_id):
    dish = next((dish for dish in menu if dish['id'] == dish_id), None)
    if dish:
        dish['name'] = request.json.get('name', dish['name'])
        dish['price'] = request.json.get('price', dish['price'])
        dish['available'] = request.json.get('available', dish['available'])
        return jsonify({'message': 'Dish updated successfully'})
    else:
        return jsonify({'message': 'Dish not found'})


orders = []
order_id_counter = 1

@app.route('/orders', methods=['POST'])
def place_order():
    customer_name = request.json['customer_name']
    dish_ids = request.json['dish_ids']

    # Check if all dishes are available
    for dish_id in dish_ids:
        dish = next((dish for dish in menu if dish['id'] == dish_id and dish['available']), None)
        if not dish:
            return jsonify({'message': f'Dish with ID {dish_id} is not available'})

    # Process the order
    global order_id_counter
    order = {
        'id': order_id_counter,
        'customer_name': customer_name,
        'dish_ids': dish_ids,
        'status': 'received'
    }
    orders.append(order)
    order_id_counter += 1
    return jsonify({'message': 'Order placed successfully', 'order_id': order['id']})

@app.route('/orders/<int:order_id>', methods=['PUT'])
def update_order_status(order_id):
    order = next((order for order in orders if order['id'] == order_id), None)
    if order:
        new_status = request.json.get('status')
        if new_status in ['preparing', 'ready for pickup', 'delivered']:
            order['status'] = new_status
            return jsonify({'message': 'Order status updated successfully'})
        else:
            return jsonify({'message': 'Invalid order status'})
    else:
        return jsonify({'message': 'Order not found'})

@app.route('/orders', methods=['GET'])
def get_orders():
    return jsonify(orders)


@app.route('/exit', methods=['GET'])
def exit_app():
    shutdown_server()
    return 'Server shutting down...'

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug server')
    func()


if __name__ == '__main__':
    app.run()
