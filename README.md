# 🌍 AI-Powered IoT Air Quality & Pollution Monitoring Dashboard

## 📌 Project Overview

The **AI-Powered IoT Air Quality & Pollution Monitoring Dashboard** is a smart environmental monitoring system designed to measure, analyze, visualize, and predict air pollution levels in real time.

The system collects air quality parameters such as:

* Air Quality Index (AQI)
* Gas Concentration (MQ135)
* Smoke/Gas Level (MQ2)
* Temperature
* Humidity

The collected data is processed and displayed on an interactive dashboard built with Streamlit. The platform supports both real IoT hardware (ESP32 + Sensors) and virtual simulation, making it suitable for students, researchers, and smart city applications.

---

# 🎯 Objectives

* Monitor air quality in real time.
* Detect pollution events and hazardous conditions.
* Generate alerts when pollution exceeds safe thresholds.
* Visualize environmental data through interactive dashboards.
* Store historical records for analysis.
* Predict future AQI values using Machine Learning.
* Support smart city environmental monitoring.
* Provide a GitHub-ready IoT portfolio project.

---

# 🚀 Key Features

## Core Features

✅ Real-Time Air Quality Monitoring

✅ AQI Classification

✅ Temperature & Humidity Monitoring

✅ Pollution Status Detection

✅ Air Quality Alerts

✅ Historical Data Logging

✅ CSV Export

✅ PDF Report Generation

---

## Dashboard Features

✅ Interactive Streamlit Dashboard

✅ AQI Gauge Meter

✅ AQI Trend Charts

✅ Temperature Trend Charts

✅ Humidity Trend Charts

✅ Pollution Distribution Pie Chart

✅ Correlation Heatmap

✅ AQI Histogram

✅ Analytics Dashboard

---

## Smart City Features

✅ Multi-Node Monitoring

✅ School Monitoring Node

✅ Hospital Monitoring Node

✅ Industrial Area Monitoring Node

✅ Traffic Zone Monitoring Node

✅ Pollution Ranking

✅ Hotspot Detection

✅ Smart City Command Center

✅ Interactive Pollution Map

---

## AI Features

✅ AQI Prediction

✅ Forecast Visualization

✅ Smart Recommendations

✅ Environmental Risk Score

---

## IoT Features

✅ ESP32 Compatible

✅ MQTT Ready

✅ ThingSpeak Ready

✅ Node-RED Ready

✅ Real-Time Sensor Streaming

---

# 🏗 System Architecture

```text
MQ135 Sensor
      │
MQ2 Sensor
      │
DHT22 Sensor
      │
      ▼
   ESP32
      │
      ▼
 Data Processing
      │
      ▼
 AQI Calculation
      │
      ▼
 Dashboard
      │
 ┌────┴────┐
 ▼         ▼
Alerts   Reports
      │
      ▼
 Machine Learning
      │
      ▼
 AQI Prediction
```

---

# 🧩 Technologies Used

## Programming Languages

* Python
* C++
* Arduino IDE

## Libraries

* Streamlit
* Pandas
* NumPy
* Plotly
* Scikit-Learn
* ReportLab

## IoT Platforms

* ESP32
* ThingSpeak
* MQTT
* Node-RED

## Data Storage

* CSV Files

---

# 📂 Project Structure

```text
IoT-Air-Quality-Monitoring/

│
├── dashboard/
│   └── dashboard.py
│
├── simulation/
│   └── sensor_simulator.py
│
├── data/
│   └── air_quality.csv
│
├── reports/
│
├── images/
│
├── circuit_diagram/
│
├── arduino_code/
│   └── esp32_air_quality.ino
│
├── README.md
│
├── requirements.txt
│
└── .gitignore
```

---

# 🔌 Hardware Components

| Component | Purpose                |
| --------- | ---------------------- |
| ESP32     | Main Controller        |
| MQ135     | Air Quality Sensor     |
| MQ2       | Smoke/Gas Sensor       |
| DHT22     | Temperature & Humidity |
| Buzzer    | Alert System           |
| LED       | Status Indicator       |
| OLED/LCD  | Display Output         |
| WiFi      | Cloud Communication    |

---

# 🖥 Dashboard Screens

### Dashboard Page

* AQI Meter
* Live Sensor Values
* AQI Prediction
* Health Recommendations
* AQI Trends
* Temperature Trends
* Humidity Trends

### Analytics Page

* AQI Statistics
* Correlation Heatmap
* Pollution Histogram
* Hotspot Detection
* Pollution Ranking
* Interactive Map
* Forecast Analysis

---

# 🌍 Multi-Node Monitoring

The project simulates multiple monitoring stations:

| Node         | Location          |
| ------------ | ----------------- |
| School       | Educational Area  |
| Hospital     | Healthcare Area   |
| Industry     | Industrial Zone   |
| Traffic Zone | High Traffic Area |

Each node generates environmental readings independently.

---

# 🤖 Machine Learning

The system uses Linear Regression to:

* Analyze AQI history
* Predict future AQI
* Forecast pollution trends

Predicted AQI is displayed directly on the dashboard.

---

# 🚨 Alert System

The system automatically generates alerts.

## AQI Categories

| AQI       | Status    |
| --------- | --------- |
| 0 – 50    | Good      |
| 51 – 100  | Moderate  |
| 101 – 200 | Poor      |
| > 200     | Hazardous |

When AQI exceeds 200:

* Alert generated
* Warning displayed
* Hazardous condition recorded

---

# 📊 Data Logging

Every sensor reading is stored in:

```text
data/air_quality.csv
```

Stored Parameters:

* Timestamp
* Node
* MQ135
* MQ2
* Temperature
* Humidity
* AQI
* Status
* Alert
* Battery
* Sensor Health
* Latitude
* Longitude

---

# 📄 Report Generation

The dashboard can generate PDF reports containing:

* Average AQI
* Maximum AQI
* Minimum AQI
* Total Alerts
* Monitoring Summary

Reports are stored inside:

```text
reports/
```

---

# ▶️ Installation

## Step 1

Clone Repository

```bash
git clone https://github.com/yourusername/IoT-Air-Quality-Monitoring.git
```

---

## Step 2

Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 3

Start Simulator

```bash
python simulation/sensor_simulator.py
```

---

## Step 4

Run Dashboard

```bash
streamlit run dashboard/dashboard.py
```

---

# 📷 Screenshots Checklist

Capture the following screenshots:

✅ Project Folder Structure

✅ Circuit Diagram

✅ Simulator Running

✅ Dashboard Home Page

✅ AQI Gauge

✅ AQI Prediction

✅ Analytics Dashboard

✅ Pollution Ranking

✅ Interactive Map

✅ PDF Report

✅ CSV Dataset

✅ GitHub Repository

---

# 🌐 Future Improvements

* Real ESP32 Integration
* MQTT Live Streaming
* ThingSpeak Cloud Dashboard
* Node-RED Dashboard
* Telegram Alerts
* Email Alerts
* Mobile Application
* AI-Based Pollution Forecasting
* Smart City Deployment
* Solar-Powered Sensor Nodes

---
# screenshots
<img width="1366" height="768" alt="Screenshot 2026-06-13 130236" src="https://github.com/user-attachments/assets/16929d03-598f-43b0-9c32-7e2397e08440" />
<img width="1366" height="768" alt="Screenshot 2026-06-13 130304" src="https://github.com/user-attachments/assets/100fa1db-3aed-4cbf-8f48-c3818606a2da" />
<img width="1366" height="768" alt="Screenshot 2026-06-13 130316" src="https://github.com/user-attachments/assets/344f6b90-91e0-440e-9aa3-e2273ccde1ed" />
<img width="1366" height="768" alt="Screenshot 2026-06-13 130329" src="https://github.com/user-attachments/assets/da6d5b84-61ef-43d4-a71b-88852a1922ae" />
<img width="1366" height="768" alt="Screenshot 2026-06-13 130340" src="https://github.com/user-attachments/assets/1aff2df3-b18d-42ab-ad75-09076e084f08" />


# 💼 Resume Description

Developed an AI-Powered IoT Air Quality Monitoring Dashboard using Python, Streamlit, Machine Learning, and IoT concepts. The system performs real-time environmental monitoring, AQI classification, pollution analytics, predictive forecasting, multi-node monitoring, and report generation. Built a smart-city-inspired dashboard with interactive visualizations, alerts, and environmental intelligence features.

---

# 🎤 Interview Question

### Explain Your Project

This project is an AI-powered IoT air quality monitoring system that measures environmental conditions such as air quality, gas concentration, temperature, and humidity. The system calculates AQI, classifies pollution levels, generates alerts, stores historical data, predicts future AQI using machine learning, and visualizes everything through an interactive Streamlit dashboard. It supports both virtual simulation and real ESP32-based hardware deployment, making it suitable for smart city and environmental monitoring applications.

---

# 👩‍💻 Author

Tanisha Mittal

B.Tech Electronics & Communication Engineering

IoT | AI | Machine Learning | Data Analytics | Smart Systems

---

⭐ If you found this project useful, consider giving it a star on GitHub.
