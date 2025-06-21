from preguntas_completas import *
from variables import *

import random
import copy



# Define subsecuencias de preguntas basadas en la respuesta a la pregunta 2
secuencias_preguntas_cantidadHijos = {
    "1": [3, 4, 5],
    "2": [6, 7, 8, 9, 10, 11],
    "3": [12, 13, 14, 15, 16, 17, 18, 19, 20],
    "4": [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32]
}

# Lista explícita de preguntas a recorrer
preguntas_a_recorrer = [32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47]


preguntas_con_siguiente = [1, 2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 34, 40, 41, 43, 44, 46]



def generar_respuestas_aleatorias(pregunta_respuestas, secuencias_preguntas_cantidadHijos, cantidad):
    respuestas_aleatorias = []
    conteo_respuestas = 0
    for pregunta, datos in pregunta_respuestas.items():
        for respuesta_seleccionada in datos["respuesta"].keys():
            if respuesta_seleccionada not in secuencias_preguntas_cantidadHijos:
                print(f"Clave no encontrada en secuencias_preguntas_cantidadHijos: {respuesta_seleccionada}. Se omitirá esta opción.")
                continue
            subseccion = secuencias_preguntas_cantidadHijos[respuesta_seleccionada]
            for sub_idx in subseccion:
                sub_pregunta = pregunta_respuestas[sub_idx]
                sub_pregunta_texto = sub_pregunta["pregunta"]
                sub_opciones = sub_pregunta["respuesta"]
                
                sub_opciones_validas = {k: v for k, v in sub_opciones.items() if v > 0}
                
                if not sub_opciones_validas:
                    continue
                
                sub_respuesta_seleccionada = random.choices(
                    list(sub_opciones_validas.keys()),
                    weights=sub_opciones_validas.values(),
                    k=1
                )[0]
                
                pregunta_respuestas[sub_idx]["respuesta"][sub_respuesta_seleccionada] -= 1
                respuestas_aleatorias.append({sub_pregunta_texto: sub_respuesta_seleccionada})

                conteo_respuestas += 1
                
    return respuestas_aleatorias, conteo_respuestas

# Supongo que 'pregunta_respuestas', 'secuencias_preguntas_cantidadHijos', y 'preguntas_a_recorrer' están definidos
respuestas_aleatorias, conteo_respuestas = generar_respuestas_aleatorias(pregunta_respuestas, secuencias_preguntas_cantidadHijos, 344)




# Crear y abrir el archivo de texto
with open('respuestas.txt', 'w') as f:
    for idx, respuestas in enumerate(respuestas_aleatorias, 1):
        f.write(f"\nRespuestas ejecución {idx}:\n")
        for pregunta, respuesta in respuestas.items():
            f.write(f"Pregunta: {pregunta}\n")
            if isinstance(respuesta, list):
                f.write("Respuestas:\n")
                for r in respuesta:
                    f.write(f"  - {r}\n")
            else:
                f.write(f"Respuesta: {respuesta}\n")
        f.write("\n" + "="*50 + "\n")

# Crear y abrir el archivo de texto para los conteos
with open('conteo_respuestas.txt', 'w') as f:
    for pregunta, respuestas in conteo_respuestas.items():
        f.write(f"Pregunta: {pregunta}\n")
        for respuesta, conteo in respuestas.items():
            f.write(f"  Respuesta: {respuesta}, Conteo: {conteo}\n")
        f.write("\n" + "="*50 + "\n")