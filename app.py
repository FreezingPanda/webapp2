import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="FreezingPanda's Web Portfolio", page_icon="", layout="wide")

def load_lottieurl(url):
 r = requests.get(url)
 if r.status_code != 200:
    st.write("No animation rn :()")
    return None
    
 return r.json()

st.subheader("Hello, I am Panda")
st.title("An Australian based high school student, gamedev & programmer")

st.write("I am passionate about game development and app creation, I've always wanted to work with code and make software. And here I am now!")         

lottie_coding = load_lottieurl("https://lottie.host/ff849127-3b12-4969-8108-77fb056224c1/V0AFiFDmxq.json")
img_gm = Image.open("images/gm.png")
img_contact_form_vs = Image.open("images/vs.png")
with st.container():
 left_column, right_column = st.columns(2)
 with left_column:
  st.write("##")
  st.write("""Ever since I first played a game on the Xbox 360, I wondered how it all worked, what made it 
          tick and how you added more to it, I never really looked too far into it until 2023, when I downloaded
           Python and VS Code for the first time, and wrote my first program""")
  st.write("I plan to eventually make my dream game when I develop more programming skills, right now it's just a lot of learning and getting better!")
  
 st.write("---")
 st.subheader("Links:")

 st.write("[GameJolt]()")
 st.write("[GitHub](https://github.com/FreezingPanda)")
 st.write("[lastfm](https://www.last.fm/user/FreezingPanda)")
 st.write("[guns.lol](https://guns.lol/freezingpanda)")

with right_column:
  st_lottie(lottie_coding, height=300, key="coding")


with st.container():
  st.write("---")
  st.header("What I use")
  st.header("##")
  image_column, text_column = st.columns((1, 2))
  with image_column:
    st.image(img_contact_form_vs)
    st.image(img_gm)
  with text_column:
    st.subheader("The software I use")
    st.write("I [use Visual Studio Code](https://code.visualstudio.com/) and [Python](https://www.python.org/) for standard programming and app development, but for game development I use [GameMaker](https://gamemaker.io/en)")

