from textblob import TextBlob
import pandas as pd
import os
import time
import glob
import os
from gtts import gTTS
import streamlit as st
from PIL import Image
from googletrans import Translator

st.title("Análisis Emocional")
st.header("Plataforma de expresión y liberación emocional.")
st.write("A través de esta plataforma podrás evaluar tu estado emocional diariamente y encontrar formas de regular tu estado.")
image = Image.open("FeelingsWheel.png")

st.image(image, caption="Rueda de emociones")

st.subheader("Guía Inicial")
st.write("¿Como te sientes hoy?")
resp1 = st.checkbox("Alegría")
resp2 = st.checkbox("Tristeza")
if resp1:
  st.write("La alegría nos permite disfrutar diferentes aspectos de la vida y generar actitudes positivas frente a estos. También favorece el aprendizaje y la memoria")
if resp2:
  st.write("La alegría nos permite disfrutar diferentes aspectos de la vida y generar actitudes positivas frente a estos. También favorece el aprendizaje y la memoria")


st.subheader("¿Cómo te sientes hoy? Escribe una palabra que describa tu estado emocional.")

translator = Translator()

with st.expander('Analizar texto'):
    text = st.text_input('Escribe por favor: ')
    if text:

        translation = translator.translate(text, src="es", dest="en")
        trans_text = translation.text
        blob = TextBlob(trans_text)
        st.write('Polarity: ', round(blob.sentiment.polarity,2))
        st.write('Subjectivity: ', round(blob.sentiment.subjectivity,2))
        x=round(blob.sentiment.polarity,2)
        if x >= 0.5:
            st.write( 'Es un sentimiento Positivo 😊')
        elif x <= -0.5:
            st.write( 'Es un sentimiento Negativo 😔')
        else:
            st.write( 'Es un sentimiento Neutral 😐')

