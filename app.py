import streamlit as st
import pandas as pd
import numpy as np
from Flexicar_scraping import FlexicarScraping
from Concat_funtion import concat
from config import *
from PIL import Image

st.title('¿CUÁL ES EL MEJOR VEHÍCULO QUE SE ADAPTA MEJOR A MIS NECESIDADES?')

img= Image.open('feriaVO.jpg')
st.image(img,width=690)

km = st.selectbox(
    "¿Cuántos Km haces al año?", 
    ("Más de 15.000 km","Menos de 15.000km")
)

km1='You selected: ', km
uso = st.selectbox(
    "¿Cómo serán tus desplazamientos con tu vehículo?",
     ("Sobretodo por ciudad y muy pocos viajes por carretera al año.",
     "Por ciudad y carretera por igual.", "Uso el vehículo sobretodo para viajar y muy poco por ciudad.",
     )
)
uso1='You selected: ', uso

familia = st.selectbox(
    "¿Cuántas personas suelen viajar contigo?",
     ("Suelo viajar sólo y/o una persona más.",
     "Suelo viajar con la familia (3 personas máx).", 
     "Suelo viajar con la familia (más de 3 personas)."
     )
)       
familia1='You selected: ', familia

vid_file=open("video.mp4","rb").read()
st.video(vid_file)
if km1==('You selected: ', 'Menos de 15.000km') and uso1==('You selected: ', 'Sobretodo por ciudad y muy pocos viajes por carretera al año.') and familia1==('You selected: ', 'Suelo viajar sólo y/o una persona más.'):
    df=FlexicarScraping(Tipo1)
    st.write("Puedes encontrar los detalles de tu resultado haciendo click en la URL:")
    st.write("Click aquí:",Tipo1)
    st.dataframe(df)
elif km1 == ('You selected: ', 'Menos de 15.000km') and uso1 == ('You selected: ', 'Por ciudad y carretera por igual.') and familia1 == ('You selected: ', 'Suelo viajar sólo y/o una persona más.'):
    df=FlexicarScraping(Tipo2)
    st.write("Puedes encontrar los detalles de tu resultado haciendo click en la URL:")
    st.write("Click aquí:",Tipo2)
    st.dataframe(df)
elif km1 == ('You selected: ', 'Más de 15.000 km') and uso1 == ('You selected: ', 'Sobretodo por ciudad y muy pocos viajes por carretera al año.') and familia1 == ('You selected: ', 'Suelo viajar sólo y/o una persona más.'):
    df=FlexicarScraping(Tipo3)
    st.write("Puedes encontrar los detalles de tu resultado haciendo click en la URL:")
    st.write("Click aquí:",Tipo3)
    st.dataframe(df)
elif km1 == ('You selected: ', 'Más de 15.000 km') and uso1 == ('You selected: ', 'Uso el vehículo sobretodo para viajar y muy poco por ciudad.') and familia1 == ('You selected: ', 'Suelo viajar con la familia (3 personas máx).'):
    df=FlexicarScraping(Tipo4)
    st.write("Puedes encontrar los detalles de tu resultado haciendo click en la URL:")
    st.write("Click aquí:",Tipo4)
    st.dataframe(df)
elif km1 == ('You selected: ', 'Menos de 15.000km') and uso1 == ('You selected: ', 'Sobretodo por ciudad y muy pocos viajes por carretera al año.') and familia1 == ('You selected: ', 'Suelo viajar con la familia (3 personas máx).'):
    df=FlexicarScraping(Tipo5)
    st.write("Puedes encontrar los detalles de tu resultado haciendo click en la URL:")
    st.write("Click aquí:",Tipo5)
    st.dataframe(df)
elif km1 == ('You selected: ', 'Menos de 15.000km')and uso1 == ('You selected: ', 'Sobretodo por ciudad y muy pocos viajes por carretera al año.') and familia1 ==('You selected: ', 'Suelo viajar con la familia (más de 3 personas).'):
    df=FlexicarScraping(Tipo6)
    st.write("Puedes encontrar los detalles de tu resultado haciendo click en la URL:")
    st.write("Click aquí:",Tipo6)
    st.dataframe(df)
elif km1 == ('You selected: ', 'Más de 15.000 km') and uso1 == ('You selected: ', 'Uso el vehículo sobretodo para viajar y muy poco por ciudad.') and familia1 ==('You selected: ', 'Suelo viajar con la familia (más de 3 personas).'):
    df=FlexicarScraping(Tipo7)
    st.write("Puedes encontrar los detalles de tu resultado haciendo click en la URL:")
    st.write("Click aquí:",Tipo7)
    st.dataframe(df)
elif km1 == ('You selected: ', 'Más de 15.000 km') and uso1 == ('You selected: ', 'Sobretodo por ciudad y muy pocos viajes por carretera al año.') and familia1 ==('You selected: ', 'Suelo viajar sólo y/o una persona más.'):
    df=FlexicarScraping(Tipo3)
    st.write("Puedes encontrar los detalles de tu resultado haciendo click en la URL:")
    st.write("Click aquí:",Tipo3)
    st.dataframe(df)
elif km1 == ('You selected: ', 'Menos de 15.000 km') and uso1 == ('You selected: ', 'Uso el vehículo sobretodo para viajar y muy poco por ciudad.') and familia1 ==('You selected: ', 'Suelo viajar con la familia (más de 3 personas).'):
    df=FlexicarScraping(Tipo6)
    st.write("Puedes encontrar los detalles de tu resultado haciendo click en la URL:")
    st.write("Click aquí:",Tipo6)
    st.dataframe(df)

st.sidebar.header("¿Cómo funciona este calificador de usuarios?")
st.sidebar.text("Este programa te recomienda los vehículos que están en el momento de la consulta. Te mostrará los vehículos que más se adapten a sus necesidades.")