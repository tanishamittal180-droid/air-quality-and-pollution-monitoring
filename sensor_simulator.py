import pandas as pd
import random
import time
import os
from datetime import datetime

FILE = "data/air_quality.csv"

os.makedirs("data", exist_ok=True)

nodes = {
    "School": {
        "lat": 28.7041,
        "lon": 77.1025
    },
    "Hospital": {
        "lat": 28.6139,
        "lon": 77.2090
    },
    "Industry": {
        "lat": 28.5355,
        "lon": 77.3910
    },
    "Traffic Zone": {
        "lat": 28.4595,
        "lon": 77.0266
    }
}

columns = [
    "timestamp",
    "node",
    "mq135",
    "mq2",
    "temperature",
    "humidity",
    "aqi",
    "status",
    "alert",
    "battery",
    "sensor_health",
    "lat",
    "lon"
]

if not os.path.exists(FILE):
    pd.DataFrame(columns=columns).to_csv(
        FILE,
        index=False
    )

def classify(aqi):

    if aqi <= 50:
        return "Good"

    elif aqi <= 100:
        return "Moderate"

    elif aqi <= 200:
        return "Poor"

    return "Hazardous"

while True:

    current_hour = datetime.now().hour

    rows = []

    for node, location in nodes.items():

        # Day/Night Pattern

        if 6 <= current_hour <= 10:

            traffic_factor = 40

        elif 17 <= current_hour <= 21:

            traffic_factor = 50

        else:

            traffic_factor = 10

        # Base Pollution

        if node == "Industry":

            base = random.randint(180, 320)

        elif node == "Traffic Zone":

            base = random.randint(120, 250)

        elif node == "Hospital":

            base = random.randint(70, 150)

        else:

            base = random.randint(40, 120)

        # Random Pollution Event

        event = random.choice([
            0,
            0,
            0,
            0,
            50,
            100
        ])

        mq135 = base + traffic_factor + event

        mq2 = mq135 + random.randint(
            -20,
            20
        )

        temperature = round(
            random.uniform(20, 45),
            2
        )

        humidity = round(
            random.uniform(30, 90),
            2
        )

        aqi = int(
            (mq135 + mq2) / 2
        )

        status = classify(aqi)

        alert = (
            "YES"
            if aqi > 200
            else "NO"
        )

        battery = random.randint(
            70,
            100
        )

        sensor_health = random.choice([
            "Healthy",
            "Healthy",
            "Healthy",
            "Warning"
        ])

        rows.append({

            "timestamp":
            datetime.now(),

            "node":
            node,

            "mq135":
            mq135,

            "mq2":
            mq2,

            "temperature":
            temperature,

            "humidity":
            humidity,

            "aqi":
            aqi,

            "status":
            status,

            "alert":
            alert,

            "battery":
            battery,

            "sensor_health":
            sensor_health,

            "lat":
            location["lat"],

            "lon":
            location["lon"]

        })

    pd.DataFrame(rows).to_csv(

        FILE,

        mode="a",

        header=False,

        index=False

    )

    print(
        "Generated Smart City Sensor Data"
    )

    time.sleep(5)