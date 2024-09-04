import pandas as pd
import numpy as np
from PIL import Image
import pickle as pkl
import streamlit as st 

st.markdown("""
    <style>
    .stTextInput input {
        font-size: 18px;  /* Change the font size of the text inside the box */
        height: 45px;     /* Adjust the height of the input box */
        width: 500px;     /* Adjust the width of the input box */
        padding: 10px;    /* Add padding for better appearance */
    }
    </style>
    """, unsafe_allow_html=True)

lg = pkl.load(open('model.pkl','rb'))

# web app 
st.set_page_config(page_title = "Job Placement Predication Model")
img = Image.open('img.jpeg')
st.image(img,width = 600)
st.title('Job Placement Predication Model')
input_text = st.text_input("Enter all the features:")

if input_text:
    input_list = input_text.split(',')
    np_df = np.asarray(input_list,dtype = float)
    pred = lg.predict(np_df.reshape(1,-1))
    if pred[0] == 1:
        st.markdown("<p style='font-size:24px; font-weight:bold;'>Already Placed</p>", unsafe_allow_html=True)

    else:
        st.markdown("<h1 style='font-size:24px; font-weight:bold;'>Not Placed</h1>", unsafe_allow_html=True)

