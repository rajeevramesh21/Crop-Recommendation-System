# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 13:08:31 2021

@author: rajeevramesh
"""

import streamlit as st
from multipage import MultiPage
import p_app
import f_predict
import home
import plant_disease_detect
import helper as help
app = MultiPage()
st.title("Crop Doctor")


help.set_bg_hack()
# Add all your applications (pages) here
app.add_page("Home", home.main)
app.add_page("Suitable Crop Prediction", p_app.main)
app.add_page("Fertilizer Prediction", f_predict.main)
app.add_page("Plant Disease Prediction",plant_disease_detect.main)





app.run()