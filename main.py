from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import random
import time
from preguntas_completas import pregunta_respuestas

# ---------- Generador de respuestas aleatorias ----------
def generar_respuestas_aleatorias(pregunta_respuestas, cantidad=3):
    datos_generados = []
    for _ in range(cantidad):
        respuestas_dict = {}
        for idx, pregunta_info in pregunta_respuestas.items():
            opciones = list(pregunta_info["respuesta"].items())
            ponderado = []
            for texto, peso in opciones:
                ponderado.extend([texto] * peso)
            if not ponderado:
                continue
            seleccion = random.choice(ponderado)
            respuestas_dict[pregunta_info["pregunta"]] = seleccion
        datos_generados.append(respuestas_dict)
    return datos_generados

# ---------- Proceso para responder preguntas + clic en "Siguiente" ----------
def procesar_datos(driver, respuestas):
    for pregunta, respuesta in respuestas.items():
        print(f"[DEBUG] Intentando responder la pregunta: {pregunta} con la respuesta: {respuesta}")
        intentos = 0
        while intentos < 3:
            try:
                xpath_respuesta = f"//span[normalize-space(text())='{respuesta}']"
                print(f"[DEBUG] Buscando elemento con XPATH: {xpath_respuesta}")
                elemento = WebDriverWait(driver, 2).until(
                    EC.element_to_be_clickable((By.XPATH, xpath_respuesta))
                )
                elemento.click()
                # time.sleep(random.uniform(1, 2)) # ¡Elimina o reduce!
                time.sleep(0.25) # suficiente para registrar el click

                # Escribir texto adicional si aplica
                for idx, info in pregunta_respuestas.items():
                    if info["pregunta"] == pregunta and respuesta.lower() == "si" and "respuesta_texto_si" in info:
                        texto_elegido = random.choice(info["respuesta_texto_si"])
                        print(f"[DEBUG] → Escribiendo texto adicional: {texto_elegido}")
                        try:
                            campo_texto = WebDriverWait(driver, 1.5).until(
                                EC.presence_of_element_located((By.XPATH, "//input[@type='text' and contains(@aria-label, 'respuesta')]"))
                            )
                            campo_texto.send_keys(texto_elegido)
                            time.sleep(0.1)
                        except Exception as e:
                            print(f"[DEBUG][⚠️] No se encontró el campo de texto: {e}")

                # Acción posterior
                accion = None
                for info in pregunta_respuestas.values():
                    if info["pregunta"] == pregunta:
                        accion = info.get("accion_post_pregunta", None)
                        break
                print(f"[DEBUG] Acción post-pregunta para '{pregunta}': {accion}")

                if accion == "siguiente":
                    try:
                        siguiente = WebDriverWait(driver, 1.5).until(
                            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Siguiente')]"))
                        )
                        siguiente.click()
                        time.sleep(0.2)
                    except Exception as e:
                        print(f"[DEBUG][⚠️] No se encontró el botón 'Siguiente': {e}")
                elif accion == "enviar":
                    try:
                        enviar = WebDriverWait(driver, 1.5).until(
                            EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Enviar')]"))
                        )
                        enviar.click()
                        time.sleep(0.2)
                    except Exception as e:
                        print(f"[DEBUG][⚠️] No se encontró el botón 'Enviar': {e}")

                break
            except Exception as e:
                print(f"[DEBUG][ERROR] Ocurrió un error al buscar '{respuesta}' para la pregunta '{pregunta}': {e}")
                intentos += 1
                print(f"[DEBUG] Reintentando... ({intentos} de 3 intentos)")
                time.sleep(0.5)
                if intentos == 3:
                    print(f"[DEBUG] Se han agotado los intentos para la respuesta '{respuesta}' de la pregunta '{pregunta}'.")
                    break
        print("\n" + "=" * 40 + "\n")
    print("[DEBUG] Fin de procesar_datos(), intentaremos enviar si hay botón disponible...")

# ---------- Iniciar navegador ----------
def iniciar_navegador():
    service = Service('C:/Users/medin/Downloads/chrome-win64/chromedriver.exe')
    options = Options()
    # Opcional: desactivar imágenes y animaciones para mayor velocidad
    prefs = {"profile.managed_default_content_settings.images": 2}
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(service=service, options=options)
    # Inyectar CSS para quitar animaciones (puede ayudar)
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
        var style = document.createElement('style');
        style.innerHTML = '* { transition: none !important; animation: none !important; }';
        document.head.appendChild(style);
        """
    })
    return driver, service

# ---------- Responder una encuesta completa ----------
def responder_encuesta(url_encuesta, datos):
    contador_diccionarios = 0
    for respuestas in datos:
        contador_diccionarios += 1
        print(f"\nProcesando diccionario {contador_diccionarios} de {len(datos)}")
        intentos = 0
        while intentos < 3:
            try:
                driver, service = iniciar_navegador()
                driver.get(url_encuesta)
                time.sleep(1.2) # puede reducirse si la página es rápida
                procesar_datos(driver, respuestas)

                # Enviar formulario si está disponible
                try:
                    enviar = WebDriverWait(driver, 1.5).until(
                        EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Enviar')]"))
                    )
                    enviar.click()
                    print("🚀 Formulario enviado exitosamente.\n")
                except:
                    print("⚠️ No se encontró el botón 'Enviar'. Puede que no haya terminado la encuesta.")

                driver.quit()
                service.stop()
                break
            except Exception as e:
                print(f"Ocurrió un error general: {e}")
                intentos += 1
                print(f"Reintentando... ({intentos} de 3)")
                time.sleep(0.7)
                if intentos == 3:
                    print("Saltando al siguiente diccionario...")