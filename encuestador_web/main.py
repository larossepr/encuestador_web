import streamlit as st
# Page: Encuestador AMBI
st.set_page_config(
    page_title="Encuestador AMBI",
    page_icon="📋",
    layout="centered",
    initial_sidebar_state="collapsed"
)
st.title("🌿 Proyecto AMBI")
st.subheader("Bienvenido al sistema de encuestas ambientales.")
st.write("Por favor elija un nombre para crear la encuesta")
nombre = st.text_input("Nombre: ").strip().lower()
crear = st.button("Crear encuesta", )
if crear:
    if nombre:
        st.session_state["nombre_encuesta"] = nombre
        st.switch_page("pages/encuestador_web.py")
    else:
        st.warning("Por favor elija un nombre para la encuesta")



