# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 14:58:18 2021

@author: rajeevramesh
"""

import pandas as pd
import streamlit as st
import numpy as np
import pickle
import config
import requests
import base64
import helper as help
import matplotlib.pyplot as plt


model = pickle.load(open('classifier.pkl','rb'))

b = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21]

a = ['Apple','Banana','blackgram','chickpea','coconut','coffee',
     'cotton','grapes','jute','kidney beans','lentil','maize','mango',
     'moth beans','mung bean','muskmelon','orange','papaya','pigeonpeas',
     'pomegranate','Rice','Watermelon']

a = pd.DataFrame(a,columns=['label'])
b = pd.DataFrame(b,columns=['encoded'])
classes = pd.concat([a,b],axis=1).sort_values('encoded').set_index('label')


def predict(n,p,k,temp,humi,ph,rain):
    data=[[n,p,k,temp,humi,ph,rain]]
    pred = model.predict(data)
    
    #fetching the label for given encoded value
    for i in range(0,len(classes)):
        if(classes.encoded[i]==pred):
            output = classes.index[i].upper()
    return output

def predict_proba(n,p,k,temp,humi,ph,rain):
    data=[[n,p,k,temp,humi,ph,rain]]
    pred = model.predict_proba(data)
    pred = pd.DataFrame(data = np.round(pred.T*100,2), index=classes.index,columns=['predicted_values'])
    high = pred.predicted_values.nlargest(5)
    return high

def weather_fetch(city_name):
    """
    Fetch and returns the temperature and humidity of a city
    :params: city_name
    :return: temperature, humidity
    """
    weather_api_key = "9d7cde1f6d07ec55650544be1631307e"
    api_key = weather_api_key
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()

    if x["cod"] != "404":
        y = x["main"]

        temperature = round((y["temp"] - 273.15), 2)
        humidity = y["humidity"]
        return temperature, humidity
    else:
        return None




def main():
    #st.image('download.png')
    
    
    b1, titl, b2 = st.columns([1,5,1])
    titl.title('Crop Recommendation')
    st.sidebar.header('Enter the details')
    n = st.sidebar.number_input('Nitrogen(N) value in soil',value=1)
    p = st.sidebar.number_input('Phosphorous(P) value in soil',value=1)
    k = st.sidebar.number_input('Potassium(K) value in soil',value=1)
    ph = st.sidebar.number_input('PH value',value=1.0)
    rain = st.sidebar.number_input('Rain Fall in mm',value=1.0)
    c_name=st.sidebar.text_input("Enter city name",value="Delhi")
    
    temp,humi=weather_fetch(c_name)

    if st.button('Predict'):
        prediction = predict(n,p,k,temp,humi,ph,rain)
        b5, res, b6 = st.columns([1,5,1])
        res.header('Recommended Crop : {}'.format(prediction))

    if st.checkbox('Charts'):
        b3, res, b4 = st.columns([1,5,1])
        st.header('Top 5 recommended Crops')
        pred1 = predict_proba(n,p,k,temp,humi,ph,rain)
        fig, axes = plt.subplots()
        axes.pie(x=pred1,autopct='%1.1f%%',labels=pred1.index,explode=(0.1, 0, 0, 0, 0),shadow=True,startangle=90)
        st.pyplot(fig)
        
if __name__=='__main__':
    main()

