# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 15:23:27 2021

@author: rajeevramesh
"""
import streamlit as st
from utils.fertilizer import fertilizer_dic
import pandas as pd

def main():
    b1, titl, b2 = st.columns([1,5,1])
    st.sidebar.header('Enter the details')
    N = st.sidebar.number_input('Nitrogen(N) value in soil',value=1)
    P = st.sidebar.number_input('Phosphorous(P) value in soil',value=1)
    K = st.sidebar.number_input('Potassium(K) value in soil',value=1)
    crop_name=st.sidebar.selectbox('Select a crop',('rice', 'maize' ,'chickpea', 'kidneybeans', 'pigeonpeas' ,'mothbeans',
    'mungbean' ,'blackgram', 'lentil', 'pomegranate' ,'banana' ,'mango' ,'grapes',
    'watermelon', 'muskmelon', 'apple', 'orange', 'papaya', 'coconut' ,'cotton',
    'jute' ,'coffee'))
    df = pd.read_csv('Data/fertilizer.csv')
    titl.title('Fertilizer Suggestion')
    # ph = float(request.form['ph'])
    if st.button('Predict'):
        nr = df[df['Crop'] == crop_name]['N'].iloc[0]
        pr = df[df['Crop'] == crop_name]['P'].iloc[0]
        kr = df[df['Crop'] == crop_name]['K'].iloc[0]

        n = nr - N
        p = pr - P
        k = kr - K
        temp = {abs(n): "N", abs(p): "P", abs(k): "K"}
        max_value = temp[max(temp.keys())]
        if max_value == "N":
            if n < 0:
                key = 'NHigh'
            else:
                key = "Nlow"
        elif max_value == "P":
            if p < 0:
                key = 'PHigh'
            else:
                key = "Plow"
        else:
            if k < 0:
                key = 'KHigh'
            else:
                key = "Klow"

        response = str(fertilizer_dic[key])
        st.title(response)

    

    

if __name__=='__main__':
    main()
    
    
    