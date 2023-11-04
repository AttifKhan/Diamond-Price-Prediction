# -*- coding: utf-8 -*-
"""
Created on Mon Jun  6 08:47:19 2022

@author: Admin
"""

#pip install sreamlit

import streamlit as st
import pandas as pd
import pickle
from PIL import Image

#st.title('Laptop Price Prediction')

st.markdown("<h1 style='text-align: center; color: greeen;'>Diamond price</h1>", unsafe_allow_html=True)
image = Image.open('dia.jpg')
col1, col2, col3 = st.columns(3)
with col1:
    st.write('')
with col2:
    st.image(image,width=300)
with col3:
    st.write('')
st.markdown("<h1 style='text-align: centre; color: black; font-size: 25px';></h1>", unsafe_allow_html=True)




st.sidebar.header('User Input Parameters')



def user_input_features():
    carat = st.sidebar.slider('carat',min_value=0.2,max_value=5.01,step=0.1)
    cut = st.sidebar.selectbox('cut',('Ideal', 'Premium', 'Good', 'Very Good', 'Fair'))
    color = st.sidebar.selectbox('color',('E', 'I', 'J', 'H', 'F', 'G', 'D'))
    
    clarity = st.selectbox("clarity",('SI2', 'SI1', 'VS1', 'VS2', 'VVS2', 'VVS1', 'I1', 'IF'))
    depth = st.slider("depth",min_value=43.0,max_value=79.0,step=0.1)
    
    table = st.sidebar.slider('table',min_value=43.0,max_value=95.0,step=0.1)    
    x = st.sidebar.slider('x',min_value=3.73,max_value=10.74,step=0.1)
    
    y = st.slider("y",min_value=3.68,max_value=58.9,step=0.1)
    
    z = st.sidebar.slider('z',min_value=1.07,max_value=31.8,step=0.1)
    
    
    data={'carat': carat,
         'cut': cut,
         'color': color,
         'clarity': clarity,
         'depth': depth,
         'table': table,
    
         'x': x,
         'y': y,
         'z': z}
    
    

    features = pd.DataFrame(data,index = [0])
    return features 
    
df = user_input_features()
st.subheader('User Input parameters')
st.write(df)



with open(file="model.sav",mode="rb") as f1:
    model = pickle.load(f1)
    
    
prediction = model.predict(df)
#prediction_proba = clf.predict_proba(df)

st.subheader('Predicted Result')
#st.write('Yes' if prediction_proba[0][1] > 0.5 else 'No')

#st.subheader('Prediction Probability')
st.write(prediction[0])
















