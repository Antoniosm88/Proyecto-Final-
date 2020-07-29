import streamlit as st
import pandas as pd
import numpy as np
from Flexicar_scraping import FlexicarScraping
from Concat_funtion import concat
from config import *

st.title('¿CUÁL ES EL MEJOR VEHÍCULO QUE SE ADAPTA MEJOR A MIS NECESIDADES?')
km = st.selectbox("¿Cuántos Km haces al año?", ["Menos de 15.000 km","----"])
km1 = st.selectbox("", ["Más de 15.000 km","----"])
uso = st.selectbox(
    "¿Cómo serán tus desplazamientos con tu vehículo?",
     ["Sobretodo por ciudad y muy pocos viajes por carretera al año.",
     "----"]
)
uso2 = st.selectbox(
    "",
     [
     "Por ciudad y carretera por igual.", "----"]
)
uso3 = st.selectbox(
    "",
     [ "Uso el vehículo sobretodo para viajar y muy poco por ciudad.", "----"
     ]
)

familia = st.selectbox(
    "¿Cuántas personas suelen viajar contigo?",
     ["Suelo viajar sólo y/o una persona más.",
     "----"])

familia2 = st.selectbox(
    "",
     [
     "Suelo viajar con la familia (3 personas máx).", 
     "----"])
familia3 = st.selectbox(
    "",
     ["Suelo viajar con la familia (más de 3 personas).","----"])          


if km == "Menos de 15.000km" and uso == "Sobretodo por ciudad y muy pocos viajes por carretera al año." and familia == "Suelo viajar sólo y/o una persona más.":
    df=FlexicarScraping(Tipo1)
    st.dataframe(df)

elif km == "Menos de 15.000 km" and uso == "Por ciudad y carretera por igual." and familia == "Suelo viajar sólo y/o una persona más.":
    df=FlexicarScraping(Tipo2)
    st.dataframe(df)
elif km == "Más de 15.000 km" and uso == "Uso el vehículo sobretodo para viajar y muy poco por ciudad." and familia == "Suelo viajar sólo y/o una persona más.":
    df=FlexicarScraping(Tipo3)
    st.dataframe(df)
elif km == "Más de 15.000 km" and uso == "Uso el vehículo sobretodo para viajar y muy poco por ciudad." and familia == "Suelo viajar con la familia (3 personas máx).":
    df=FlexicarScraping(Tipo4)
    st.dataframe(df)
elif km == "Menos de 15.000km" and uso == "Sobretodo por ciudad y muy pocos viajes por carretera al año." and familia == "Suelo viajar con la familia (3 personas máx).":
    df=FlexicarScraping(Tipo5)
    st.dataframe(df)
elif km == "Menos de 15.000km" and uso == "Sobretodo por ciudad y muy pocos viajes por carretera al año." and familia =="Suelo viajar con la familia (más de 3 personas).":
    df=FlexicarScraping(Tipo6)
    st.dataframe(df)
elif km == "Más de 15.000km" and uso == "Uso el vehículo sobretodo para viajar y muy poco por ciudad." and familia =="Suelo viajar con la familia (más de 3 personas).":
    df=FlexicarScraping(Tipo7)
    st.dataframe(df)

