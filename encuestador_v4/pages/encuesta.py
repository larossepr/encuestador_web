import streamlit as st
import os
import pandas as pd
import time
# Configura la pagina con titulo que aparece, icono, su disposicion y el estado de la barra lateral
st.set_page_config(
    page_title= "Encuesta especifica",
    page_icon= "",
    layout="wide",
    initial_sidebar_state="collapsed"
) 
# Datos de la main page que se usan en esta
if "nombre_del_proyecto" not in st.session_state:
    st.warning("⚠️ No se ha definido un nombre para la encuesta. Vuelve a la página principal")
    time.sleep(1.5)
    st.switch_page("main.py")
proyecto = st.session_state["nombre_del_proyecto"].title()
nombre = st.session_state["nombre_del_proyecto"]
#ruta a guardar el csv
encuesta = f"{nombre}_encuesta.csv"
# Titulo y Subtitulo
st.title(f"Analisis de Interesados del proyecto {proyecto}")
st.subheader("Por favor, contesta las siguientes preguntas.")
# Groso del formulario
form = st.empty()
with form.form("Analisis de interesados"):
    genero = st.radio("Genero:", ["Masculino", "Femenino"], horizontal=True)
    edad = st.radio("Edad:", ["<18", "18-25", "26-35", "36-45", "46-60", "60+"], horizontal=True)
    estado_civil = st.radio("Estado Civil:", ["Soltero", "Casado", "Divorciado", "Viudo"], horizontal=True)
    nivel_educativo = st.radio("Nivel Educativo:", ["Basico", "Intermedio", "Bachiller", "Superior"], horizontal=True)
    profesion = st.text_input("Profesion :")
    sector_laboral = st.radio("Sector Laboral:", ["Publico", "Privado", "Independiente", "Desempleado"], horizontal=True)
    ocio = ["Bares", "Colmados", "Galleras", "Play", "Billar", "Playa o rio"]
    lugares_ocio = st.multiselect("Lugares que visita la gente visita en la comunidad para divertirse  |  *Elija uno o mas lugares*", ocio, placeholder="Elija uno o mas lugares")
    st.caption("Elija uno o mas lugares")
    orgs = ["Iglesia", "Grupo Deportivo", "Club", "Asociacion de Agricultores", "Asociacion de Comerciantes", "Asociacion de Ganaderos", "Otra"]
    organizacion = st.multiselect("Organizaciones a las que pertenece  |  *Elija una o mas organizaciones*", orgs, placeholder="Elija una o mas organizaciones")
    st.caption("Elija una o mas organizaciones")
    tierra = st.radio("Posee usted tierra?", ["Si", "No"], horizontal=True, index=1)
    vivienda = st.radio("Posee usted vivienda?", ["Si", "No"], horizontal=True, index=1)
    exitencia = st.radio(f"Sabia usted de la existencia del proyecto {proyecto}?", ["Si", "No"], horizontal=True, index=0)
    positividad = st.radio(f"Cree usted que las operaciones del proyecto {proyecto} son positivas para la comunidad?", ["Si", "No"], horizontal=True, index=0)
    st.write("En terminos ambientales, califique los siguientes campos: ")
    calidad_aire = st.radio("La calidad del Aire es:", ["Buena", "Regular", "Mala"], horizontal=True)
    calidad_agua = st.radio("La calidad del Agua es:", ["Buena", "Regular", "Mala"], horizontal=True)
    calidad_tierra = st.radio("La calidad del Tierra es:", ["Buena", "Regular", "Mala"], horizontal=True)
    calidad_paisaje = st.radio("La calidad del Paisaje es:", ["Buena", "Regular", "Mala"], horizontal=True)
    incidencia_paisaje = st.radio(f"Piensa usted que las actividades del proyecto {proyecto}, tienen incidencia sobre el paisaje?", ["Lo Mejorara", "Lo Empeorara", "No tendra Incidencia"], horizontal=True, index=0)
    incidencia_animales = st.radio(f"Piensa usted que las actividades del proyecto {proyecto}, afectan a los animales", ["Si", "No"], horizontal=True, index=1)
    incidencia_plantas = st.radio(f"Piensa usted que las actividades del proyecto {proyecto}, afectan a los arboles y las plantas?", ["Si", "No"], horizontal=True, index=1)
    inundacion = st.radio("Piensa usted que esta zona podria inundarse por algun rio o tsunami del mar?", ["Si", "No"], horizontal=True, index=1)
    desarrollo = st.radio(f"Piensa usted que las actividades del proyecto {proyecto}, contribuyen al desarollo de la comunidad?", ["Si", "No"], horizontal=True, index=0)
    empleo = st.radio(f"Piensa usted que las actividades del proyecto {proyecto}, ayudan a la creacion de empleo?", ["Si", "No"], horizontal=True, index=0)
    natividad = st.radio("Es usted nativo de aqui?", ["Si", "No"], horizontal=True, index=0)
    reside = st.radio("Reside usted en la comunidad?", ["Si", "No"], horizontal=True, index=0)
    temporada = "N/A"
    if reside == "No":
        temporada = st.radio("Viene por temporada?", ["Si", "No"], horizontal=True, index=1)
    st.write("Podria darnos mas informacion sobre usted?")
    nombre_completo = st.text_input("Nombre Completo: ")
    telefono = st.text_input("Telefono: ")
    email = st.text_input("Correo electronico: ")
    direccion = st.text_input("Direccion: ")

    #Boton de enviar formulario
    submitted = st.form_submit_button("Enviar encuesta")
    #Lo que pasa al pulsar el boton
if submitted:
    #diccionario con todas las respuestas del formulario
    datos_encuesta = {
        "Nombre": nombre_completo,
        "Telefono": telefono,
        "Email": email,
        "Direccion": direccion,
        "Genero": genero,
        "Edad": edad,
        "Estado Civil": estado_civil,
        "Nivel Educativo": nivel_educativo,
        "Profesion": profesion,
        "Sector Laboral": sector_laboral,
        "Lugares de Ocio": ",".join(lugares_ocio),
        "Organizaciones": ",".join(organizacion),
        "Posee Tierra": tierra,
        "Posee Vivienda": vivienda,
        "Conoce el Proyecto": exitencia,
        "Proyecto Positivo": positividad,
        "Calidad del Aire": calidad_aire,
        "Calidad del Agua": calidad_agua,
        "Calidad de la Tierra": calidad_tierra,
        "Calidad del Paisaje": calidad_paisaje,
        "Incidencia en el Paisaje": incidencia_paisaje,
        "Afecta a los Animales": incidencia_animales,
        "Afecta a las Plantas": incidencia_plantas,
        "Riesgo de Inundacion": inundacion,
        "Contribuye al Desarrollo": desarrollo,
        "Crea Empleo": empleo,
        "Es Nativo": natividad,
        "Reside en la Comunidad": reside,
        "Viene por Temporada": temporada
    }
    
    #convertir las respuestas del formulario a DataFrame
    df = pd.DataFrame([datos_encuesta])
    #pasar el DataFrame a CSV y anadir las respuestas sin borrar nada de lo existente
    df.to_csv(encuesta, mode="a", index=False, header=False, encoding="utf-8")
    #Visualizacion de formulario completado
    st.success("Gracias por completar la encuesta, el formulario se reiniciara, no hace falta volver a rellenarlo...")
    time.sleep(5)
    form.empty()
    st.rerun()
st.markdown("---")
    #boton para descargar los datos //Beta//
with open(encuesta, "r", encoding="utf-8") as file:
    csv_data = file.read().encode("utf-8")
if st.button("Descargar Resultados en CSV"):
    st.download_button(
    label="Pulsa para confirmar descarga",
    data=csv_data,
    file_name=f"{nombre}_resultados_de_analisis_de interesados.csv",
    mime="text/csv"
    )

    
