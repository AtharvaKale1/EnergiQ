## ⚡ Enhanced EnergiQ 🔋🔮

**AI-Powered Energy Demand Forecasting Using Time Series Modeling**

---

### 📌 Overview

**Enhanced Energy Forecast** is a machine learning-based project that intelligently predicts future energy consumption using historical load data. By integrating powerful time-series forecasting techniques like ARIMA and SARIMA, this solution empowers industries, grid operators, and policymakers to optimize energy usage, reduce costs, and support sustainable planning.

---

### 🚀 Features

* 🔢 **Multistep Energy Forecasting**
* 🧠 **SARIMA & ARIMA Models for Seasonal Analysis**
* 📈 **Trend & Residual Visualization**
* 🧪 **ACF, PACF, Dickey-Fuller, and KPSS Tests**
* 💡 **Optimized Model Selection via AIC/BIC**
* 🗂️ **CSV Input & Output Ready**
* 🌱 **Scalable for Smart Grids & Renewable Planning**
* 🌐 **Interactive Streamlit Web App Interface**

---

### 📂 Project Structure

```
├── Enhanced_Energy_Forecast.ipynb   # Jupyter notebook with full implementation
├── forecast_sample_input.csv        # Sample input data (Time vs Load)
├── app.py                           # Streamlit app script
└── README.md                        # Project description & guide
```

---

### 🛠️ Tech Stack

* **Python** 🐍
* **Libraries:** `pandas`, `numpy`, `matplotlib`, `statsmodels`, `seaborn`, `streamlit`
* **Models:** ARIMA, SARIMA
* **Visualization:** Time Series Plots, ACF/PACF, Seasonal Decomposition
* **UI:** Streamlit-based Interactive Forecast Interface

---

### 📊 Sample Forecast Flow

1. ✅ Load and clean the dataset
2. 📉 Visualize trends and seasonality
3. ☑️ Conduct stationarity tests (ADF & KPSS)
4. 🧰 Tune model parameters using AIC/BIC
5. 🔮 Generate and plot forecasts
6. 📝 Export predictions to CSV
7. 🌐 Visualize results on Streamlit App

---

### 🖼️ Visual Insights

* Seasonal Decomposition of Time Series
* Forecast vs Actual Comparison Plot
* Residual Analysis for Error Distribution
* Streamlit Dashboard with Forecast Sliders & Results

---

### 🧪 Sample Input Format (`forecast_sample_input.csv`)

| Date       | Load   |
| ---------- | ------ |
| 2022-01-01 | 3456.2 |
| 2022-01-02 | 3542.1 |
| ...        | ...    |

> Input must be time-indexed, continuous, and ideally daily/monthly aggregated.

---

### 📤 Output

Forecasts are generated and saved with future date indices, ready for use in dashboards or reports. Results are also visualized in an interactive **Streamlit web app**.

![image](https://github.com/user-attachments/assets/a57b30b2-1a66-451c-96a5-7ead3598db0f)

![image](https://github.com/user-attachments/assets/5e34e5d3-a6e0-45ba-9ec4-26c260931edc)

![image](https://github.com/user-attachments/assets/333a6a75-d93a-4b25-891e-cfdd98877380)

![image](https://github.com/user-attachments/assets/40690736-01ef-4080-bd2d-c15c16da737c)

## StreamLit InterFace

![image](https://github.com/user-attachments/assets/06f7c09f-7347-4c59-80cc-7b55998b17c0)

---

### ✅ Use Cases

* ⚡ Smart Grid Load Management
* 🏭 Industrial Demand Forecasting
* 🏠 Energy Monitoring for Smart Homes
* 🌍 Renewable Integration Planning

---

### 📌 Future Improvements

* Integrate Prophet or LSTM for deep learning-based forecasting
* Enhance Streamlit UI with custom plots and export options
* REST API for energy forecast on demand

---

### 🙌 Contributors

Made with 💡 by **Atharva Kale**

---

### 📃 License

This project is open-source and free to use under the **MIT License**.
