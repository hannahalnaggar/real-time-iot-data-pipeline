# Real-Time IoT Data Pipeline 🚀

## 📌 Project Overview
This project simulates IoT sensor data (temperature, humidity), processes it in **batch and streaming modes**, and visualizes the results on a real-time dashboard.  
It demonstrates key **data engineering concepts** like **ETL**, **streaming analytics**, and **cloud-native orchestration**.

---

## 🧩 Architecture
1. **Data Simulation**: Python script generates IoT sensor readings every 5 seconds.
2. **Batch Processing (ETL)**: Cleans and stores data in a SQL database or data lake.
3. **Streaming Analytics**: Real-time processing with alerts on threshold breaches.
4. **Dashboard**: Visualizes temperature/humidity trends and alerts.

![Architecture Diagram](docs/architecture.png)

---

## 🧱 Tech Stack
- **Python** (data generation, ETL)
- **Pandas / NumPy** (data processing)
- **SQLite / PostgreSQL / Azure Data Lake** (storage)
- **Apache Kafka / Azure Stream Analytics** (real-time streaming)
- **Streamlit / Grafana / Power BI** (dashboard)
- **Azure Data Factory (optional)** for orchestration

---

## 📦 Project Milestones

### Milestone 1: Data Simulation
- `scripts/data_simulator.py` generates random sensor data and stores it in CSV/log file.

### Milestone 2: Batch ETL
- `scripts/batch_etl.py` reads data, performs transformations, and loads it into SQL.

### Milestone 3: Streaming Analytics
- `scripts/streaming_pipeline.py` sets up real-time ingestion and alerting.

### Milestone 4: Dashboard & Reporting
- `dashboard/dashboard_app.py` displays live metrics and alerts.

---

## 📊 Example Output
| Timestamp | Sensor ID | Temperature | Humidity | Alert |
|------------|------------|-------------|----------|--------|
| 2025-10-05 12:00 | sensor_01 | 35.2°C | 65% | ✅ Normal |
| 2025-10-05 12:05 | sensor_02 | 45.8°C | 72% | ⚠️ High Temp |

---

## 🧪 Setup Instructions
```bash
# Clone the repo
git clone https://github.com/<your-username>/real-time-iot-data-pipeline.git

# Navigate to project
cd real-time-iot-data-pipeline

# Install dependencies
pip install -r requirements.txt

# Run simulator
python scripts/data_simulator.py
