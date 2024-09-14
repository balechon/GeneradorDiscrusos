import streamlit as st
from modules.speech_generator_rag import SpeechGenerator
from modules.speech_generator_phi import generate_speech, load_model, clear_gpu_memory

clear_gpu_memory()

st.set_page_config(page_title="Generador de Discursos")
st.title("Generador de Discursos")


@st.cache_resource
def get_speech_generator():
    return SpeechGenerator()


@st.cache_resource
def get_phi_models():
    model, tokenizer = load_model()
    return model, tokenizer


generator = get_speech_generator()
phi_model, phi_tokenizer = get_phi_models()

# Inicializar el estado de la sesión si no existe
if 'clear_text' not in st.session_state:
    st.session_state.clear_text = False


# Función para manejar el borrado de texto
def clear_text():
    st.session_state.clear_text = True


# Añadir menú desplegable para seleccionar el modelo
modelo_seleccionado = st.selectbox(
    "Selecciona el modelo de generación:",
    ("RAG LLAMA Model", "Fine-Tuned PHI-3 Model"),
)

# Cambiar el texto del input según el modelo seleccionado
input_label = "Introduce el tema del discurso:" if modelo_seleccionado == "RAG LLAMA Model" else "Ingresa el inicio de tu discurso, el modelo lo completará:"

# Crear una columna para el input de texto y otra para el botón de borrar
col1, col2 = st.columns([3, 1])

with col1:
    # Si clear_text es True, borra el texto y restablece la bandera
    if st.session_state.clear_text:
        st.session_state.topic_input = ""
        st.session_state.clear_text = False

    topic = st.text_area(input_label, key="topic_input", height=150)

with col2:
    st.button("Borrar texto", on_click=clear_text)

if st.button("Generar Discurso"):
    if topic:
        with st.spinner("Generando el discurso... Por favor, espera."):
            speech = generator.generate_speech(topic) if modelo_seleccionado == "RAG LLAMA Model" else generate_speech(
                phi_model, phi_tokenizer, topic)
        st.session_state.speech = speech
        st.subheader("Discurso Generado:")
        st.write(speech)
    else:
        st.warning("Por favor, introduce un tema o inicio del discurso.")

if 'speech' in st.session_state:
    st.download_button(
        label="Descargar Discurso",
        data=st.session_state.speech,
        file_name="discurso_generado.txt",
        mime="text/plain"
    )