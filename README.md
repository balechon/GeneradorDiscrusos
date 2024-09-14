# Generador de Discursos

## Descripción
Este proyecto presenta un generador de discursos basado en LLMs, usando RAG y Fine-Tuning.
## Características
- RAG esta implementado con LLAMA3
- Fine-Tuning con Phi3
- Aplicación para generar discursos

## Configuración
1. Es necesario tener instalado las librerias de Python que se encuentran en el archivo `requirements.txt`. Para instalarlas, ejecutar el siguiente comando:
```bash
pip install -r requirements.txt
```

2. Para la correcta ejecucion del modelo RAG, se necesita usar una base vectorial, en este proyecto se ha implementado mediante Pinecone. Para ello, es necesario tener una cuenta en Pinecone y ejecutar el archivo `/config/pinecone_db_config.py`.

3. Recuerde especificar las API keys en el archivo `.env` siguiendo el formato del archivo `.env.example`.

## Licencia
MIT

## Contacto
balechon96@gmail.com
