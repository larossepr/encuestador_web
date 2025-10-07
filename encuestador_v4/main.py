import streamlit as st
import os
import pandas as pd
import time
# Configura la pagina con titulo que aparece, icono, su disposicion y el estado de la barra lateral
st.set_page_config(
    page_title= "Sistema de Encuestas Ambientales",
    page_icon= "",
    layout="wide",
    initial_sidebar_state="collapsed"
) 
# Textos de la pagina
st.title("🌿 Proyecto AMBI")
st.header("Bienvenido al sistema de encuestas ambientales")
st.subheader("Por favor elija un nombre de proyecto para crear la encuesta")
#Input de el usuario
nombre = st.text_input("Nombre del Proyecto:").lower().strip()
st.caption("Al momento de crear encuesta se descargara un archivo CSV vital para guardar los datos de la encuesta")
# Boton 
crear = st.button("Crear encuesta")


# Verifica si la encuesta existe en disco, si no, la crea, si existe se leen los contenidos y se pasan a DataFrame

encuesta = f"{nombre}_encuesta.csv"
if crear:
    if nombre:
        if os.path.exists(encuesta):
            with open(encuesta, "r") as file:
                st.session_state["datos_encuesta"] = []
                st.session_state["nombre_del_proyecto"] = nombre
                st.switch_page("pages/encuesta.py")
                
        else:
            with st.spinner("Creando nueva encuesta"):
                with open(encuesta, "w", encoding="utf-8") as file:
                    file.write("Nombre,Telefono,Email,Direccion," \
                    "Genero,Edad,Estado Civil,Nivel Educativo,Profesion," \
                    "Sector Laboral,Lugares de Ocio,Organizaciones," \
                    "Posee Tierra,Posee Vivienda,Conoce el Proyecto," \
                    "Proyecto Positivo,Calidad del Aire,Calidad del Agua," \
                    "Calidad de la Tierra,Calidad del Paisaje," \
                    "Incidencia en el Paisaje,Afecta a los Animales,Afecta a las Plantas," \
                    "Riesgo de Inundacion,Contribuye al Desarrollo,Crea Empleo," \
                    "Es Nativo,Reside en la Comunidad,Viene por Temporada\n")
                    time.sleep(1)
                    st.success("Encuesta creada")
                
                st.session_state["datos_encuesta"] = []
                st.session_state["nombre_del_proyecto"] = nombre
                st.switch_page("pages/encuesta.py")
    else:
        st.warning("Por favor elige un nombre")  