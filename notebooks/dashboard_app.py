import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import time

# Load your sensor data
df = pd.read_csv(r"C:\Users\hannah\Downloads\sensor_data_depi.csv")
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Dashboard layout
st.set_page_config(page_title="IoT Sensor Dashboard", layout="wide")
st.title("🌡️ Real-Time IoT Sensor Monitoring Dashboard")

# Sidebar filters
st.sidebar.header("Filters")
selected_device = st.sidebar.selectbox("Select Device", df['device_id'].unique())
time_range = st.sidebar.selectbox("Time Range", ["Last Hour", "Last 6 Hours", "Last 24 Hours", "All Data"])

# KPI Metrics
col1, col2, col3, col4 = st.columns(4)

with col1:
    current_temp = df[df['device_id'] == selected_device]['temperature'].iloc[-1]
    st.metric("Current Temperature", f"{current_temp:.1f}°C")

with col2:
    current_humidity = df[df['device_id'] == selected_device]['humidity'].iloc[-1]
    st.metric("Current Humidity", f"{current_humidity:.1f}%")

with col3:
    avg_temp = df[df['device_id'] == selected_device]['temperature'].mean()
    st.metric("Average Temperature", f"{avg_temp:.1f}°C")

with col4:
    alerts = len(df[(df['temperature'] > 35) | (df['humidity'] > 70)])
    st.metric("Total Alerts", alerts)

# Charts
col1, col2 = st.columns(2)

with col1:
    st.subheader("Temperature Trend")
    fig_temp = px.line(df[df['device_id'] == selected_device], 
                      x='timestamp', y='temperature',
                      title=f"Temperature for {selected_device}")
    st.plotly_chart(fig_temp, use_container_width=True)

with col2:
    st.subheader("Humidity Trend")
    fig_humidity = px.line(df[df['device_id'] == selected_device], 
                          x='timestamp', y='humidity',
                          title=f"Humidity for {selected_device}")
    st.plotly_chart(fig_humidity, use_container_width=True)

# Alerts Section
st.subheader("🚨 Alert History")
alerts_df = df[(df['temperature'] > 35) | (df['humidity'] > 70)]
if not alerts_df.empty:
    st.dataframe(alerts_df[['timestamp', 'device_id', 'temperature', 'humidity']])
else:
    st.info("No alerts detected in the current data range")

# Device Comparison
st.subheader("Device Performance Comparison")
col1, col2 = st.columns(2)

with col1:
    fig_box_temp = px.box(df, x='device_id', y='temperature', 
                         title="Temperature Distribution by Device")
    st.plotly_chart(fig_box_temp, use_container_width=True)

with col2:
    fig_box_humidity = px.box(df, x='device_id', y='humidity', 
                             title="Humidity Distribution by Device")
    st.plotly_chart(fig_box_humidity, use_container_width=True)