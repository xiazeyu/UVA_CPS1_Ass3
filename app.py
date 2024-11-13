from flask import Flask, render_template, jsonify
import os
from dotenv import load_dotenv
from influxdb import InfluxDBClient

app = Flask(__name__)

load_dotenv()
host = os.getenv("HOST")
port = int(os.getenv("PORT"))
username = os.getenv("USER")
password = os.getenv("PASSWORD")
database = os.getenv("DATABASE")
client = InfluxDBClient(host, port, username, password, database, ssl=True, verify_ssl=True)

def get_room_temperature(room_name):
    temp = None
    result = client.query(f'SELECT value FROM "Temperature_°C" WHERE location_specific = \'{room_name}\' ORDER BY time DESC LIMIT 1;')
    for k,v in result.items():
        for d in v:
            temp = d.get("value")
    return {
        room_name: temp
    }

@app.route('/')
def index():
    return render_template('map.html')

@app.route('/temperature/<room_name>')
def temperature(room_name):
    room_temperature = get_room_temperature(room_name=room_name)
    return jsonify(room_temperature)

if __name__ == '__main__':
    app.run(debug=True)
