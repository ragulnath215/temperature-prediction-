import streamlit as st
import numpy as np
import joblib

# 🌟 Load the trained Random Forest model
with open("my_model.pkl", "rb") as model_file:
    model = joblib.load(model_file)

# 🎨 Streamlit UI
st.title("🌤️ Next-Day Temperature Prediction App")
st.markdown("#### Enter the weather features and get AI-powered temperature forecasts! SUI")

# 📌 User Input Fields
Present_Tmax = st.number_input("🌡️ Present Maximum Temperature (°C)", min_value=15.0, max_value=40.0, value=30.0)
Present_Tmin = st.number_input("🌡️ Present Minimum Temperature (°C)", min_value=5.0, max_value=30.0, value=20.0)
LDAPS_Tmax_lapse = st.number_input("🌡️ LDAPS Forecast Max Temp (°C)", min_value=10.0, max_value=40.0, value=32.0)
LDAPS_Tmin_lapse = st.number_input("🌡️ LDAPS Forecast Min Temp (°C)", min_value=5.0, max_value=30.0, value=22.0)
LDAPS_CC2 = st.number_input("☁️ Cloud Cover (6-11h) (%)", min_value=0.0, max_value=1.0, value=0.5)
LDAPS_CC3 = st.number_input("☁️ Cloud Cover (12-17h) (%)", min_value=0.0, max_value=1.0, value=0.5)
avg_cc = st.number_input("☁️ Average Cloud Cover (%)", min_value=0.0, max_value=1.0, value=0.5)

# 📌 Convert User Input to NumPy Array
user_input = np.array([[Present_Tmax, Present_Tmin, LDAPS_Tmax_lapse, 
                        LDAPS_Tmin_lapse, LDAPS_CC2, LDAPS_CC3, 
                         avg_cc]])

# 🎯 Predict Temperature
if st.button("🔮 Predict Next-Day Maximum Temperature"):
    prediction = model.predict(user_input)
    st.success(f"🌡️ Predicted Next-Day Maximum Temperature: **{prediction[0]:.2f}°C**")

# 🏁 Run the Streamlit App
# To run, use: `streamlit run app.py`
