import streamlit as st
import pickle
import pandas as pd
import numpy as np

def prediction(name,company,year,kms_driven,fuel_type):
    predicting = model.predict(pd.DataFrame([[name,company,year,kms_driven,fuel_type]], columns=['name','company','year','kms_driven','fuel_type']))
    return str(np.round(predicting[0],2))



car_dict = pickle.load(open('car_dict.pkl','rb'))
model = pickle.load(open('LinearRegressionModel.pkl','rb'))

car_df = pd.DataFrame(car_dict)
st.title('Car Price Predictor')

name = st.selectbox("Model:", car_df['name'].unique())
company = st.selectbox("Company:", car_df['company'].unique())
year = st.selectbox("Year:", sorted(car_df['year'].unique()))  # Sorted years
kms_driven = st.selectbox("Kilometers Driven:", sorted(car_df['kms_driven'].unique()))  # Sorted kilometers driven
fuel_type = st.selectbox("Fuel Type:", car_df['fuel_type'].unique())


if st.button("Predict"):
    predicting = prediction(name, company, year, kms_driven, fuel_type)
    st.write(predicting)
