from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from pruebas import *
from bs4 import BeautifulSoup
import random
from preguntas_completas import *
import time

def procesar_datos(driver, respuestas):
    for pregunta, respuesta in respuestas.items():
        if isinstance(respuesta, list):
            for item in respuesta:
                print(f"Respondiendo: {item}")
                intentos = 0
                while intentos < 5:
                    try:
                        # elemento = driver.find_element(By.XPATH, f"//span[contains(text(), '{item}')]")
                        elemento = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f"//span[contains(text(), '{item}')]")))
                        elemento.click()
                        if item == "Enviar" or item == "Siguiente":
                            time.sleep(1)
                        break
                    except Exception as e:
                        print(f"Ocurrió un error al buscar el elemento: {e}")
                        intentos += 1
                        print(f"Reintentando... ({intentos} de 3 intentos)")
                        time.sleep(1)
                        if intentos == 5:
                            print("Se han agotado los intentos. Deteniendo el proceso.")
                            return
        else:
            print(f"Respondiendo: {respuesta}")
            intentos = 0
            while intentos < 5:
                try:
                    # elemento = driver.find_element(By.XPATH, f"//span[contains(text(), '{respuesta}')]")
                    elemento = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, f"//span[contains(text(), '{respuesta}')]")))
                    elemento.click()
                    if respuesta == "Enviar" or respuesta == "Siguiente":
                        time.sleep(1)
                    break
                except Exception as e:
                    print(f"Ocurrió un error al buscar el elemento: {e}")
                    intentos += 1
                    print(f"Reintentando... ({intentos} de 3 intentos)")
                    time.sleep(1)
                    if intentos == 5:
                        print("Se han agotado los intentos. Deteniendo el proceso.")
                        return
    print("\n" + "-"*40 + "\n")  # Separador entre diccionarios





# función para iniciar el servicio del WebDriver y abrir el navegador
def iniciar_navegador():
    # Configura el servicio del WebDriver
    service = Service('C:/Users/medin/Downloads/chromedriver-win64/chromedriver.exe')
    service.start()

    # Configura las opciones del WebDriver
    options = webdriver.ChromeOptions()

    # Crea el WebDriver con el servicio y las opciones configuradas
    driver = webdriver.Chrome(service=service, options=options)
    return driver, service

def responder_encuesta(url_encuesta, datos):
    # Agrega un contador para los diccionarios
    contador_diccionarios = 0

    # Recorre cada diccionario en la lista de datos
    for respuestas in datos:
        # Incrementa el contador de diccionarios
        contador_diccionarios += 1
        print(f"Procesando el diccionario {contador_diccionarios} de {len(datos)}")

        # Inicializa un contador para los intentos de procesamiento
        intentos = 0

        while intentos < 3:
            try:
                # Inicializa el WebDriver
                driver, service = iniciar_navegador()
                # Abre el formulario de Google Forms
                service.start()
                driver.get(url_encuesta)
                
                time.sleep(1)
                # Da clic en el botón siguiente
                next_button = driver.find_element(By.XPATH, "//span[contains(text(), 'Siguiente')]")
                next_button.click()
                time.sleep(1)

                # Procesa cada pregunta y su respuesta
                procesar_datos(driver, respuestas)

                # Cierra el navegador después de procesar todos los conjuntos de respuestas
                driver.quit()
                service.stop()
                time.sleep(1)

                # Si todo el procesamiento fue exitoso, reinicia el contador de intentos y sale del ciclo while
                intentos = 0
                break

            except Exception as e:
                # Imprime el error
                print(f"Ocurrió un error: {e}")
                # Incrementa el contador de intentos
                intentos += 1
                print(f"Reintentando... ({intentos} de 3 intentos)")

                # Si ya se han hecho 3 intentos, sale del ciclo while y pasa al siguiente diccionario
                if intentos == 3:
                    print("Se han agotado los intentos. Pasando al siguiente diccionario.")
                    break



# URL de la encuesta
url_encuesta = "https://docs.google.com/forms/d/e/1FAIpQLSdCl_2SUWVF6F89hDnDiikgrdLVkeW6wWZk2-AnQ3zHDnxPRg/formResponse"


respuestas_aleatorias = generar_respuestas_aleatorias(pregunta_respuestas, secuencias_preguntas_cantidadHijos, 344)



# Itera sobre cada diccionario en respuestas_aleatorias
for respuestas in respuestas_aleatorias:
    # Llama a la función responder_encuesta para procesar cada conjunto de respuestas
    responder_encuesta(url_encuesta, respuestas)

