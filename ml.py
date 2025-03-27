import streamlit as st
import numpy as np
import joblib

# 🌟 Load the trained Random Forest model
with open("my_model.pkl", "rb") as model_file:
    model = joblib.load(model_file)

# 🎨 Streamlit UI
st.title("🌤️ Next-Day Temperature Prediction App")
st.markdown("#### Enter the weather features and get AI-powered temperature forecasts!")

# 📌 User Input Fields
Present_Tmax = st.number_input("🌡️ Present Maximum Temperature (°C)", min_value=15.0, max_value=40.0, value=30.0)
Present_Tmin = st.number_input("🌡️ Present Minimum Temperature (°C)", min_value=5.0, max_value=30.0, value=20.0)
LDAPS_RHmin = st.number_input("💧 LDAPS Min Relative Humidity (%)", min_value=10.0, max_value=100.0, value=30.0)
LDAPS_RHmax = st.number_input("💧 LDAPS Max Relative Humidity (%)", min_value=20.0, max_value=100.0, value=80.0)
LDAPS_Tmax_lapse = st.number_input("🌡️ LDAPS Forecast Max Temp (°C)", min_value=10.0, max_value=40.0, value=32.0)
LDAPS_Tmin_lapse = st.number_input("🌡️ LDAPS Forecast Min Temp (°C)", min_value=5.0, max_value=30.0, value=22.0)
LDAPS_WS = st.number_input("🌬️ LDAPS Wind Speed (m/s)", min_value=0.0, max_value=30.0, value=5.0)
LDAPS_CC1 = st.number_input("☁️ Cloud Cover (0-5h) (%)", min_value=0.0, max_value=1.0, value=0.5)
LDAPS_CC2 = st.number_input("☁️ Cloud Cover (6-11h) (%)", min_value=0.0, max_value=1.0, value=0.5)
LDAPS_CC3 = st.number_input("☁️ Cloud Cover (12-17h) (%)", min_value=0.0, max_value=1.0, value=0.5)
LDAPS_CC4 = st.number_input("☁️ Cloud Cover (18-23h) (%)", min_value=0.0, max_value=1.0, value=0.5)
LDAPS_PPT3 = st.number_input("🌧️ Precipitation (12-17h) (%)", min_value=0.0, max_value=30.0, value=5.0)
LDAPS_PPT4 = st.number_input("🌧️ Precipitation (18-23h) (%)", min_value=0.0, max_value=30.0, value=5.0)
avg_cc = st.number_input("☁️ Average Cloud Cover (%)", min_value=0.0, max_value=1.0, value=0.5)
avg_ppt = st.number_input("🌧️ Average Precipitation (%)", min_value=0.0, max_value=30.0, value=5.0)

# 📌 Convert User Input to NumPy Array
user_input = np.array([[Present_Tmax, Present_Tmin, LDAPS_RHmin, LDAPS_RHmax, LDAPS_Tmax_lapse, 
                        LDAPS_Tmin_lapse, LDAPS_WS, LDAPS_CC1, LDAPS_CC2, LDAPS_CC3, LDAPS_CC4, 
                        LDAPS_PPT3, LDAPS_PPT4, avg_cc, avg_ppt]])

# 🎯 Predict Temperature
if st.button("🔮 Predict Next-Day Maximum Temperature"):
    prediction = model.predict(user_input)
    st.success(f"🌡️ Predicted Next-Day Maximum Temperature: **{prediction[0]:.2f}°C**")

# 🏁 Run the Streamlit App
# To run, use: `streamlit run app.py`
