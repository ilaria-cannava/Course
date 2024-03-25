import streamlit as st
import pandas as pd
import pickle

# Load the pre-trained model
with open('churn_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Function to predict churn
def predict_churn(data):
    predictions = model.predict(data)
    return predictions

# Streamlit App
def main():
    st.title('Customer Churn Prediction')

    # Sidebar for uploading file
    st.sidebar.title('Upload File')
    uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=["csv"])

    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file)
        st.dataframe(data.head())

        # Button to trigger prediction
        if st.button('Predict Churn'):
            # Assume your data preprocessing steps here
            # Assuming X contains the input features for prediction
            predictions = predict_churn(X)
            data['Predictions'] = predictions
            
            # Save predictions to CSV
            output_filename = "predictions.csv"
            data.to_csv(output_filename, index=False)
            st.success(f"Predictions saved to {output_filename}")

if __name__ == "__main__":
    main()