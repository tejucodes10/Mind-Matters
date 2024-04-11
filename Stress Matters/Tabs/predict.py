"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st

# Import necessary functions from web_functions
from web_functions import predict


def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Predict your stress levels")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:#f63366">Decision Tree Classifier</b> for the Prediction of Stress Level.
            </p>
        """, unsafe_allow_html=True)
    
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    # Take input of features from the user.
    sr = st.slider("Snoring Rate", int(df["sr"].min()), int(df["sr"].max()))
    rr = st.slider("Respiration Rate", int(df["rr"].min()), int(df["rr"].max()))
    bt = st.slider("Body Temperature (in °F)", int(df["bt"].min()), int(df["bt"].max()))
    lm = st.slider("Limb Movement", float(df["lm"].min()), float(df["lm"].max()))
    bo = st.slider("Blood Oxygen(%)", float(df["bo"].min()), float(df["bo"].max()))
    rem = st.slider("Rapid Eye Movement", float(df["rem"].min()), float(df["rem"].max()))
    sh = st.slider("Number of hours of sleep", float(df["sh"].min()), float(df["sh"].max()))
    hr = st.slider("Heart Rate", float(df["hr"].min()), float(df["hr"].max()))
    

    # Create a list to store all the features
    features = [sr,rr,bt,lm,bo,rem,sh,hr]

    # Create a button to predict
    if st.button("Predict your stress level"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        st.info("Your stress level has been predicted")

        # Print the output according to the prediction
        if (prediction == 1):
            st.success("You have low stress level 🙂")
            st.write("Stress score =",str(prediction[0]))
        elif (prediction == 2):
            st.warning("You have medium stress level 😐")
            st.write("Stress score =",str(prediction[0]))
        elif (prediction == 3):
            st.error("You have high stress level! 😞")
            st.write("Stress score =",str(prediction[0]))
        elif (prediction == 4):
            st.error("You have very high stress level, please visit the doctor 😫")
            st.write("Stress score =",str(prediction[0]))
        else:
            st.success("You are stress free and calm, good job 😄")

        
