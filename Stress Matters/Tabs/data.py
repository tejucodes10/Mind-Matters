"""This modules contains data about home page"""

# Import necessary modules
import streamlit as st


def app(df):
    """This function create the Data Info page"""

    # Add title to the page
    st.title("About the stress level dataset")

    # Add subheader for the section
    st.subheader("View dataset")

    # Create an expansion option to check the data
    with st.expander("View dataset"):
        st.dataframe(df)

    

    # Add the link to you dataset
    st.markdown("""
                    <p style="font-size:24px">
                        <a 
                            href="https://raw.githubusercontent.com/DataMinati/Streamlit-Database/main/SaYoPillow.csv"
                            target=_blank
                            style="text-decoration:none;"
                        >Get Dataset
                        </a> 
                    </p>
                """, unsafe_allow_html=True
    )