"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st

def app():
    """This function create the home page"""
    
    # Add title to the home page
    st.title("Stress Level Detector")

    # Add brief describtion of your web app
    st.markdown(
    """<p style="font-size:20px;">
            Stress is the most common problem in young adults today, and often ignored, unacknowledged and causing several health issues. 
    """, unsafe_allow_html=True)

    st.markdown(
    """<p style="font-size:20px;">
            Our app helps you predict your stress levels based on a given health dataset and parameters. 
    """, unsafe_allow_html=True)

    st.markdown(
    """<p style="font-size:20px;">
            Additionally, it helps you understand the various body parameters contributing to the stress. 
    """, unsafe_allow_html=True)

    st.markdown(
    """<p style="font-size:20px;">
            Please note that this app is not a substitute for professional medical help and only a tool. 
    """, unsafe_allow_html=True)