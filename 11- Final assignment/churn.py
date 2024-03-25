# import library
import streamlit as st 
import pickle
import numpy as np
from PIL import Image
import pandas as pd
import pylance

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
    #st.set_page_config(page_title='Customer churn prediction', layout='wide')
    
    # add image
    image = Image.open('customer_service_1.jpg')
    st.image(image, use_column_width=False)
    add_selectbox =st.sidebar.selectbox('How would you liek to predict?',('Online','Batch'))
    st.sidebar.info('This app will predict customer churn and identify customer churn risk')
    st.sider.image(image)
    
    # add title
    st.title('Customer Churn Risk Prediction using Machine Learning')

        
    st.write('Please enter relevnt customer data')

    # take input from user
    MonthlyMinutes = st.number_input('Monthly minutes usage:', min_value=0, step=1)
    TotalRecurringCharge = st.number_input('Total recurring charges:', min_value=0, step=0.001)
    PercChangeMinutes = st.number_input('Minutes usage change over the given period', min_value=None, max_value=None, step=0.001)
    UniqueSubs = st.number_input('Number of Unique Subscritions:', min_value=0, step=1)
    Handsets = st.number_input('How many handsets the customer has:', min_value=0, step=1)
    CurrentEquipmentDays = st.number_input('How many days is the current equipment old:', min_value=0, step=1)
    HandsetRefurbished = st.number_input('Owns a refurbished handset| yes or no | yes = 1 and no = 0:',min_value=0, max_value=1, step=1)
    HandsetWebCapable = st.number_input('Owns a web capable handset| yes or no | yes = 1 and no = 0:',min_value=0, max_value=1, step=1)
    RetentionCalls = st.number_input('How many retention calls were made:', min_value=0, step=1)
    RetentionOffersAccepted = st.number_input('Accepted retention offer| yes or no | yes = 1 and no = 0:',min_value=0, max_value=1, step=1)
    CreditRating = st.number_input('Credit Rating, Range from 1 to 7 (Highest, High, Good, Medium, Good, Low, VeryLow ,Lowest)', min_value=1, max_value=7, step=1)
        
    # code for prediction
    predict =''
    
    ## button for prediction
    if st.button('Predict'):
        predict = churn_prediction([MonthlyMinutes,TotalRecurringCharge,PercChangeMinutes,
                                    UniqueSubs,Handsets,CurrentEquipmentDays,
                                    HandsetRefurbished, HandsetWebCapable, RetentionCalls,
                                    RetentionOffersAccepted, CreditRating])
    
    st.success(predict)
    
    # run script
main()

# if __name__=='__main__':
#     main()