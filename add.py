import streamlit as st
from textblob import TextBlob
from PIL import Image
import pandas as pd
import os
import time
import glob
import os
from gtts import gTTS
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
resp3 = st.checkbox("Ira")
if resp1:
  st.write("La alegría nos permite disfrutar diferentes aspectos de la vida y generar actitudes positivas frente a estos. También favorece el aprendizaje y la memoria")
if resp2:
  st.write("La tristeza aumenta la cohesión con otras personas, nos permite valorar otros aspectos de la vida y fomenta la aparición de la empatía.")
if resp3:
  st.write("La ira moviliza la energía interior y elimina obstáculos en el camino.")

st.subheader("Si no encontraste una opción que te representara, escribe una palabra que describa tu estado emocional.")

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

try:
    os.mkdir("temp")
except:
    pass

st.subheader("Habla en voz alta y desahógate. Graba tu voz y escucha para procesar e interpretar desde otro punto de vista tus emociones.")

text = st.text_input("¿Desea escuchar la información?")

tld="es"

def text_to_speech(text, tld):
    
    tts = gTTS(text,"es", tld, slow=False)
    try:
        my_file_name = text[0:20]
    except:
        my_file_name = "audio"
    tts.save(f"temp/{my_file_name}.mp3")
    return my_file_name, text


#display_output_text = st.checkbox("Verifica el texto")

if st.button("Escuchar"):
    result, output_text = text_to_speech(text, tld)
    audio_file = open(f"temp/{result}.mp3", "rb")
    audio_bytes = audio_file.read()
    st.markdown(f"## Tú audio:")
    st.audio(audio_bytes, format="audio/mp3", start_time=0)

    #if display_output_text:
    st.markdown(f"## Texto en audio:")
    st.write(f" {output_text}")


def remove_files(n):
    mp3_files = glob.glob("temp/*mp3")
    if len(mp3_files) != 0:
        now = time.time()
        n_days = n * 86400
        for f in mp3_files:
            if os.stat(f).st_mtime < now - n_days:
                os.remove(f)
                print("Deleted ", f)


remove_files(7)

