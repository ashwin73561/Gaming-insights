import streamlit as st
from Home import main as Home_app
from prediction import main as app4_app
from resources import main as Resource_app
st.markdown(
        f"""
        <style>
        .stApp {{
            background-color:#ffffff ;
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

PAGES = {
    "Home": Home_app,
    "Prediction": app4_app,
    "Resource":Resource_app
}
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page()
