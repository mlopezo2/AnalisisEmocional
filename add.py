import streamlit as st
from PIL import Image

st.title("Análisis Emocional")
st.header("Plataforma de expresión y liberación emocional.")
st.write("A través de esta plataforma podrás ")
image = Image.open("FeelingsWheel.png")

st.image(image, caption="Rueda de emociones")
