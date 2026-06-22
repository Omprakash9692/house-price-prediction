import streamlit as st
import joblib
import pandas as pd

# Page Config
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="wide",
)

# Load Model
model = joblib.load("house_price_model.pkl")

# Sidebar
st.sidebar.title("🏠 About Project")
st.sidebar.info(
    """House Price Prediction using Machine Learning

Model: Linear Regression
Dataset: 50,000 Houses
R² Score: 0.9968

Developed by Omprakash"""
)

# Header
st.title("🏠 AI House Price Prediction System")
st.markdown("Enter the property details below to estimate the house price.")

st.divider()

# Two Columns
col1, col2 = st.columns(2)

with col1:
    st.subheader("🏠 Property Details")

    area = st.number_input(
        "Area (sq ft)",
        min_value=500,
        max_value=5000,
        value=2500,
    )

    bedrooms = st.number_input(
        "Bedrooms",
        min_value=1,
        max_value=10,
        value=3,
    )

    bathrooms = st.number_input(
        "Bathrooms",
        min_value=1,
        max_value=10,
        value=2,
    )

    floors = st.number_input(
        "Floors",
        min_value=1,
        max_value=5,
        value=2,
    )

    age = st.number_input(
        "Age",
        min_value=0,
        max_value=100,
        value=10,
    )

    distance = st.number_input(
        "Distance from City Center",
        value=10,
    )

with col2:
    st.subheader("📍 Location & Amenities")

    location = st.selectbox("Location", ["low", "medium", "premium"])
    income_level = st.selectbox("Income Level", ["high", "low", "mid"])

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

# Correct Encoding
location_map = {"low": 0, "medium": 1, "premium": 2}
income_map = {"high": 0, "low": 1, "mid": 2}

st.divider()

if st.button("🔮 Predict House Price", use_container_width=True):
    input_data = pd.DataFrame(
        {
            "area": [area],
            "bedrooms": [bedrooms],
            "bathrooms": [bathrooms],
            "floors": [floors],
            "age": [age],
            "distance": [distance],
            "garage": [garage],
            "parking": [parking],
            "garden": [garden],
            "security": [security],
            "school_nearby": [school_nearby],
            "hospital_nearby": [hospital_nearby],
            "shopping_mall_nearby": [shopping_mall_nearby],
            "public_transport": [public_transport],
            "crime_rate": [crime_rate],
            "population_density": [population_density],
            "location": [location_map[location]],
            "income_level": [income_map[income_level]],
        }
    )

    prediction = model.predict(input_data)

    st.success(f"💰 Estimated House Price: ₹ {prediction[0]:,.2f}")
    st.metric(label="Predicted Price", value=f"₹ {prediction[0]:,.0f}")
    st.balloons()

st.divider()

st.markdown(
    """
### 📊 Project Information

This application predicts house prices using a Machine Learning Linear Regression model trained on a housing dataset with 50,000 records.

Features used:

* Area
* Bedrooms
* Bathrooms
* Floors
* Age
* Location
* Amenities
* Crime Rate
* Population Density
"""
)

