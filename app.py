import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("house_price_model.pkl")

st.title("🏠 House Price Prediction")

area = st.number_input("Area", min_value=500, max_value=5000, value=2500)
bedrooms = st.number_input("Bedrooms", min_value=1, max_value=10, value=3)
bathrooms = st.number_input("Bathrooms", min_value=1, max_value=10, value=2)
floors = st.number_input("Floors", min_value=1, max_value=5, value=2)
age = st.number_input("Age", min_value=0, max_value=100, value=10)

distance = st.number_input("Distance", value=10)

garage = st.selectbox("Garage", [0, 1])
parking = st.selectbox("Parking", [0, 1])
garden = st.selectbox("Garden", [0, 1])
security = st.selectbox("Security", [0, 1])

school_nearby = st.selectbox("School Nearby", [0, 1])
hospital_nearby = st.selectbox("Hospital Nearby", [0, 1])
shopping_mall_nearby = st.selectbox("Shopping Mall Nearby", [0, 1])
public_transport = st.selectbox("Public Transport", [0, 1])

crime_rate = st.number_input("Crime Rate", value=5.0)
population_density = st.number_input("Population Density", value=5000)

location = st.selectbox("Location", ["low", "medium", "premium"])
income_level = st.selectbox("Income Level", ["high", "low", "mid"])

location_map = {
    "low": 0,
    "medium": 1,
    "premium": 2
}

income_map = {
    "low": 0,
    "mid": 1,
    "high": 2
}

if st.button("Predict Price"):

    data = pd.DataFrame({
        "area":[area],
        "bedrooms":[bedrooms],
        "bathrooms":[bathrooms],
        "floors":[floors],
        "age":[age],
        "distance":[distance],
        "garage":[garage],
        "parking":[parking],
        "garden":[garden],
        "security":[security],
        "school_nearby":[school_nearby],
        "hospital_nearby":[hospital_nearby],
        "shopping_mall_nearby":[shopping_mall_nearby],
        "public_transport":[public_transport],
        "crime_rate":[crime_rate],
        "population_density":[population_density],
        "location":[location_map[location]],
        "income_level":[income_map[income_level]]
    })

    prediction = model.predict(data)

    st.success(f"Predicted Price: ₹ {prediction[0]:,.2f}")