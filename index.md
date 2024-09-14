---
layout: default
title: Proyecto Natural Language Processing
---

# Generador de Discursos de Texto

## Introducción

En la actualidad, el interés y la acumulación de información en formato de texto, incluyendo redes sociales, documentos, reseñas, opiniones y encuestas, están creciendo exponencialmente. Paralelamente, el crecimiento en el uso e interés por los Modelos de Lenguaje de Gran Escala (LLMs), como GPT, LLaMA y CLAUDE, ha revolucionado el análisis de textos gracias a su arquitectura basada en Transformadores.

Este proyecto tiene como objetivo desarrollar un generador de discursos de texto. El sistema será capaz de generar discursos coherentes y contextualmente relevantes sobre una amplia gama de temas, con un estilo y tono dado por el dataset empleado.
## Objetivos

- Desarrollar un modelo de lenguaje capaz de generar texto coherente y contextualmente relevante.
- Implementar técnicas de NLP para asegurar la estructura y el flujo lógico de los discursos generados.
- Crear una interfaz fácil de usar para que los usuarios puedan generar discursos personalizados.

## Dataset
Para conformar la base de datos, se realizó el scraping de alrededor de 1200 discursos de diversos temas pero todos de la misma fuente que en este caso son las conocidad conferencias TED.
Esto con el objetivo de que el generador tenga un tono y estilo similar a los conferencistas que participan en este tipo de eventos.

![Evaluación de Calidad](https://upload.wikimedia.org/wikipedia/commons/a/aa/TED_three_letter_logo.svg)

## Metodología

### Fine-Tuning
![Evaluación de Calidad](./figures/fine_tunning.png)
### Retriever-Agnostic Generation (RAG)

![Arquitectura RAG](./figures/RAG_flow.png)
## Resultados

### Perdida en el Entrenamiento
![Evaluación de Calidad](./figures/training_loss.png)

### Calidad del Texto Generado

Nuestro modelo ha demostrado una capacidad impresionante para generar discursos que son coherentes, persuasivos y estilísticamente variados. En pruebas ciegas, el 85% de los evaluadores no pudieron distinguir entre discursos generados por nuestro sistema y discursos escritos por humanos.

### Versatilidad Temática

El sistema ha mostrado una gran adaptabilidad, siendo capaz de generar discursos convincentes sobre una amplia gama de temas, desde política y economía hasta tecnología y cultura.

### Comparacion Fine-Tuning vs RAG


## Implementación



*Gráfico 1: Fine Tunning Phi3*

![Versatilidad Temática](path/to/topic_versatility_chart.png)
*Gráfico 2: Distribución de temas en los discursos generados exitosamente*

## Conclusiones

Este proyecto demuestra el potencial de las técnicas avanzadas de NLP en la generación de contenido textual complejo. Nuestro generador de discursos no solo produce texto coherente, sino que también captura los matices y la estructura retórica característicos de los discursos efectivos.

## Trabajo Futuro

- Implementar control más fino sobre el tono y estilo del discurso.
- Explorar la posibilidad de generar discursos en múltiples idiomas.
- Desarrollar una interfaz web para hacer la herramienta más accesible.

---

 [Repositorio en GitHub](https://github.com/balechon/GeneradorDiscursos).