import streamlit as st
from PIL import Image
def main():
    st.title(":rainbow[ONLINE GAMING BEHAVIOUR PREDICTION]")
    st.write("The objective of my project is to find the engagement level of the person who plays games based on the details they provided")
    img = Image.open('project.jpg')
    st.image(img, width=450)