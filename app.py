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

room_temps = {}
result = client.query('SELECT LAST(value) FROM "Temperature_°C" GROUP BY "location_specific";')
for k,v in result.items():
    location = k[1]['location_specific']
    for d in v:
        temp = d.get("last")
        room_temps[location] = temp

print(room_temps)

def get_room_temperatures():
    return room_temps

@app.route('/')
def index():
    return render_template('map.html')

@app.route('/temperatures')
def temperatures():
    room_temperatures = get_room_temperatures()
    return jsonify(room_temperatures)

if __name__ == '__main__':
    app.run(debug=True)
