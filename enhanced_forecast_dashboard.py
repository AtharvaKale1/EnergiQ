# interactive_forecast_dashboard.py

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.metrics import mean_squared_error

# Configure page
st.set_page_config("📈 Energy Forecasting Studio", layout="wide")
st.markdown("<h1 style='text-align: center;'>📊 Energy Time Series Forecasting Studio</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Upload data, adjust model parameters, and forecast with interactive ARIMA/SARIMA models</p>", unsafe_allow_html=True)

# Sidebar configuration
with st.sidebar:
    st.header("🔧 Forecast Settings")
    model_type = st.selectbox("Choose Model", ["ARIMA", "SARIMA"])
    forecast_horizon = st.slider("Forecast Months", 6, 36, 12)

    st.markdown("📉 Model Hyperparameters")

    p = st.slider("AR term (p)", 0, 10, 2)
    d = st.slider("Differencing order (d)", 0, 2, 1)
    q = st.slider("MA term (q)", 0, 10, 2)

    seasonal_p = st.slider("Seasonal AR (P)", 0, 2, 1)
    seasonal_d = st.slider("Seasonal D", 0, 2, 1)
    seasonal_q = st.slider("Seasonal MA (Q)", 0, 2, 1)
    seasonal_period = st.slider("Seasonal Period", 6, 24, 12)

    st.markdown("---")
    st.markdown("👨‍💻 Built by:")
    st.markdown("- Atharva Kale")
    st.markdown("- Harsh Kubade")
    st.markdown("- Aditya Jain")

uploaded_file = st.file_uploader("📤 Upload a CSV with 'Date' and 'Value' columns", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    df.columns = [col.strip().lower() for col in df.columns]

    if "date" not in df.columns or "value" not in df.columns:
        st.error("❌ File must have 'Date' and 'Value' columns.")
    else:
        df['date'] = pd.to_datetime(df['date'])
        df = df.sort_values('date')
        df.set_index('date', inplace=True)

        train = df.iloc[:-forecast_horizon]
        test = df.iloc[-forecast_horizon:]

        tab1, tab2, tab3 = st.tabs(["📊 Visualize Data", "📈 Run Forecast", "📥 Download"])

        with tab1:
            st.subheader("📊 Time Series Overview")
            fig = px.line(df, y='value', title="Time Series Data", labels={'value': 'Value'})
            st.plotly_chart(fig, use_container_width=True)

        with tab2:
            st.subheader(f"🧠 Forecast using {model_type}")

            if st.button("🚀 Generate Forecast"):
                try:
                    if model_type == "ARIMA":
                        model = ARIMA(train, order=(p, d, q))
                        fit = model.fit()
                        forecast = fit.forecast(steps=forecast_horizon)
                    else:
                        model = SARIMAX(train,
                                        order=(p, d, q),
                                        seasonal_order=(seasonal_p, seasonal_d, seasonal_q, seasonal_period))
                        fit = model.fit()
                        forecast = fit.forecast(steps=forecast_horizon)

                    forecast_df = pd.DataFrame({'Forecast': forecast}, index=test.index)
                    combined = pd.concat([test, forecast_df], axis=1)
                    combined.columns = ['Actual', 'Forecast']

                    st.success("✅ Forecast complete!")

                    fig2 = px.line(combined, title="📉 Actual vs Forecast", labels={"value": "Value"})
                    fig2.add_scatter(x=forecast_df.index, y=forecast_df.Forecast, mode='lines', name="Forecast")
                    st.plotly_chart(fig2, use_container_width=True)

                    mse = mean_squared_error(test, forecast)
                    st.metric("📐 Mean Squared Error (MSE)", f"{mse:.2f}")

                    st.session_state["forecast_df"] = forecast_df

                except Exception as e:
                    st.error(f"⚠️ Forecast failed: {e}")

        with tab3:
            if "forecast_df" in st.session_state:
                csv = st.session_state["forecast_df"].to_csv().encode()
                st.download_button("📥 Download Forecast CSV", data=csv, file_name="forecast.csv", mime="text/csv")
            else:
                st.info("🔔 Run a forecast first to enable download.")
