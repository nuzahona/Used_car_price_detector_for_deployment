import streamlit as st 
import pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler
import time

with open('model_pickle', "rb") as f:
    mp = pickle.load(f)
    
with open('scaler_pickle', "rb") as f:
    scala = pickle.load(f)
    
st.title("Used CaR Price Detector")

# Create individual input boxes for each feature
engine = st.number_input("Engine (CC)", value=0.0)
max_power = st.number_input("Max Power (bhp)", value=0.0)
mileage = st.number_input("Mileage (km/l)", value=23.4, step=10.0)
seats = st.number_input("Seats", value=5, step=1)
transmission = st.radio("Transmission Type (0 = Manual, 1 = Automatic)", [0, 1])

# Fuel Type - Select One
fuel_type = st.radio("Select Fuel Type", ["CNG", "Diesel", "LPG", "Petrol"])
fuel_CNG = 1 if fuel_type == "CNG" else 0
fuel_Diesel = 1 if fuel_type == "Diesel" else 0
fuel_LPG = 1 if fuel_type == "LPG" else 0
fuel_Petrol = 1 if fuel_type == "Petrol" else 0

# Seller Type - Select One
seller_type = st.radio("Select Seller Type", ["Dealer", "Individual", "Trustmark Dealer"])
seller_type_Dealer = 1 if seller_type == "Dealer" else 0
seller_type_Individual = 1 if seller_type == "Individual" else 0
seller_type_Trustmark_Dealer = 1 if seller_type == "Trustmark Dealer" else 0

owner_type = st.radio("Select Owner Type", ["owner_First_Owner", "owner_Second_Owner", "owner_Third_Owner", "owner_Fourth_Above_Owner", "owner_Test_Drive_Car"])
owner_First_Owner = 1 if seller_type == "owner_First_Owner" else 0
owner_Second_Owner = 1 if seller_type == "owner_Second_Owner" else 0
owner_Third_Owner = 1 if seller_type == "owner_Third_Owner" else 0
owner_Fourth_Above_Owner = 1 if seller_type == "owner_Fourth_Above_Owner" else 0
owner_Test_Drive_Car = 1 if seller_type == "owner_Test_Drive_Car" else 0




# Other features
year = st.number_input("Year of Manufacture", value=2002, step=1)
km_driven = st.number_input("Kilometers Driven", value=1500000, step=1000)

# Manually create the dictionary for user inputs
predict_car = {
    'engine': engine,
    'max_power': max_power,
    'selling_price': 0,  # Not used in prediction
    'mileage': mileage,
    'seats': seats,
    'fuel_CNG': fuel_CNG,
    'fuel_Diesel': fuel_Diesel,
    'fuel_LPG': fuel_LPG,
    'fuel_Petrol': fuel_Petrol,
    'seller_type_Dealer': seller_type_Dealer,
    'seller_type_Individual': seller_type_Individual,
    'seller_type_Trustmark Dealer': seller_type_Trustmark_Dealer,
    'owner_First Owner': owner_First_Owner,
    'owner_Fourth & Above Owner': owner_Fourth_Above_Owner,
    'owner_Second Owner': owner_Second_Owner,
    'owner_Test Drive Car': owner_Test_Drive_Car,
    'owner_Third Owner': owner_Third_Owner,
    'transmission': transmission,
    'year': year,
    'km_driven': km_driven
}

# Save input dictionary to a pickle file
if st.button("Send to Model"):
    with open("input.pkl", "wb") as file:
        pickle.dump(predict_car, file)
    st.success("Wait")

    # Wait for the result
    time.sleep(3)

    # Load the output
    try:
        with open("output.pkl", "rb") as file:
            prediction = pickle.load(file)
            st.success(f"Predicted Car Price Category: {prediction}")
    except FileNotFoundError:
        st.error("Prediction file not found. Please check if `app.ipynb` ran correctly.")