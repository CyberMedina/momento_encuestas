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



def generar_respuestas_aleatorias(pregunta_respuestas, secuencias_preguntas_cantidadHijos, num_iteraciones):
    respuestas_totales = []
    conteo_respuestas = {}

    # Hacer una copia profunda del diccionario original para preservar las cantidades iniciales
    pregunta_respuestas_copia = copy.deepcopy(pregunta_respuestas)

    for _ in range(num_iteraciones):
        respuestas = {}
        finalizar_inmediatamente = False
        
        for idx, pregunta in pregunta_respuestas_copia.items():
            if finalizar_inmediatamente:
                break

            pregunta_texto = pregunta["pregunta"]
            opciones = pregunta["respuesta"]
            
            # Filtrar opciones con más de 0 respuestas disponibles
            opciones_validas = {k: v for k, v in opciones.items() if v > 0}
            
            # Si no hay opciones válidas, continuar con la siguiente pregunta
            if not opciones_validas:
                continue
            
            # Seleccionar una respuesta aleatoria basada en las cantidades disponibles
            respuesta_seleccionada = random.choices(
                list(opciones_validas.keys()), 
                weights=opciones_validas.values(), 
                k=1
            )[0]
            
            # Restar uno a la cantidad de la respuesta seleccionada
            pregunta_respuestas_copia[idx]["respuesta"][respuesta_seleccionada] -= 1
            
            # Agregar la respuesta seleccionada al nuevo diccionario
            respuestas[pregunta_texto] = respuesta_seleccionada

            # Actualizar el conteo de respuestas seleccionadas
            if pregunta_texto not in conteo_respuestas:
                conteo_respuestas[pregunta_texto] = {}
            if respuesta_seleccionada not in conteo_respuestas[pregunta_texto]:
                conteo_respuestas[pregunta_texto][respuesta_seleccionada] = 0
            conteo_respuestas[pregunta_texto][respuesta_seleccionada] += 1

            if idx in preguntas_con_siguiente:
                respuestas[f"Siguiente seccion{idx}"] = "Siguiente"
            
            # Verificar si la respuesta seleccionada es "No" para la clave 1
            if idx == 1:
                if respuesta_seleccionada == "No":
                    finalizar_inmediatamente = True
                    respuestas["Finalizar"] = "Enviar"
                continue
            
            # Si la pregunta es la 2, agregar la subsección correspondiente
            if idx == 2:
                subseccion = secuencias_preguntas_cantidadHijos[respuesta_seleccionada]
                for sub_idx in subseccion:
                    sub_pregunta = pregunta_respuestas_copia[sub_idx]
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
                    
                    pregunta_respuestas_copia[sub_idx]["respuesta"][sub_respuesta_seleccionada] -= 1
                    respuestas[sub_pregunta_texto] = sub_respuesta_seleccionada

                    if sub_idx in preguntas_con_siguiente:
                        respuestas[f"Siguiente seccion{sub_idx}"] = "Siguiente"
                    
                    # Actualizar el conteo de respuestas seleccionadas para la subsección
                    if sub_pregunta_texto not in conteo_respuestas:
                        conteo_respuestas[sub_pregunta_texto] = {}
                    if sub_respuesta_seleccionada not in conteo_respuestas[sub_pregunta_texto]:
                        conteo_respuestas[sub_pregunta_texto][sub_respuesta_seleccionada] = 0
                    conteo_respuestas[sub_pregunta_texto][sub_respuesta_seleccionada] += 1
                
                # No continuar con las preguntas principales después de seguir la subsección
                break

        # Inicializar un flag para verificar si debemos saltar a la pregunta 48
        saltar_a_pregunta_48 = False
        saltar_a_pregunta_49 = False
        saltar_a_pregunta_46 = False

        # Iterar sobre las preguntas en la lista explícita
        for idx in preguntas_a_recorrer:
            if finalizar_inmediatamente:
                break

            if saltar_a_pregunta_46 and idx in [44, 45]:
                continue

            if idx in preguntas_con_siguiente:
                if idx == 8:
                    print(f"SE ENCONTRÓ UNA PREGUNTA CON SIGUIENTE 8: {idx}")
                respuestas[f"Siguiente seccion{idx}"] = "Siguiente"

            # Si debemos saltar a la pregunta 48, actualizar el índice y procesar esa pregunta
            if saltar_a_pregunta_48:
                idx = 48

            if saltar_a_pregunta_49:
                idx = 49
            
            if saltar_a_pregunta_46:
                idx = 46
                saltar_a_pregunta_46 = False # Solo saltar una vez
                

            pregunta = pregunta_respuestas_copia[idx]

            pregunta_texto = pregunta["pregunta"]
            opciones = pregunta["respuesta"]

            # Filtrar opciones con más de 0 respuestas disponibles
            opciones_validas = {k: v for k, v in opciones.items() if v > 0}

            # Si no hay opciones válidas, continuar con la siguiente pregunta
            if not opciones_validas:
                continue

            # Si la pregunta es de selección múltiple, seleccionar todas las respuestas válidas
            if pregunta["tipo_pregunta"] == "seleccion_multiple":
                respuestas_seleccionadas = [k for k, v in opciones_validas.items() if v > 0]
                for respuesta in respuestas_seleccionadas:
                    pregunta_respuestas_copia[idx]["respuesta"][respuesta] -= 1
                respuestas[pregunta_texto] = respuestas_seleccionadas
                
                # Actualizar el conteo de respuestas seleccionadas para selección múltiple
                if pregunta_texto not in conteo_respuestas:
                    conteo_respuestas[pregunta_texto] = {}
                for respuesta in respuestas_seleccionadas:
                    if respuesta not in conteo_respuestas[pregunta_texto]:
                        conteo_respuestas[pregunta_texto][respuesta] = 0
                    conteo_respuestas[pregunta_texto][respuesta] += 1
            else:
                # Seleccionar una respuesta aleatoria basada en las cantidades disponibles
                respuesta_seleccionada = random.choices(
                    list(opciones_validas.keys()), 
                    weights=opciones_validas.values(), 
                    k=1
                )[0]

                # Restar uno a la cantidad de la respuesta seleccionada
                pregunta_respuestas_copia[idx]["respuesta"][respuesta_seleccionada] -= 1

                # Agregar la respuesta seleccionada al nuevo diccionario
                respuestas[pregunta_texto] = respuesta_seleccionada
                
                # Actualizar el conteo de respuestas seleccionadas
                if pregunta_texto not in conteo_respuestas:
                    conteo_respuestas[pregunta_texto] = {}
                if respuesta_seleccionada not in conteo_respuestas[pregunta_texto]:
                    conteo_respuestas[pregunta_texto][respuesta_seleccionada] = 0
                conteo_respuestas[pregunta_texto][respuesta_seleccionada] += 1

            # Si estamos en la pregunta 33 y la respuesta es "No", marcar para saltar a la pregunta 48
            if idx == 33 and respuesta_seleccionada == "No":
                saltar_a_pregunta_48 = True

            # Si estamos en la pregunta 39 y la respuesta es "No", marcar para saltar a la pregunta 49
            if idx == 39 and respuesta_seleccionada == "No":
                saltar_a_pregunta_49 = True

            # Si estamos en la pregunta 43, establecer el flujo de preguntas correspondiente
            if idx == 43:
                if respuesta_seleccionada == "No":
                    saltar_a_pregunta_46 = True

            
            # Si estamos en las preguntas 48 o 49, marcar para finalizar inmediatamente
            if idx == 48 or idx == 49:
                finalizar_inmediatamente = True

        if "Finalizar" not in respuestas:
            respuestas[f"Siguiente seccion{idx}"] = "Siguiente"
            respuestas["Finalizar"] = "Enviar"
        
        respuestas_totales.append(respuestas)

    return respuestas_totales, conteo_respuestas

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