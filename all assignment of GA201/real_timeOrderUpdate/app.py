from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
socketio = SocketIO(app)

# Store order status data
order_status_data = {}

# WebSocket event handlers
@socketio.on('connect')
def handle_connect():
    emit('order_status_data', order_status_data)

@socketio.on('update_order_status')
def handle_update_order_status(data):
    order_id = data['order_id']
    new_status = data['new_status']
    order_status_data[order_id] = new_status
    emit('order_status_update', data, broadcast=True)

# Route for order tracking page
@app.route('/order-tracking')
def order_tracking():
    return render_template('order_tracking.html')

# Route for order status update page
@app.route('/order-status-update')
def order_status_update():
    return render_template('order_status_update.html')

if __name__ == '__main__':
    socketio.run(app)
