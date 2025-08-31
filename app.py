import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Insurance Charges Prediction 💰")
st.write("Predict insurance charges based on your details.")

# Input fields
age = st.number_input("Age", min_value=0, max_value=120, value=30)
bmi = st.number_input("BMI", min_value=0.0, max_value=60.0, value=25.0)
children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)
smoker = st.selectbox("Smoker", ["Yes", "No"])
region = st.selectbox("Region", ["southwest", "southeast", "northwest", "northeast"])

# Encode categorical variables
smoker_mapping = {"Yes": 1, "No": 0}
region_mapping = {"southwest":0, "southeast":1, "northwest":2, "northeast":3}

smoker_encoded = smoker_mapping[smoker]
region_encoded = region_mapping[region]

# Prediction
if st.button("Predict"):
    features = np.array([[age, bmi, children, smoker_encoded, region_encoded]])
    prediction = model.predict(features)
    st.success(f"Predicted Insurance Charges: ${prediction[0]:.2f}")
