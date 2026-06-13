# ==========================================================
# SMART AIR QUALITY MONITORING SYSTEM
# COMPLETE DASHBOARD - PART 1
# ==========================================================

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

from streamlit_autorefresh import st_autorefresh

import os
from datetime import datetime

# Machine Learning
from sklearn.linear_model import LinearRegression

# PDF Report
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet

# ----------------------------------------------------------
# PAGE CONFIG
# ----------------------------------------------------------

st.set_page_config(
    page_title="Smart Air Quality Monitoring",
    page_icon="🌍",
    layout="wide"
)

# ----------------------------------------------------------
# AUTO REFRESH
# ----------------------------------------------------------

st_autorefresh(
    interval=5000,
    key="refresh"
)

# ----------------------------------------------------------
# FILE PATH
# ----------------------------------------------------------

FILE = "data/air_quality.csv"

# ----------------------------------------------------------
# HEADER
# ----------------------------------------------------------

st.markdown(
    """
    <h1 style='text-align:center;'>
    🌍 Smart Air Quality Monitoring Dashboard
    </h1>
    """,
    unsafe_allow_html=True
)

st.markdown("---")

# ==========================================================
# UTILITY FUNCTIONS
# ==========================================================

def classify_aqi(aqi):

    if aqi <= 50:
        return "Good"

    elif aqi <= 100:
        return "Moderate"

    elif aqi <= 200:
        return "Poor"

    else:
        return "Hazardous"


# ----------------------------------------------------------
# HEALTH RECOMMENDATION
# ----------------------------------------------------------

def health_advice(aqi):

    if aqi <= 50:

        return """
        ✅ Safe for outdoor activities.
        ✅ Fresh air conditions.
        """

    elif aqi <= 100:

        return """
        ⚠ Sensitive people should reduce
        prolonged outdoor exposure.
        """

    elif aqi <= 200:

        return """
        😷 Wear masks outdoors.
        🏃 Avoid heavy exercise outside.
        """

    else:

        return """
        🚨 Hazardous Air Quality

        • Stay indoors
        • Use air purifier
        • Wear N95 masks
        """


# ----------------------------------------------------------
# AQI PREDICTION
# ----------------------------------------------------------

def predict_next_aqi(df):

    try:

        if len(df) < 5:
            return None

        data = df.copy()

        data["index"] = np.arange(len(data))

        X = data[["index"]]

        y = data["aqi"]

        model = LinearRegression()

        model.fit(X, y)

        future = [[len(data)]]

        prediction = model.predict(future)

        return round(float(prediction[0]), 2)

    except:
        return None


# ----------------------------------------------------------
# PDF REPORT GENERATION
# ----------------------------------------------------------

def generate_pdf_report(df):

    os.makedirs(
        "reports",
        exist_ok=True
    )

    filename = (
        f"reports/AQI_Report_"
        f"{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    )

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    elements = []

    title = Paragraph(
        "Smart Air Quality Monitoring Report",
        styles["Title"]
    )

    elements.append(title)

    elements.append(
        Spacer(1, 20)
    )

    avg_aqi = round(
        df["aqi"].mean(),
        2
    )

    max_aqi = int(
        df["aqi"].max()
    )

    min_aqi = int(
        df["aqi"].min()
    )

    total_alerts = len(
        df[df["alert"] == "YES"]
    )

    text = f"""
    Average AQI: {avg_aqi}<br/>
    Maximum AQI: {max_aqi}<br/>
    Minimum AQI: {min_aqi}<br/>
    Total Alerts: {total_alerts}<br/>
    Total Records: {len(df)}<br/>
    Generated: {datetime.now()}<br/>
    """

    elements.append(
        Paragraph(
            text,
            styles["BodyText"]
        )
    )

    doc.build(elements)

    return filename


# ----------------------------------------------------------
# DATA LOADER
# ----------------------------------------------------------

def load_data():

    if not os.path.exists(FILE):

        st.error(
            "CSV file not found."
        )

        st.stop()

    try:

        df = pd.read_csv(
            FILE,
            engine="python",
            on_bad_lines="skip"
        )

        return df

    except Exception as e:

        st.error(str(e))

        st.stop()


# ----------------------------------------------------------
# STATUS COLOR
# ----------------------------------------------------------

def get_status_emoji(status):

    if status == "Good":
        return "🟢"

    elif status == "Moderate":
        return "🟡"

    elif status == "Poor":
        return "🟠"

    else:
        return "🔴"


# ----------------------------------------------------------
# LOAD DATA
# ----------------------------------------------------------

df = load_data()

if len(df) == 0:

    st.warning(
        "No data available."
    )

    st.stop()


# ----------------------------------------------------------
# NODE FILTER
# ----------------------------------------------------------

if "node" in df.columns:

    nodes = ["All"] + sorted(
        list(df["node"].unique())
    )

else:

    nodes = ["All"]


selected_node = st.sidebar.selectbox(
    "Select Location",
    nodes
)

if (
    selected_node != "All"
    and "node" in df.columns
):

    df = df[
        df["node"] == selected_node
    ]


# ----------------------------------------------------------
# PAGE NAVIGATION
# ----------------------------------------------------------

page = st.sidebar.selectbox(
    "Navigation",
    [
        "Dashboard",
        "Analytics"
    ]
)

# ----------------------------------------------------------
# LATEST RECORD
# ----------------------------------------------------------

latest = df.iloc[-1]

predicted_aqi = predict_next_aqi(df)

# ==========================================================
# END OF PART 1
# ==========================================================
# ==========================================================
# DASHBOARD PAGE
# ==========================================================

if page == "Dashboard":

    st.title("📡 Live Air Quality Monitoring")

    # ------------------------------------------------------
    # KPI CARDS
    # ------------------------------------------------------

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric(
        "AQI",
        int(latest["aqi"])
    )

    col2.metric(
        "Temperature",
        f"{latest['temperature']} °C"
    )

    col3.metric(
        "Humidity",
        f"{latest['humidity']} %"
    )

    col4.metric(
        "Status",
        latest["status"]
    )

    if predicted_aqi is not None:

        col5.metric(
            "Predicted AQI",
            predicted_aqi
        )

    st.divider()

    # ------------------------------------------------------
    # AQI GAUGE
    # ------------------------------------------------------

    left, right = st.columns([2, 1])

    with left:

        gauge = go.Figure(
            go.Indicator(
                mode="gauge+number",
                value=float(latest["aqi"]),
                title={
                    "text": "Air Quality Index"
                },
                gauge={
                    "axis": {
                        "range": [0, 400]
                    },
                    "steps": [

                        {
                            "range": [0, 50],
                            "color": "lightgreen"
                        },

                        {
                            "range": [50, 100],
                            "color": "yellow"
                        },

                        {
                            "range": [100, 200],
                            "color": "orange"
                        },

                        {
                            "range": [200, 400],
                            "color": "red"
                        }
                    ]
                }
            )
        )

        st.plotly_chart(
            gauge,
            use_container_width=True
        )

    # ------------------------------------------------------
    # STATUS PANEL
    # ------------------------------------------------------

    with right:

        status = str(
            latest["status"]
        )

        emoji = get_status_emoji(
            status
        )

        st.subheader(
            f"{emoji} Air Quality Status"
        )

        st.markdown(
            f"### {status}"
        )

        if status == "Good":

            st.success(
                "Air quality is healthy."
            )

        elif status == "Moderate":

            st.warning(
                "Moderate pollution detected."
            )

        elif status == "Poor":

            st.error(
                "Poor air quality."
            )

        else:

            st.error(
                "Hazardous pollution level!"
            )

        # Forecast

        if predicted_aqi is not None:

            forecast = classify_aqi(
                predicted_aqi
            )

            st.info(
                f"Forecast: {forecast}"
            )

    st.divider()

    # ------------------------------------------------------
    # SMART RECOMMENDATIONS
    # ------------------------------------------------------

    st.subheader(
        "🩺 Health Recommendations"
    )

    st.warning(
        health_advice(
            latest["aqi"]
        )
    )

    st.divider()

    # ------------------------------------------------------
    # AQI TREND
    # ------------------------------------------------------

    st.subheader(
        "📈 AQI Trend"
    )

    fig1 = px.line(
        df,
        x="timestamp",
        y="aqi",
        markers=True,
        title="AQI Over Time"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

    # ------------------------------------------------------
    # TEMPERATURE & HUMIDITY
    # ------------------------------------------------------

    c1, c2 = st.columns(2)

    with c1:

        fig2 = px.line(
            df,
            x="timestamp",
            y="temperature",
            markers=True,
            title="Temperature Trend"
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

    with c2:

        fig3 = px.line(
            df,
            x="timestamp",
            y="humidity",
            markers=True,
            title="Humidity Trend"
        )

        st.plotly_chart(
            fig3,
            use_container_width=True
        )

    st.divider()

    # ------------------------------------------------------
    # POLLUTION DISTRIBUTION
    # ------------------------------------------------------

    st.subheader(
        "🌍 Pollution Distribution"
    )

    status_counts = (
        df["status"]
        .value_counts()
        .reset_index()
    )

    status_counts.columns = [
        "Status",
        "Count"
    ]

    pie = px.pie(
        status_counts,
        names="Status",
        values="Count",
        title="AQI Category Distribution"
    )

    st.plotly_chart(
        pie,
        use_container_width=True
    )

    st.divider()

    # ------------------------------------------------------
    # ALERT SUMMARY
    # ------------------------------------------------------

    st.subheader(
        "🚨 Alert Summary"
    )

    alerts = len(
        df[df["alert"] == "YES"]
    )

    if alerts > 0:

        st.error(
            f"{alerts} pollution alerts recorded."
        )

    else:

        st.success(
            "No alerts recorded."
        )

    st.divider()

    # ------------------------------------------------------
    # DOWNLOAD CSV
    # ------------------------------------------------------

    st.subheader(
        "⬇ Download Dataset"
    )

    with open(
        FILE,
        "rb"
    ) as file:

        st.download_button(
            label="Download CSV",
            data=file,
            file_name="air_quality.csv",
            mime="text/csv"
        )

    st.divider()

    # ------------------------------------------------------
    # PDF REPORT
    # ------------------------------------------------------

    st.subheader(
        "📄 Generate PDF Report"
    )

    if st.button(
        "Create PDF Report"
    ):

        report_file = (
            generate_pdf_report(df)
        )

        with open(
            report_file,
            "rb"
        ) as pdf:

            st.download_button(
                label="Download Report",
                data=pdf,
                file_name=os.path.basename(
                    report_file
                ),
                mime="application/pdf"
            )

    st.divider()

    # ------------------------------------------------------
    # RECENT DATA
    # ------------------------------------------------------

    st.subheader(
        "🗂 Recent Records"
    )

    st.dataframe(
        df.tail(20),
        use_container_width=True
    )

# ==========================================================
# END OF PART 2
# ==========================================================
# ==========================================================
# ANALYTICS PAGE
# ==========================================================

elif page == "Analytics":

    st.title("📊 Air Quality Analytics")

    # ------------------------------------------------------
    # OVERVIEW METRICS
    # ------------------------------------------------------

    avg_aqi = round(df["aqi"].mean(), 2)

    max_aqi = int(df["aqi"].max())

    min_aqi = int(df["aqi"].min())

    total_alerts = len(
        df[df["alert"] == "YES"]
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Average AQI",
        avg_aqi
    )

    col2.metric(
        "Maximum AQI",
        max_aqi
    )

    col3.metric(
        "Minimum AQI",
        min_aqi
    )

    col4.metric(
        "Total Alerts",
        total_alerts
    )

    st.divider()

    # ------------------------------------------------------
    # AQI HISTOGRAM
    # ------------------------------------------------------

    st.subheader(
        "📈 AQI Distribution"
    )

    hist = px.histogram(
        df,
        x="aqi",
        nbins=20,
        title="AQI Histogram"
    )

    st.plotly_chart(
        hist,
        use_container_width=True
    )

    st.divider()

    # ------------------------------------------------------
    # CORRELATION MATRIX
    # ------------------------------------------------------

    st.subheader(
        "🔥 Correlation Heatmap"
    )

    numeric_df = df.select_dtypes(
        include="number"
    )

    if len(numeric_df.columns) > 1:

        corr = numeric_df.corr()

        heatmap = px.imshow(
            corr,
            text_auto=True,
            aspect="auto",
            title="Feature Correlation"
        )

        st.plotly_chart(
            heatmap,
            use_container_width=True
        )

    st.divider()

    # ------------------------------------------------------
    # LOCATION ANALYTICS
    # ------------------------------------------------------

    if "node" in df.columns:

        st.subheader(
            "🏙 Location Comparison"
        )

        location_avg = (
            df.groupby("node")["aqi"]
            .mean()
            .reset_index()
        )

        location_avg["aqi"] = (
            location_avg["aqi"]
            .round(2)
        )

        bar = px.bar(
            location_avg,
            x="node",
            y="aqi",
            title="Average AQI by Location"
        )

        st.plotly_chart(
            bar,
            use_container_width=True
        )

        # --------------------------------------------------
        # MOST POLLUTED AREA
        # --------------------------------------------------

        st.subheader(
            "🚨 Pollution Hotspot"
        )

        hotspot = (
            location_avg
            .sort_values(
                "aqi",
                ascending=False
            )
            .iloc[0]
        )

        st.error(
            f"Highest Pollution Area: "
            f"{hotspot['node']} "
            f"(AQI {round(hotspot['aqi'])})"
        )

        # --------------------------------------------------
        # LOCATION RANKING
        # --------------------------------------------------

        st.subheader(
            "🏆 Location Ranking"
        )

        ranking = (
            location_avg
            .sort_values(
                "aqi",
                ascending=False
            )
        )

        st.dataframe(
            ranking,
            use_container_width=True
        )

    st.divider()

    # ------------------------------------------------------
    # POLLUTION STATUS COUNTS
    # ------------------------------------------------------

    st.subheader(
        "🌍 Pollution Categories"
    )

    good = len(
        df[df["status"] == "Good"]
    )

    moderate = len(
        df[df["status"] == "Moderate"]
    )

    poor = len(
        df[df["status"] == "Poor"]
    )

    hazardous = len(
        df[df["status"] == "Hazardous"]
    )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric("Good", good)

    c2.metric("Moderate", moderate)

    c3.metric("Poor", poor)

    c4.metric("Hazardous", hazardous)

    st.divider()

    # ------------------------------------------------------
    # AQI FORECAST
    # ------------------------------------------------------

    st.subheader(
        "🔮 AQI Forecast"
    )

    if predicted_aqi is not None:

        future_values = []

        current = predicted_aqi

        for i in range(10):

            future_values.append(
                current + (i * 2)
            )

        forecast_df = pd.DataFrame({

            "Future Step":
            list(range(1, 11)),

            "Forecast AQI":
            future_values
        })

        forecast_chart = px.line(
            forecast_df,
            x="Future Step",
            y="Forecast AQI",
            markers=True,
            title="Predicted AQI Trend"
        )

        st.plotly_chart(
            forecast_chart,
            use_container_width=True
        )

    st.divider()

    # ------------------------------------------------------
    # POLLUTION MAP
    # ------------------------------------------------------

    if (
        "lat" in df.columns
        and "lon" in df.columns
    ):

        st.subheader(
            "🗺 Pollution Monitoring Map"
        )

        map_df = (
            df.groupby(
                [
                    "node",
                    "lat",
                    "lon"
                ]
            )["aqi"]
            .mean()
            .reset_index()
        )

        map_df = map_df.rename(
            columns={
                "lat": "latitude",
                "lon": "longitude"
            }
        )

        st.map(
            map_df
        )

    st.divider()

    # ------------------------------------------------------
    # RAW DATASET
    # ------------------------------------------------------

    st.subheader(
        "🗂 Full Dataset"
    )

    st.dataframe(
        df,
        use_container_width=True
    )

# ==========================================================
# FOOTER
# ==========================================================

st.markdown("---")

st.markdown(
    """
    <center>

    🌍 Smart Air Quality Monitoring System

    IoT + AI + Analytics + Dashboard

    </center>
    """,
    unsafe_allow_html=True
)

# ==========================================================
# END OF COMPLETE DASHBOARD
# ==========================================================
# ==========================================================
# SMART CITY MONITORING SECTION
# ==========================================================

st.divider()

st.subheader("🏙 Smart City Monitoring")

# ----------------------------------------------------------
# KPI CARDS
# ----------------------------------------------------------

if "node" in df.columns:

    active_nodes = df["node"].nunique()

else:

    active_nodes = 1

hazardous_events = len(
    df[df["status"] == "Hazardous"]
)

total_alerts = len(
    df[df["alert"] == "YES"]
)

k1, k2, k3 = st.columns(3)

k1.metric(
    "Active Nodes",
    active_nodes
)

k2.metric(
    "Hazardous Events",
    hazardous_events
)

k3.metric(
    "Total Alerts",
    total_alerts
)

# ----------------------------------------------------------
# SENSOR HEALTH
# ----------------------------------------------------------

if "sensor_health" in df.columns:

    st.subheader(
        "🩺 Sensor Health Status"
    )

    health_counts = (
        df["sensor_health"]
        .value_counts()
        .reset_index()
    )

    health_counts.columns = [
        "Health",
        "Count"
    ]

    fig_health = px.bar(
        health_counts,
        x="Health",
        y="Count",
        title="Sensor Health Overview"
    )

    st.plotly_chart(
        fig_health,
        use_container_width=True
    )

# ----------------------------------------------------------
# BATTERY ANALYTICS
# ----------------------------------------------------------

if (
    "battery" in df.columns
    and "node" in df.columns
):

    st.subheader(
        "🔋 Battery Monitoring"
    )

    battery_avg = (
        df.groupby("node")["battery"]
        .mean()
        .reset_index()
    )

    battery_chart = px.bar(
        battery_avg,
        x="node",
        y="battery",
        title="Average Battery Level"
    )

    st.plotly_chart(
        battery_chart,
        use_container_width=True
    )

# ----------------------------------------------------------
# NODE STATUS TABLE
# ----------------------------------------------------------

if (
    "node" in df.columns
    and "battery" in df.columns
    and "sensor_health" in df.columns
):

    st.subheader(
        "📡 Node Status"
    )

    latest_nodes = (
        df.sort_values("timestamp")
        .groupby("node")
        .tail(1)
    )

    node_table = latest_nodes[[
        "node",
        "aqi",
        "status",
        "battery",
        "sensor_health"
    ]]

    st.dataframe(
        node_table,
        use_container_width=True
    )

# ----------------------------------------------------------
# ALERT TREND
# ----------------------------------------------------------

st.subheader(
    "🚨 Alert Trend"
)

alert_data = df.copy()

alert_data["alert_flag"] = (
    alert_data["alert"]
    .apply(
        lambda x: 1
        if x == "YES"
        else 0
    )
)

alert_chart = px.line(
    alert_data,
    x="timestamp",
    y="alert_flag",
    title="Alert Activity Over Time"
)

st.plotly_chart(
    alert_chart,
    use_container_width=True
)

# ----------------------------------------------------------
# AQI VS TEMPERATURE
# ----------------------------------------------------------

st.subheader(
    "🌡 AQI vs Temperature"
)

scatter = px.scatter(
    df,
    x="temperature",
    y="aqi",
    color="status",
    title="AQI vs Temperature Analysis"
)

st.plotly_chart(
    scatter,
    use_container_width=True
)

# ----------------------------------------------------------
# AQI VS HUMIDITY
# ----------------------------------------------------------

st.subheader(
    "💧 AQI vs Humidity"
)

scatter2 = px.scatter(
    df,
    x="humidity",
    y="aqi",
    color="status",
    title="AQI vs Humidity Analysis"
)

st.plotly_chart(
    scatter2,
    use_container_width=True
)

# ==========================================================
# END OF PHASE 4 ADDITIONS
# ==========================================================
# ==========================================================
# DEVICE CONNECTIVITY
# ==========================================================

st.divider()

st.subheader("📶 Device Connectivity")

if "node" in df.columns:

    latest_devices = (
        df.sort_values("timestamp")
        .groupby("node")
        .tail(1)
    )

    latest_devices["connection"] = "Online"

    connectivity = latest_devices[
        ["node", "connection"]
    ]

    st.dataframe(
        connectivity,
        use_container_width=True
    )
# ==========================================================
# AQI LEADERBOARD
# ==========================================================

st.subheader("🏆 AQI Leaderboard")

if "node" in df.columns:

    ranking = (
        df.groupby("node")["aqi"]
        .mean()
        .reset_index()
    )

    ranking = ranking.sort_values(
        "aqi",
        ascending=False
    )

    ranking.columns = [
        "Location",
        "Average AQI"
    ]

    st.dataframe(
        ranking,
        use_container_width=True
    )
# ==========================================================
# RISK SCORE
# ==========================================================

st.subheader("⚠ Environmental Risk Score")

avg_aqi = df["aqi"].mean()

risk_score = min(
    round(avg_aqi / 3, 2),
    100
)

st.progress(
    int(risk_score)
)

st.metric(
    "Risk Score",
    f"{risk_score}/100"
)
# ==========================================================
# LIVE SENSOR FEED
# ==========================================================

st.subheader("📡 Live Sensor Feed")

latest_records = (
    df.sort_values("timestamp")
    .tail(10)
)

st.dataframe(
    latest_records,
    use_container_width=True
)
# ==========================================================
# DATA QUALITY
# ==========================================================

st.subheader("🧪 Data Quality Monitor")

missing_values = df.isnull().sum().sum()

total_records = len(df)

quality = round(
    (
        1 -
        (missing_values /
         max(total_records,1))
    ) * 100,
    2
)

st.metric(
    "Data Quality",
    f"{quality}%"
)
# ==========================================================
# NODE PERFORMANCE
# ==========================================================

if (
    "battery" in df.columns
    and "node" in df.columns
):

    st.subheader(
        "⚙ Node Performance"
    )

    performance = (
        df.groupby("node")["battery"]
        .mean()
        .reset_index()
    )

    fig_perf = px.bar(
        performance,
        x="node",
        y="battery",
        title="Node Performance Score"
    )

    st.plotly_chart(
        fig_perf,
        use_container_width=True
    )
# ==========================================================
# COMMAND CENTER
# ==========================================================

st.subheader("🏙 Smart City Command Center")

critical_nodes = len(
    df[df["status"] == "Hazardous"]
)

poor_nodes = len(
    df[df["status"] == "Poor"]
)

good_nodes = len(
    df[df["status"] == "Good"]
)

c1,c2,c3 = st.columns(3)

c1.metric(
    "Critical Zones",
    critical_nodes
)

c2.metric(
    "Moderate Risk",
    poor_nodes
)

c3.metric(
    "Healthy Zones",
    good_nodes
)
# ==========================================================
# AQI HEAT RANKING
# ==========================================================

if "node" in df.columns:

    st.subheader(
        "🔥 Pollution Heat Ranking"
    )

    heat = (
        df.groupby("node")["aqi"]
        .mean()
        .reset_index()
    )

    heat = heat.sort_values(
        "aqi",
        ascending=False
    )

    heat_chart = px.bar(
        heat,
        x="node",
        y="aqi",
        title="Pollution Ranking"
    )

    st.plotly_chart(
        heat_chart,
        use_container_width=True
    )
# ==========================================================
# SMART CITY RECOMMENDATION
# ==========================================================

st.subheader("🤖 AI Recommendations")

current_aqi = latest["aqi"]

if current_aqi <= 50:

    st.success(
        "Air quality is excellent."
    )

elif current_aqi <= 100:

    st.warning(
        "Monitor AQI periodically."
    )

elif current_aqi <= 200:

    st.warning(
        "Wear masks outdoors."
    )

else:

    st.error(
        "Immediate action required. Hazardous pollution detected."
    )
st.markdown("---")

st.markdown(
"""
### 🌍 AI-Powered Smart Air Quality Monitoring System

Features:
- Multi-Node Monitoring
- AQI Prediction
- Smart Alerts
- Analytics
- Environmental Intelligence
- Smart City Dashboard
"""
)