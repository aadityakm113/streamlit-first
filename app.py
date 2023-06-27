import streamlit as st
import requests
from PIL import Image
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Aaditya's Streamlit Site",page_icon=":sign_of_the_horns:", layout="wide" )

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
#load assets
lottie_guitar=load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_cyvidjfv.json")
lottie_webdev=load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_tvpnb2fp.json")
img_bday=Image.open("Images/birthday-invite.png")
img_movies=Image.open("Images/movie-ranking.png")

#Header
with st.container():
    left_column,right_column=st.columns(2)
    with left_column:
        st.header("Streamlit Website")
        st.subheader("Hi my name is Aaditya! :wave:")
        st.title("A budding Web Developer")
        st.write("I am a CS student passionate about web development and coding!")
        st.write("This is my first time using streamlit and it is very nice!")
        st.write("[GitHub](https://github.com/aadityakm113)")
    with right_column:
        st_lottie(lottie_webdev,height=300,key="webdev")

#About
with st.container():
    st.write("---")
    left_column,right_column=st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write('''
        - I am a Third Year Engineering Student
        - I play the guitar in a Prog Metal Band
        - I watch a lot of movies
        ''')
    with right_column:
        st_lottie(lottie_guitar,height=300,key="guitar")

#Projects
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("A few examples of some very basic web dev projects")
    image_col,textcol=st.columns((1,2))
    with image_col:
        st.image(img_bday)
        
    with textcol:
        st.write("Birthday party invitation")
        
    
with st.container():
    image_col,textcol=st.columns((1,2))
    with image_col:
        st.image(img_movies)
    with textcol:
        st.write("Movie ranking list")