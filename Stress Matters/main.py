"""This is the main module to run the app"""

# Importing the necessary Python modules.
import streamlit as st

# Import necessary functions from web_functions
from web_functions import load_data

# Import pages
from Tabs import home, data, predict, visualise

# Configure the app
st.set_page_config(
    page_title = 'Stress Matters',
    page_icon = 'heavy_exclamation_mark',
    layout = 'wide',
    initial_sidebar_state = 'auto'
)

# Dictionary for pages
Tabs = {
    "Home": home,
    "About the dataset": data,
    "Predict your stress levels": predict,
    "Visualise your parameters": visualise
    
}

# Create a sidebar
# Add title to sidear
st.sidebar.title("Stress Matters")

# Create radio option to select the page
page = st.sidebar.radio("We offer: ", list(Tabs.keys()))

# Loading the dataset.
df, X, y = load_data()

# Call the app funciton of selected page to run
if page in ["Predict your stress levels", "Visualise your parameters"]:
    Tabs[page].app(df, X, y)
elif (page == "About the dataset"):
    Tabs[page].app(df)
else:
    Tabs[page].app()
