import streamlit as st
from modules.speech_generator import SpeechGenerator

st.set_page_config(page_title="Generador de Discursos")
st.title("Generador de Discursos")

@st.cache_resource
def get_speech_generator():
    return SpeechGenerator()

generator = get_speech_generator()

def clear_session():
    for key in list(st.session_state.keys()):
        del st.session_state[key]

# Añadir menú desplegable para seleccionar el modelo
modelo_seleccionado = st.selectbox(
    "Selecciona el modelo de generación:",
    ("RAG LLAMA Model", "Fine-Tuned PHI-3 Model"),
)

topic = st.text_input("Introduce el tema del discurso:", key="topic_input")

col1, col2 = st.columns(2)

if col1.button("Generar Discurso"):
    if topic:
        with st.spinner("Generando el discurso... Por favor, espera."):
            if modelo_seleccionado == "RAG LLAMA Model":
                speech = generator.generate_speech(topic)
            else:
                # Aquí irá la lógica para el Modelo 2
                speech = "Este es un placeholder para el Modelo 2. Implementa la lógica específica aquí."
        st.session_state.speech = speech
        st.subheader("Discurso Generado:")
        st.write(speech)
    else:
        st.warning("Por favor, introduce un tema para el discurso.")

if 'speech' in st.session_state:
    st.download_button(
        label="Descargar Discurso",
        data=st.session_state.speech,
        file_name="discurso_generado.txt",
        mime="text/plain"
    )