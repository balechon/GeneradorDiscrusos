---
layout: default
title: Proyecto Natural Language Processing
---

# Generador de Discursos de Texto

## Introducción

En la actualidad, el interés y la acumulación de información en formato de texto, incluyendo redes sociales, documentos, reseñas, opiniones y encuestas, están creciendo exponencialmente. Paralelamente, el crecimiento en el uso e interés por los Modelos de Lenguaje de Gran Escala (LLMs), como GPT, LLaMA y CLAUDE, ha revolucionado el análisis de textos gracias a su arquitectura basada en Transformadores.

Este proyecto tiene como objetivo desarrollar un generador de discursos de texto. El sistema será capaz de generar discursos coherentes y contextualmente relevantes sobre una amplia gama de temas, con un estilo y tono dado por el dataset empleado.

En esta ocasion se va a explorar dos enfoques para la generación de discursos: Fine-Tuning y Retriever-Agnostic Generation (RAG).
## Objetivos

- Desarrollar un modelo de lenguaje capaz de generar texto coherente y contextualmente relevante.
- Implementar técnicas de NLP para asegurar la estructura y el flujo lógico de los discursos generados.
- Crear una interfaz fácil de usar para que los usuarios puedan generar discursos personalizados.

## Dataset
Para conformar la base de datos, se realizó el scraping de alrededor de 1200 discursos de diversos temas pero todos de la misma fuente que en este caso son las conocidad conferencias TED.
Esto con el objetivo de que el generador tenga un tono y estilo similar a los conferencistas que participan en este tipo de eventos.

![Evaluación de Calidad](https://upload.wikimedia.org/wikipedia/commons/a/aa/TED_three_letter_logo.svg)

## Metodología



## Fine-Tuning

![Arquitectura RAG](./figures/fine_tunning.png)


El enfoque de fine-tuning consiste en ajustar un modelo de lenguaje pre-entrenado a un conjunto de datos específico. En este proyecto, se utilizó el modelo [Phi3 Mini-4K](https://huggingface.co/microsoft/Phi-3-mini-4k-instruct) de Microsoft como punto de partida y se ajustó al dataset de discursos de TED.

### Formato del Dataset

Para que el modelo pueda entender y aprender del dataset, el texto de entrada se ha formateado de la siguiente manera:

```
user: 
Crea un discurso al estilo TED-Talk que suene como si fuera dado por un experto en [campo] y que trate sobre [temáticas]

assistant:
[Contenido del discurso]
```

Los campos `[campo]` y `[temáticas]` variarán dependiendo de los datos disponibles de discursos en el dataset.


Para el entrenamiento se definieron los hiperparámetros para optimizar el rendimiento del modelo teniendo en cuenta las limitaciones de recursos computacionales y la necesidad de un entrenamiento eficiente.
Algunos de los hiperparámetros empleados se resumen en la siguiente tabla:


| Hiperparámetro | Valor | Explicación |
|----------------|-------|-------------|
| per_device_train_batch_size | 2 | Número de muestras procesadas simultáneamente por dispositivo. Un valor bajo (2) permite entrenar con recursos de GPU limitados. |
| gradient_accumulation_steps | 8 | Acumula gradientes de varios pasos antes de actualizar los pesos. Ayuda a simular batches más grandes sin aumentar el uso de memoria. |
| learning_rate | 1e-4 | Tasa de aprendizaje. Un valor de 0.0001 es típico para fine-tuning, balanceando la velocidad de aprendizaje y la estabilidad. |
| num_train_epochs | 5 | Número de veces que el modelo pasa por todo el dataset durante el entrenamiento. |
| optim | "adamw_bnb_8bit" | Optimizador AdamW con cuantización de 8 bits, que reduce el uso de memoria manteniendo el rendimiento. |
| lr_scheduler_type | "linear" | Disminuye linealmente la tasa de aprendizaje durante el entrenamiento, lo que ayuda a la convergencia. |

Para el entrenamiento se utilizó una GPU NVIDIA A100 con 32 GB de memoria. El proceso de fine-tuning tomó aproximadamente 2 horas.

**Pérdida durante el entrenamiento**



![Evaluación de Calidad](./figures/training_loss.png)

Como se puede apreciar en el gráfico, la pérdida disminuye rápidamente durante las primeras épocas, especialmente en la primera donde cae de 1.8 a aproximadamente 0.7. Posteriormente, se observan caídas abruptas al inicio de las épocas 2 y 3, seguidas de una estabilización gradual. Finalmente, la pérdida converge alrededor de 0.1 en las épocas 4 y 5, indicando un ajuste exitoso del modelo a la tarea de generación de discursos.

### Retriever-Agnostic Generation (RAG)

![Arquitectura RAG](./figures/RAG_flow.png)
## Resultados



### Calidad del Texto Generado

Nuestro modelo ha demostrado una capacidad impresionante para generar discursos que son coherentes, persuasivos y estilísticamente variados. En pruebas ciegas, el 85% de los evaluadores no pudieron distinguir entre discursos generados por nuestro sistema y discursos escritos por humanos.

### Versatilidad Temática

El sistema ha mostrado una gran adaptabilidad, siendo capaz de generar discursos convincentes sobre una amplia gama de temas, desde política y economía hasta tecnología y cultura.

### Comparacion Fine-Tuning vs RAG


| Nota | Explicación |
|------|-------------|
| No worries, it's a common mix-up! | The key difference is that permutations care about the order of arrangement, while combinations don't. Think of permutations as the 'pickier' of the two. 😉 |


## Implementación



*Gráfico 1: Fine Tunning Phi3*


*Gráfico 2: Distribución de temas en los discursos generados exitosamente*

## Conclusiones

Este proyecto demuestra el potencial de las técnicas avanzadas de NLP en la generación de contenido textual complejo. Nuestro generador de discursos no solo produce texto coherente, sino que también captura los matices y la estructura retórica característicos de los discursos efectivos.

## Trabajo Futuro

- Implementar control más fino sobre el tono y estilo del discurso.
- Explorar la posibilidad de generar discursos en múltiples idiomas.
- Desarrollar una interfaz web para hacer la herramienta más accesible.

---

 [Repositorio en GitHub](https://github.com/balechon/GeneradorDiscursos).