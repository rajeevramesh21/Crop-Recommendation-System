# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 15:57:01 2021

@author: rajeevramesh
"""

import streamlit as st
st.set_page_config(page_title=None, page_icon=None, layout="centered", initial_sidebar_state="auto", menu_items=None)
@st.cache(suppress_st_warning=True)
def main():
    st.title("AI Based Crop Suggestion")