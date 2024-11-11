import pandas as pd
import numpy as np
import streamlit as st
import pickle

# Title
st.title("Cars24 Used Car Price Prediction")

# Create two columns
col1, col2 = st.columns(2)

# First column inputs
with col1:
    fuel_type = st.selectbox( "Select fuel type",["Diesel", "Petrol", "Electric", "LPG"])

    engine = st.slider("Set the engine power",500, 5000, step=100)

    mileage = st.number_input("Enter mileage (kmpl)",min_value=0.0,max_value=50.0,value=20.0)

# Second column inputs
with col2:
    transmission = st.selectbox("Select transmission type",["Manual", "Automatic"])

    seats = st.selectbox("Enter the Number of Seats",["5", ">5"])

    max_power = st.number_input("Enter max power (bhp)",min_value=0.0,max_value=200.0,value=100.0)

def predict_price():
    try:
        # Load model
        with open('car_pred.pkl', 'rb') as file:
            model = pickle.load(file)

        # Prepare input features
        features = {
            'year': 2020.0,
            'km_driven': 50000,
            'mileage': mileage,
            'engine': engine,
            'max_power': max_power,
            'Diesel': 1 if fuel_type == "Diesel" else 0,
            'Electric': 1 if fuel_type == "Electric" else 0,
            'LPG': 1 if fuel_type == "LPG" else 0,
            'Petrol': 1 if fuel_type == "Petrol" else 0,
            'Manual': 1 if transmission == "Manual" else 0,
            '5': 1 if seats == "5" else 0,
            '>5': 1 if seats == ">5" else 0
        }

        input_df = pd.DataFrame([features])
        prediction = model.predict(input_df)
        return prediction[0]

    except Exception as e:
        return f"Error: {str(e)}"

if st.button("Predict Price"):
    price = predict_price()
    if isinstance(price, str):
        st.error(price)
    else:
        st.success(f"Predicted Price: ₹{price:.2f} Lakhs")