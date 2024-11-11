import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

# Load data
df = pd.read_csv('cars24-car-price-cleaned.csv')

# Prepare features based on your actual columns
X = df[[
    'year',
    'km_driven',
    'mileage',
    'engine',
    'max_power',
    'Diesel',
    'Electric',
    'LPG',
    'Petrol',
    'Manual',
    '5',
    '>5'
]]
y = df['selling_price']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
with open('car_pred.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Model trained and saved as car_pred.pkl")