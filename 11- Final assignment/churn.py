# import library
import streamlit as st 
import pickle
import numpy as np
from PIL import Image

# load the pickle file
with open('churn_model.pkl', 'rb') as file:
    model = pickle.load(file)
    
# create function for prediction
def churn_prediction(input):
    input_array =np.asarray(input)
    input_reshape = input_array.reshape(1,-1)
    prediction = model.predict(input_reshape)
    print(prediction)
    
    if(prediction[0] == 0):
       return 'Customer not likely to churn'
    else:
       return 'Customer is likely to churn'


# set up streamlit page
def main():
    st.set_page_config(page_title='Customer churn prediction', layout='wide')
    
    # add image
    image = Image.open('customer_service_1.jpg')
    st.image(image, use_column_width=False)
    
    # add title
    st.title('Customer Churn Risk Prediction using Machine Learning')
    st.write('Please enter relevnt customer data')
    
    # take input from user
    df_selection =dff[['MonthlyMinutes', 'TotalRecurringCharge', 
                       'PercChangeMinutes','UniqueSubs','Handsets', 
                       'HandsetModels',
                  'CurrentEquipmentDays', 'HandsetRefurbished',
                  'HandsetWebCapable','RetentionCalls',
                  'RetentionOffersAccepted', 'CreditRating']]
    MonthlyMinutes = st.number_input('Monthly minutes usage:', min_value=0, step=1)
    TotalRecurringCharge = st.number_input('Total recurring charges:', min_value=0, step=0.001)
    PercChangeMinutes = st.number_input('Minutes usage change over the given period', min_value=None, max_value=None, step=0.001)
    UniqueSubs = st.number_input('Number of Unique Subscritions:', )
    Handsets = st.number_input
    HandsetModels = st.number_input
    CurrentEquipmentDays = st.number_input
    HandsetRefurbished = st.number_input
    HandsetWebCapable = st.number_input
    RetentionCalls = st.number_input
    RetentionOffersAccepted = st.number_input
    CreditRating = st.number_input('Credit Rating, Range from 1 to 7 (Highest, High, Good, Medium,Good' '2-High' '5-Low, VeryLow ,Lowest')