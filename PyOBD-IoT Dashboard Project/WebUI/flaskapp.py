from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('dashboard.html')
    # Fetch OBD-II data (replace with your actual data fetching logic)
    obd_data = {
        'speed': 55,
        'rpm': 2500,
        'fuel_level': 75,
        # Add more OBD-II data here
    }
    return render_template('dashboard.html', obd_data=obd_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Make the app accessible from other devices
# Use SocketIO to run the app
