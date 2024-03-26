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
    st.write('### Input Data Manually')
    MonthlyMinutes = st.number_input('Monthly minutes usage:', min_value=-100000, step=1)
    # Add other input fields here...
    
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
            # Add other input fields here...
        })
        prediction = churn_prediction(input_df)
        st.write(prediction)

# Run the app
if __name__ == '__main__':
    main()