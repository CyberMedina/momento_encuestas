from main import responder_encuesta, generar_respuestas_aleatorias
from preguntas_completas import pregunta_respuestas
import random


# URL de tu formulario
url_encuesta = "https://docs.google.com/forms/d/e/1FAIpQLScHOHxlbw0szdomX4GwYQ20fesOvAvKuvJPtS0J0ihOgdprhQ/viewform?usp=preview"

# Generar respuestas aleatorias
respuestas_aleatorias = generar_respuestas_aleatorias(pregunta_respuestas, cantidad=5)

# Ejecutar
responder_encuesta(url_encuesta, respuestas_aleatorias)
