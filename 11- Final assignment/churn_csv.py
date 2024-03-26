import streamlit as st
import pickle
import numpy as np
import pandas as pd
from PIL import Image

# Load the model
def load_model():
    try:
        with open('churn_model.pkl', 'rb') as file:
            model = pickle.load(file)
        return model
    except Exception as e:
        st.error(f"Error loading the model: {e}")
        return None

model = load_model()

# Function for making predictions
def churn_prediction(input_df):
    prediction = model.predict(input_df)
    return prediction

# Streamlit UI
def main():
    st.set_page_config(page_title='Customer churn prediction', layout='wide')
    
    # Add image
    image = Image.open('customer_service_1.jpg')
    st.image(image, use_column_width=False)
    
    # Add title
    st.title('Customer Churn Risk Prediction using Machine Learning')
    st.write('Please enter relevant customer data or upload a CSV file.')
    
    # Option to input data manually
    st.write('### Manually Input Data for a single customer or upload a csv file below')
    MonthlyMinutes = st.number_input('Monthly minutes usage:', min_value=0, step=1)
    TotalRecurringCharge = st.number_input('Total recurring charges:', min_value=0, step=1)
    PercChangeMinutes = st.number_input('Minutes usage change over the given period', min_value=-1000, step=1)
    UniqueSubs = st.number_input('Number of Unique Subscriptions:', min_value=0, step=1)
    Handsets = st.number_input('How many handsets the customer has:', min_value=0, step=1)
    CurrentEquipmentDays = st.number_input('How many days is the current equipment old:', min_value=0, step=1)
    HandsetRefurbished = st.number_input('Owns a refurbished handset? (yes=1, no=0):', min_value=0, max_value=1, step=1)
    HandsetWebCapable = st.number_input('Owns a web capable handset? (yes=1, no=0):', min_value=0, max_value=1, step=1)
    RetentionCalls = st.number_input('How many retention calls were made:', min_value=0, step=1)
    RetentionOffersAccepted = st.number_input('Accepted retention offer? (yes=1, no=0):', min_value=0, max_value=1, step=1)
    CreditRating = st.number_input('Credit Rating (1 to 7):', min_value=1, max_value=7, step=1)
    
    # Option to upload CSV file
    st.write('### Upload CSV File')
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    
    # If file is uploaded, make predictions
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            prediction = churn_prediction(df)
            df['Prediction'] = prediction
            st.write(df)
            # Add a download button to download the prediction results
            csv = df.to_csv(index=False)
            b64 = base64.b64encode(csv.encode()).decode()  # Convert DataFrame to base64
            href = f'<a href="data:file/csv;base64,{b64}" download="predictions.csv">Download CSV File</a>'
            st.markdown(href, unsafe_allow_html=True)
        except Exception as e:
            st.error(f"Error processing CSV file: {e}")

    # If "Predict" button is clicked, make predictions
    if st.button('Predict'):
        input_df = pd.DataFrame({
            'MonthlyMinutes': [MonthlyMinutes],
            'Total recurring charges':[TotalRecurringCharge],
            'Minutes usage change over the given period':[PercChangeMinutes],
            'Number of Unique Subscriptions':[UniqueSubs],
            'How many handsets the customer has':[Handsets],
            'How many days is the current equipment old':[CurrentEquipmentDays],
            'Owns a refurbished handset? (yes=1, no=0)':[HandsetRefurbished],
            'Owns a web capable handset? (yes=1, no=0)':[HandsetWebCapable],
            'How many retention calls were made':[RetentionCalls],
            'Accepted retention offer? (yes=1, no=0)':[RetentionOffersAccepted],
            'Credit Rating (1 to 7)':[CreditRating]
            
        })
        prediction = churn_prediction(input_df)
        st.write(prediction)

# Run the app
if __name__ == '__main__':
    main()