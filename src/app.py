import streamlit as st
from modules.speech_generator_rag import SpeechGenerator
from modules.speech_generator_phi import generate_speech, load_model
st.set_page_config(page_title="Generador de Discursos")
st.title("Generador de Discursos")

@st.cache_resource
def get_speech_generator():
    return SpeechGenerator()
@st.cache_models
def get_phi_models():
    model, tokenizer = load_model()
    return model, tokenizer


generator = get_speech_generator()
phi_model, phi_tokenizer = get_phi_models()

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
                speech = generate_speech(phi_model, phi_tokenizer, topic)
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