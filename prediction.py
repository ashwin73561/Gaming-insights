import streamlit as st
import pickle
from PIL import Image

def main():
    st.title(':rainbow[ONLINE GAMING PREDICTION]')
    # img=Image.open('project.jpg')
    # st.image(img,width=580)
    age = st.text_input("Age","")
    GameGenre=st.radio("Select GameGenre",options=["Action","RPG","Simulation","Sports","Strategy"])
    if GameGenre=='Action':
       ge=0
    elif GameGenre=='RPG':
        ge=1
    elif GameGenre=='Simulation':
        ge=2
    elif GameGenre=='Sports':
        ge=3
    else:
        ge=4
    pt = st.text_input("Enter Play Time Hours","Type here")
    igp=st.radio("In Game Purchases",options=[0,1])
    spw = st.text_input("Sessions Per Week","Type here")
    asdm = st.text_input("Average Session Duration Minutes","Type here")
    pl = st.text_input("Player Level","Type here")
    au = st.text_input("Achievements Unlocked","Type here")
    features=[age,ge,pt,igp,spw,asdm,pl,au]
    scaled=pickle.load(open('scal.sav','rb'))
    model=pickle.load(open('mod.sav','rb'))
    pred=st.button('PREDICT')
    if pred:
        result=model.predict(scaled.transform([features]))
        if result==0:
            st.write('person has a high engagement level')
        elif result==1:
            st.write('person has a low engagement level')
        else:
            st.write('person has a medium engagement level')

    # url = 'https://colab.research.google.com/drive/1gvojm_nWLKZe7e5XaK-gcX_XZtAgayud#scrollTo=7OaV7Kc9hV8w'
    # st.write("Code[https://colab.research.google.com/drive/1gvojm_nWLKZe7e5XaK-gcX_XZtAgayud#scrollTo=7OaV7Kc9hV8w](%s)" % url)
    # st.header("Accuracy Comparison Of Models")
    # imag = Image.open('compare.png')
    # st.image(imag, use_column_width=None, width=500)
main()
