import csv
import json
import time
import random
from datetime import datetime

# ----- CONFIG -----
INTERVAL = 5  # seconds between readings
CSV_FILE = "sensor_data.csv"
JSON_FILE = "sensor_data.json"
DEVICE_IDS = ["sensor_01", "sensor_02", "sensor_03"]

# ----- CSV HEADER -----
def init_csv():
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["timestamp", "device_id", "temperature", "humidity"])

# ----- GENERATE SENSOR READING -----
def generate_reading():
    return {
        "timestamp": datetime.utcnow().isoformat(),
        "device_id": random.choice(DEVICE_IDS),
        "temperature": round(random.uniform(20, 40), 2),  # °C
        "humidity": round(random.uniform(30, 70), 2)      # %
    }

# ----- APPEND TO CSV -----
def write_to_csv(data):
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([data["timestamp"], data["device_id"], data["temperature"], data["humidity"]])

# ----- APPEND TO JSON -----
def write_to_json(data):
    with open(JSON_FILE, mode='a') as file:
        json.dump(data, file)
        file.write("\n")

# ----- MAIN LOOP -----
def main():
    print("Starting IoT Sensor Data Generator...")
    init_csv()

    while True:
        reading = generate_reading()
        print("Generated:", reading)

        write_to_csv(reading)
        write_to_json(reading)

        time.sleep(INTERVAL)

if __name__ == "__main__":
    main()
