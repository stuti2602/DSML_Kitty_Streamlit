import pandas as pd
import numpy as np
import streamlit as st
import datetime
import pickle

# while copy a path chang "\" to "/" otherwise it will give you and runtime error.
cars_df = pd.read_csv('cars24-car-price-cleaned.csv.csv')
st.write(
    """
    # cars 24 used car price prediction
    """
)
st.dataframe(cars_df.head())


# Encoding categorical features

encoded_dict = {
    "fuel_type": {"Diesel" : 1, "Petrol" : 2, "CNG": 3, "LPG" : 4, "Electric" : 5 },
    "Seller_type" : {"Dealer": 1, "Individual": 2, "Trustmark Dealer": 3},
    "transmission_type": {"Manual": 1, "Automatic" : 2}
}


col1, col2 = st.columns(2)

fuel_type = col1.selectbox("Select fuel type",
                            ["Diesel", "Petrol", "CNG", "LPG", "Electric"])


engine = col1.slider("Set the engine power",
                        500, 5000, step=100)

transmission_type = col2.selectbox("Select transmission type",
                                    ['Manual', "Automatic"])

seats = col2.selectbox("Enter the Number of Seats",
                        [4,5,7,9,11])


# if have button over there then the taking input will encoded to output

def model_prep(encoded_fuel_type,encoded_transmission_type,engine,seats):
    with open("C:/Data/Study/Scaler_study_material/10_Intro_to_ML_and_NN/LEC_142_ML_Linear_Regression-1/cars24-car-price-cleaned.csv","rb") as file :
        loaded_model = pickle.load(file)

        input_features = [[2012.0,2,120000,encoded_fuel_type,encoded_transmission_type,19.7,engine,46.3,seats]]
        return loaded_model.predict(input_features)

if st.button("Predict_price"):
    encoded_fuel_type = encoded_dict["fuel_type"][fuel_type]
    encoded_transmission_type = encoded_dict["transmission_type"][transmission_type]

    price = model_prep(encoded_fuel_type,encoded_transmission_type,engine,seats)

    st.header("Predicted Price is : " + str(price))

