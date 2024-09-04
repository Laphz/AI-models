import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor


# Load the dataset
df = pd.read_csv('abalone.csv')
df['Sex'] = df['Sex'].map({'M': 0, 'F': 1, 'I': 2})

# Prepare the data
x = df.drop('Rings', axis=1)
y = df['Rings']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state=42)

scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

# Train the model
rfr = RandomForestRegressor()
rfr.fit(x_train, y_train)

# Define a prediction function
def predict_age(Sex, Length, Diameter, Height, Whole_weight, Shucked_weight, Viscera_weight, Shell_weight):
    features = np.array([[Sex, Length, Diameter, Height, Whole_weight, Shucked_weight, Viscera_weight, Shell_weight]])
    scaled_features = scaler.transform(features)
    prediction = rfr.predict(scaled_features)
    return prediction[0]

# Streamlit app
st.set_page_config(page_title = "Abalone Age Prediction")
st.title('Abalone Age Prediction')
img = Image.open('img.jpeg')
img = img.resize((650,250))
st.image(img)
st.write("""
This app predicts the age of an abalone based on its physical measurements.
""")

col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)

with col1:
    Sex = st.selectbox('Sex', ['Male', 'Female', 'Infant'])
    Sex = {'Male': 0, 'Female': 1, 'Infant': 2}[Sex]
    Height = st.number_input('Height')

with col2:
    Length = st.number_input('Length')
    Whole_weight = st.number_input('Whole Weight')

with col3:
    Diameter = st.number_input('Diameter')
    Shucked_weight = st.number_input('Shucked Weight')

with col4:
    Viscera_weight = st.number_input('Viscera weight')

with col5:
    Shell_weight = st.number_input('Shell weight')

if st.button('Predict Age'):
    age = predict_age(Sex, Length, Diameter, Height, Whole_weight, Shucked_weight, Viscera_weight, Shell_weight)
    st.success(f'The predicted age of the abalone is: {age:.2f} years')

