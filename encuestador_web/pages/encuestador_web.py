import streamlit as st
import pandas as pd
import io
import os
import time
import streamlit.components.v1 as components
# Page: Encuesta
st.set_page_config(
    page_title="Encuesta",
    page_icon="📋",
    layout="centered",
    initial_sidebar_state="collapsed"
)
# Inicializacion del Almacenamiento
if "nombre_encuesta" not in st.session_state:
    st.warning("⚠️ No se ha definido un nombre para la encuesta. Vuelve a la página principal")
    time.sleep(1.5)
    st.switch_page("main.py")

nombre = st.session_state["nombre_encuesta"]
nombre = nombre.lower().strip()
proyecto = nombre.title()

if f"{nombre}_resultados_acumulativos" not in st.session_state:
    if os.path.exists(f"{nombre}_resultados_encuesta.csv"):
        st.session_state[f"{nombre}_resultados_acumulativos"] = pd.read_csv(f"{nombre}_resultados_encuesta.csv").to_dict(orient="records")
    
    else:
        st.session_state[f"{nombre}_resultados_acumulativos"] = []
if "form_id" not in st.session_state:
    st.session_state["form_id"] = 0


# *Funcion*Obtiene los datos acumulados en la sesion y crea un pdf con ellos
def obtener_datos_csv():

    if not st.session_state[f"{nombre}_resultados_acumulativos"]:
        return "".encode()

    df_final = pd.DataFrame(st.session_state[f"{nombre}_resultados_acumulativos"])
    csv_buffer = io.StringIO()
    df_final.to_csv(csv_buffer, index=False)
    return csv_buffer.getvalue().encode()

# Titulo y Subtitulo
st.title(f"Analisis de Interesados del proyecto {proyecto}")
st.subheader("Por favor, contesta las siguientes preguntas.")

# Formulario de Encuesta
form = st.empty()
with form.form(key=f"encuesta_form_{st.session_state.form_id}"):
    genero = st.radio("Genero:", ["Masculino", "Femenino"], horizontal=True)
    edad = st.radio("Edad:", ["<18", "18-25", "26-35", "36-45", "46-60", "60+"], horizontal=True)
    estado_civil = st.radio("Estado Civil:", ["Soltero", "Casado", "Divorciado", "Viudo"], horizontal=True)
    nivel_educativo = st.radio("Nivel Educativo:", ["Basico", "Intermedio", "Bachiller", "Superior"], horizontal=True)
    profesion = st.text_input("Profesion :")
    sector_laboral = st.radio("Sector Laboral:", ["Publico", "Privado", "Independiente", "Desempleado"], horizontal=True)
    ocio = ["Bares", "Colmados", "Galleras", "Play", "Billar", "Playa o rio"]
    lugares_ocio = st.multiselect("Lugares que visita la gente en la comunidad para divertirse    || Elija uno o mas lugares ||", ocio, placeholder="Elija uno o mas lugares")
    orgs = ["Iglesia", "Grupo Deportivo", "Club", "Asociacion de Agricultores", "Asociacion de Comerciantes", "Asociacion de Ganaderos", "Otra"]
    organizacion = st.multiselect("Organizaciones a las que pertenece    || Elija una o mas organizaciones ||", orgs, placeholder="Elija una o mas organizaciones")
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
    st.write("Podria darnos su nombre y direccion?")
    nombre_completo = st.text_input("Nombre Completo: ")
    direccion = st.text_input("Direccion: ")

    submitted = st.form_submit_button("Enviar Encuesta")



    

    # Lo que sucede cuando se pulsa enviar encuesta
if submitted:
    datos_encuesta = {
        "Nombre": nombre_completo,
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
    st.session_state[f"{nombre}_resultados_acumulativos"].append(datos_encuesta)
    df = pd.DataFrame(st.session_state[f"{nombre}_resultados_acumulativos"])
    df.to_csv(f"{nombre}_resultados_encuesta.csv", index=False)
    st.success("Gracias por completar la encuesta! Reiniciando formulario")
    time.sleep(1.5)
    st.session_state["form_id"] += 1
    form.empty()
    st.rerun()
    

st.markdown("---")
    #boton para descargar los datos //Beta//
if st.button("Descargar Resultados en CSV"):
    if st.session_state[f"{nombre}_resultados_acumulativos"]:
        csv_data = obtener_datos_csv()

        st.download_button(
            label="Pulsa para confirmar descarga",
            data=csv_data,
            file_name=f"{nombre}_resultados_de_analisis_de interesados.csv",
            mime="text/csv"
        )
    else:
        st.warning("No hay datos para descargar. Envia una encuesta primero!")


