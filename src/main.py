import json
import random
import time
from datetime import datetime

from faker import Faker

fake = Faker()


def generate_sensor_data(sensor_id):
    sensor_data = {
        "sensor_id": sensor_id,
        "pm2_5": round(random.uniform(0, 100), 2),
        "pm10": round(random.uniform(0, 150), 2),
        "co2": round(random.uniform(300, 1000), 2),
        "no2": round(random.uniform(0, 50), 2),
        "o3": round(random.uniform(0, 100), 2),
        "temperature": round(random.uniform(10, 40), 2),
        "humidity": round(random.uniform(20, 90), 2),
        "latitude": float(fake.latitude()),
        "longitude": float(fake.longitude()),
        "timestamp": datetime.now().isoformat(),
    }
    return sensor_data


if __name__ == "__main__":
    while True:
        sensor_data = generate_sensor_data(sensor_id="sensor_001")
        print(json.dumps(sensor_data, indent=2))
        time.sleep(5)
