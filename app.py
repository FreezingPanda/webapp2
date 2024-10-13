import streamlit as st
import requests
from streamlit_lottie import st_lottie
from PIL import Image

# Set page configuration
st.set_page_config(page_title="FreezingPandaDev", page_icon=":panda_face:", layout="wide")

# Load Lottie animation from URL
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        st.write("No animation rn :()")
        return None
    return r.json()

# Use local images for portfolio
img_gm = Image.open("images/gm.png")
img_contact_form_vs = Image.open("images/vs.png")

# Lottie animation link
lottie_coding = load_lottieurl("https://lottie.host/ff849127-3b12-4969-8108-77fb056224c1/V0AFiFDmxq.json")

# Hero Section (Introduction)
with st.container():
    st.title("👋 Hello, I'm Panda")
    st.write("### An Australian-based high school student, game developer, and programmer.")
    st.write(
        "I'm passionate about creating games and apps. Ever since I started learning Python and exploring the world of development, "
        "I've been fascinated by the endless possibilities of what I can create."
    )

# Animation next to Introduction
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("##")
        st.write(
            """
            Since playing my first game on the Xbox 360, I’ve always wondered how they worked. 
            In 2023, I downloaded Python and VS Code for the first time, and wrote my first program. 
            My goal is to continue learning and eventually create my dream game!
            """
        )
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# Divider
st.write("---")

# Links Section
st.subheader("🔗 Connect with me")
st.write("You can find me on these platforms:")
columns = st.columns(4)
columns[0].subheader("[GameJolt]()")
columns[1].subheader("[GitHub](https://github.com/FreezingPanda)")
columns[2].subheader("[lastfm](https://www.last.fm/user/FreezingPanda)")
columns[3].subheader("[guns.lol](https://guns.lol/freezingpanda)")
 # Open the file in binary mode and read its contents
file_path = "turret_game_windows.zip"
with open(file_path, "rb") as file:
    file_data = file.read()

st.download_button(
    label="Turret Game Offline",
    data=file_data,
    file_name="turret_game_windows.zip",
    mime="application/zip"
)


# What I Use Section
st.write("---")
st.header("🛠 What I Use")
st.write("### Tools & Software")
tools_column, description_column = st.columns((1, 2))
with tools_column:
    st.image(img_contact_form_vs, caption="Visual Studio Code")
    st.image(img_gm, caption="GameMaker")
with description_column:
    st.write(
        """
        For app development and programming, I primarily use [Visual Studio Code](https://code.visualstudio.com/) and [Python](https://www.python.org/). 
        For game development, I use [GameMaker](https://gamemaker.io/en), which allows me to bring my creative ideas to life.
        """
    )
# Path to your zip file



# Create a download button
