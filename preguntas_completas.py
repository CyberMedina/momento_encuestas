from variables import *

pregunta_respuestas = {

     1:{
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Posee actualmente un vehículo?",
        "respuesta": {
            "Sí": 350,
            "No": 30,
        },
        "accion_post_pregunta": "siguiente"  # ← aquí
    },
    2: {  
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Cuál es su edad?",
        "respuesta": {
            "Menor de 18": 0,
            "18-25": 95,
            "26-35": 150,
            "36-45": 50,
            "46-60": 45,
            "Mayor de 60": 10,
         }
     },
    3: {
        "tipo_pregunta" : una_opcion, 
        "pregunta": "Sexo",
        "respuesta": {
            "Masculino": 290,
            "Femenino": 60,
            "Otro": 0,
            "Prefiero no decirlo": 0,
        }
    },
    
    4:{
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Cuál es su ocupación?",
        "respuesta": {
            "Dueño de un vehículo particular": 160,
            "Mecánico o técnico automotriz": 170,
            "Dueño o trabajador de taller": 10,
            "Gerente de flota o transporte": 10,
            "Otro": 0,
        }
    },

    5:{
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Qué tipo de vehículo utiliza con mayor frecuencia?",
        "respuesta": {
            "Automóvil": 160,
            "Motocicleta": 170,
            "Camioneta": 10,
            "Vehículo pesado": 10,
            "Otro": 0,
        },
        "accion_post_pregunta": "siguiente"  # ← aquí
    },

    6: {
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Ha utilizado alguna vez un software o aplicación para controlar el mantenimiento de su vehículo?",
        "respuesta" : {
            "Sí" : 101,
            "No" : 249,
        },
    },

    7:{
        "tipo_pregunta" : una_opcion,
        "pregunta": "Actualmente, ¿utiliza alguna herramienta o sistema para llevar un registro de mantenimiento?",
        "respuesta": {
            "Sí, digital (app o software)": 101,
            "Sí, manual (libreta, notas)": 19,
            "Ninguna": 230,
        }
    },
    8:{
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Cuánto estaría dispuesto a pagar por una aplicación que le recomiende el aceite ideal y cuándo cambiarlo?",
        "respuesta": {
            "Menos de $2 mensuales": 88,
            "Entre $2 y $5 mensuales": 175,
            "Entre $5 y $10 mensuales": 52,
            "Prefiero versión gratuita con anuncios": 35,
        },
        "accion_post_pregunta": "siguiente"  # ← aquí
    },

    9:{
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Le interesaría probar una aplicación de mantenimiento preventivo como OilWise?",
        "respuesta": {
            "Sí": 200,
            "No": 120,
            "Tal vez": 30,
        }
    },

    10: {
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Qué características considera más útiles en una app de mantenimiento vehicular?",
        "respuesta" : {
            "Recordatorio automático de cambio de aceite" : 80,
            "Registro de mantenimiento general" : 80,
            "Historial del vehículo" : 100,
            "Comparador de tipos de aceite" : 15,
            "Asistente con inteligencia artificial" : 50,
            "Otras" : 25,
        },
        "accion_post_pregunta": "siguiente"  # ← aquí
    },

    11: {
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Conoce o ha oído hablar de apps como Vehic, CARFAX Car Care App, Mobil Serv Oil Analysis?",
        "respuesta" : {
            "Sí" : 320,
            "No" : 30,
        }
    },

    12: {
     "tipo_pregunta" : una_opcion,
     "pregunta": "¿Qué medios ha utilizado para conocer este tipo de software?",
     "respuesta" : {
        "Recomendación de otros" : 88,
        "Anuncios en redes sociales" : 88,
        "Búsqueda en Google o YouTube" : 100,
        "Ferias/Distribuidores automotrices" : 44,
        "Nunca he buscado este tipo de software" : 30,
        }
    },

    13:{
         "tipo_pregunta" : una_opcion,
         "pregunta": "¿Dónde buscaría un software de este tipo si lo necesitara?",
         "respuesta": {
             "Play Store / App Store": 60,
             "Google": 30,
             "Recomendación de taller": 70,
             "Redes sociales": 190,
             "Otro": 0,
         },
        "accion_post_pregunta": "siguiente"  # ← aquí
     },

    14: {
         "tipo_pregunta" : una_opcion,
         "pregunta": "¿Considera justo pagar por una aplicación que le ayude a ahorrar en mantenimientos innecesarios?",
         "respuesta" : {
             "Sí": 200,
             "No": 50,
             "Depende del precio": 100,
         }
     },

    15: {
     "tipo_pregunta" : una_opcion,
     "pregunta": "¿Qué modelo de pago preferiría?",
      "respuesta" : {
          "Único pago vitalicio": 10,
          "Pago mensual" : 160,
          "Pago anual" : 20,
          "Versión gratuita con publicidad" : 150,
          "Otro": 0,
      }
    },

     16: {
         "tipo_pregunta" : una_opcion,
         "pregunta": "¿Cuál sería un precio razonable para una app como OilWise?",
         "respuesta": {
             "Menos de $1.99": 88,
             "Entre $2.00 y $4.99": 175,
             "Entre $5.00 y $9.99": 53,
             "Más de $10.00": 18,
             "No pagaría por este tipo de app": 16,
         },
        "accion_post_pregunta": "siguiente"  # ← aquí
     },

     17: {
         "tipo_pregunta" : una_opcion,
         "pregunta": "¿Estaría dispuesto a recomendar una aplicación como esta si cumple con lo prometido?",
         "respuesta" : {
             "Sí" : 200,
             "No" : 100,
             "Tal vez" : 50
         },
         "respuesta_texto_si": ["TallerApp", "Mecánico Pro", "AutoCheck", "App de mi taller"],
        "accion_post_pregunta": "enviar"  # ← aquí
     },

 }



    # 14: {
    #     "tipo_pregunta" : una_opcion,
    #     "pregunta": "¿Cuál es el grado de autismo de su PRIMER hijo?",
    #     "respuesta" : {
    #         "Nivel 1: Necesita ayuda" : 0,
    #         "Nivel 2: Necesita ayuda notable" : 5,
    #         "Nivel 3: Necesita ayuda muy notable" : 5,
    #     }
    # },
    # 15:{
    #     "tipo_pregunta" : una_opcion,
    #     "pregunta": "¿Cuál es el género de su SEGUNDO hijo?",
    #     "respuesta": {
    #         "Másculino": 10,
    #         "Femenino": 0,
    #     }
    # },
    # 16: {
    #     "tipo_pregunta" : una_opcion,
    #     "pregunta": "¿Cuál es la edad de su SEGUNDO hijo?",
    #     "respuesta" : {
    #         "5 a 7 años" : 8,
    #         "8 a 10 años" : 0,
    #         "11 a 13 años" : 2
    #     }
    # },
    # 17: {
    #     "tipo_pregunta" : una_opcion,
    #     "pregunta": "¿Cuál es el grado de autismo de su SEGUNDO hijo?",
    #     "respuesta" : {
    #         "Nivel 1: Necesita ayuda" : 7,
    #         "Nivel 2: Necesita ayuda notable" : 2,
    #         "Nivel 3: Necesita ayuda muy notable" : 1,
    #     }
    # },
    # 18: {
    #     "tipo_pregunta" : una_opcion,
    #     "pregunta": "¿Cuál es el género de su TERCER hijo?",
    #     "respuesta": {
    #         "Másculino": 2,
    #         "Femenino": 8,
    #     }
    # },
    # 19: {
    #     "tipo_pregunta" : una_opcion,
    #     "pregunta": "¿Cuál es la edad de su TERCER hijo?",
    #     "respuesta" : {
    #         "5 a 7 años" : 0,
    #         "8 a 10 años" : 10,
    #         "11 a 13 años" : 0
    #     }
    # },
    # 20: {
    #     "tipo_pregunta" : una_opcion,
    #     "pregunta": "¿Cuál es el grado de autismo de su TERCER hijo?",
    #     "respuesta" : {
    #         "Nivel 1: Necesita ayuda" : 5,
    #         "Nivel 2: Necesita ayuda notable" : 1,
    #         "Nivel 3: Necesita ayuda muy notable" : 4,
    #     }
    # },

    # ######## TERMINA PREGUNTAS PARA 3 HIJOS ########

    # ######## INICIA PREGUNTAS PARA 4 HIJOS ########
    # 21:{
    #     "tipo_pregunta" : una_opcion,
    #     "pregunta": "¿Cuál es el género de su PRIMER hijo?",
    #     "respuesta": {
    #         "Másculino": 0,
    #         "Femenino": 0,
    #     }
    # },
    # 22: {
    #     "tipo_pregunta" : una_opcion,
    #     "pregunta": "¿Cuál es la edad de su PRIMER hijo?",
    #     "respuesta" : {
    #         "5 a 7 años" : 0,
    #         "8 a 10 años" : 0,
    #         "11 a 13 años" : 0
    #     }
    # },
    # 23: {
    #     "tipo_pregunta" : una_opcion,
    #     "pregunta": "¿Cuál es el grado de autismo de su PRIMER hijo?",
    #     "respuesta" : {
    #         "Nivel 1: Necesita ayuda" : 0,
    #         "Nivel 2: Necesita ayuda notable" : 0,
    #         "Nivel 3: Necesita ayuda muy notable" : 0,
    #     }
    # },
    # 24:{
    #     "tipo_pregunta" : una_opcion,
    #     "pregunta": "¿Cuál es el género de su SEGUNDO hijo?",
    #     "respuesta": {
    #         "Másculino": 0,
    #         "Femenino": 0,
    #     }
    # },
    # 25: {
    #     "tipo_pregunta" : una_opcion,
    #     "pregunta": "¿Cuál es la edad de su SEGUNDO hijo?",
    #     "respuesta" : {
    #         "5 a 7 años" : 0,
    #         "8 a 10 años" : 0,
    #         "11 a 13 años" : 0
    #     }
    # },
    # 26: {
    #     "tipo_pregunta" : una_opcion,
    #     "pregunta": "¿Cuál es el grado de autismo de su SEGUNDO hijo?",
    #     "respuesta" : {
    #         "Nivel 1: Necesita ayuda" : 0,
    #         "Nivel 2: Necesita ayuda notable" : 0,
    #         "Nivel 3: Necesita ayuda muy notable" : 0,
    #     }
    # },
    # 27: {
    #     "tipo_pregunta" : una_opcion,
    #     "pregunta": "¿Cuál es el género de su TERCER hijo?",
    #     "respuesta": {
    #         "Másculino": 0,
    #         "Femenino": 0,
    #     }
    # },
    # 28: {
    #     "tipo_pregunta" : una_opcion,
    #     "pregunta": "¿Cuál es la edad de su TERCER hijo?",
    #     "respuesta" : {
    #         "5 a 7 años" : 0,
    #         "8 a 10 años" : 0,
    #         "11 a 13 años" : 0
    #     }
    # },
    # 29: {
    #     "tipo_pregunta" : una_opcion,
    #     "pregunta": "¿Cuál es el grado de autismo de su TERCER hijo?",
    #     "respuesta" : {
    #         "Nivel 1: Necesita ayuda" : 0,
    #         "Nivel 2: Necesita ayuda notable" : 0,
    #         "Nivel 3: Necesita ayuda muy notable" : 0,
    #     }
    # },
    # 30: {
    #     "tipo_pregunta" : una_opcion,
    #     "pregunta": "¿Cuál es el género de su CUARTO hijo?",
    #     "respuesta": {
    #         "Másculino": 0,
    #         "Femenino": 0,
    #     }
    # },
    # 31: {
    #     "tipo_pregunta" : una_opcion,
    #     "pregunta": "¿Cuál es la edad de su CUARTO hijo?",
    #     "respuesta" : {
    #         "5 a 7 años" : 0,
    #         "8 a 10 años" : 0,
    #         "11 a 13 años" : 0
    #     }
    # },
    # 32: {
    #     "tipo_pregunta" : una_opcion,
    #     "pregunta": "¿Cuál es el grado de autismo de su CUARTO hijo?",
    #     "respuesta" : {
    #         "Nivel 1: Necesita ayuda" : 0,
    #         "Nivel 2: Necesita ayuda notable" : 0,
    #         "Nivel 3: Necesita ayuda muy notable" : 0,
    #     }
    # },
    # ######## TERMINA PREGUNTAS PARA 4 HIJOS ########

    # ######## INICIA DATOS SOBRE EL PRODUCTO ########
    # 33: {
    #     "tipo_pregunta" : una_opcion,
    #     "pregunta": "¿Su hijo cuenta con algún dispositivo inteligente? (Teléfono celular, tablet, computadora, consola de videojuegos)",
    #     "respuesta": {
    #         "Si": 244,
    #         "No": 90,
    #     }
    # },
    # 34: {
    #     "tipo_pregunta" : una_opcion,
    #     "pregunta": "¿Qué tipo de aparato inteligente es el que utiliza más su hijo?",
    #     "respuesta": {
    #         "Teléfono celular": 134,
    #         "Tablet": 90,
    #         "Computadora": 10,
    #         "Consola de videojuegos": 10,
    #     }
    # },
    # 35: {
    #     "tipo_pregunta" : "seleccion_multiple",
    #     "pregunta": "¿Qué tipo de aplicaciones tiene instalado?",
    #     "respuesta": {
    #         "Videojuegos": 244,
    #         "Aplicaciones terapeuticas para TEA o aplicaciones que considera que ayudan a la situación actual de su hijo": 63,
    #         "Aplicaciones para videos": 210,
    #         "Aplicaciones eductavias": 56 # Le hice modificaciones a esta respuesta
    #     }
    # },
    # 36: {
    #     "tipo_pregunta" : una_opcion,
    #     "pregunta": "¿Cuánto tiempo al día pasa su hijo en el celular?",
    #     "respuesta": {
    #         "1 Hora": 100,
    #         "2 Horas": 50,
    #         "3 Horas": 50,
    #         "4 Horas": 30,
    #         "5 Horas o más" : 14
    #     }
    # },
    # 37: {
    #     "tipo_pregunta" : "seleccion_multiple",
    #     "pregunta": "¿Qué tipo de aplicaciones o videojuegos que ayuden al tratamiento del TEA conoce o tiene instalado en su dispositivo inteligente de su hijo?",
    #     "respuesta": {
    #         "Otismo | Educación Especial (Empresa: Otsimo)" : 74,
    #         "Terapia del lenguaje cogniti (Empresa: ImagiRation LLC)" : 244,
    #         "Juegos para niños con autismo (Empresa: IDZ Digital Private Limited)" : 20,
    #     }
    # },
    # 38: {
    #     "tipo_pregunta" : "seleccion_multiple",
    #     "pregunta": "Indique ¿Qué factores tomaría en cuenta a la hora de instalar una aplicación que ayude a tratar el TEA?",
    #     "respuesta" : {
    #         "Precio de aplicación o suscripción" : 244,
    #         "Asistente inteligente que ayude a desarrollar la interacciones sociales": 244,
    #         "Creación de reportes mediante IA para detectar los factores que más estén perjudicando al tratante trata" : 244,
    #         "Variedad de juegos para el tratamiento de la TEA" : 150,
    #         "Variedad de estimulos visuales y sonoros que ayuden a tranquilizar el tratante": 100,
    #         "El tamaño de la aplicación" : 50,
    #         "Qué sea multiplataforma" : 120,
    #     }
    # },
    # 39:{
    #     "tipo_pregunta" : una_opcion,
    #     "pregunta": "¿Estaría dispuesto a descargar su hijo con una nueva aplicación que ayude en el tratamiento TEA con las cualidades que usted desea?",
    #     "respuesta": {
    #         "Si": 240,
    #         "No": 4,
    #     }

    # },
    # ######## TERMINA DATOS SOBRE EL PRODUCTO ########

    # ######## INICIO DATOS SOBRE EL PRECIO ########
    # 40: {
    #     "tipo_pregunta" : una_opcion,
    #     "pregunta": "¿Cuánto estaría dispuesto a pagar en una aplicación que ayude en el tratamiento de TEA?",
    #     "respuesta": {
    #         "Opción 1": 186,
    #         "Opción 2": 50,
    #         "Opción 3": 4,
    #     }
    # },

    # ######## TERMINA DATOS SOBRE EL PRECIO ########

    # ######## INICIA DATOS SOBRE LA PLAZA ##########
    # 41: {
    #     "tipo_pregunta" : una_opcion,
    #     "pregunta": "¿De qué centro es usted?",
    #     "respuesta": {
    #         "Centro de investigación Edu-terapéutico (CIE)": 155,
    #         "Hogar de protección Pajarito Azul" : 50,
    #         "Hospital Psicosocial Nacional": 35,
    #     }
    # },
    # 42: {
    #     "tipo_pregunta" : una_opcion,
    #     "pregunta": "¿En qué tienda suele descargar sus aplicaciones a su hijo?",
    #     "respuesta": {
    #         "PlayStore (Dispositivos Android)": 160,
    #         "AppStore (Dispositivos Apple iOS)": 80,
    #         "Los suelo descargar de internet sin una tienda": 0,
    #     }
    # },

    # ######## TERMINA DATOS SOBRE LA PLAZA ##########

    # ######### INICIO DE ANUNCIOS PUBLICITARIOS #########
    # 43: {
    #     "tipo_pregunta" : una_opcion,
    #     "pregunta": "¿Ha visto anuncios publicitarios a cerca de aplicaciones que den tratamiento a los niños con TEA?",
    #     "respuesta": {
    #         "Si": 43,
    #         "No": 197,
    #     }
    # },

    #             ####### INICIO SI CONOCE ANUNCIOS PUBLICITARIOS ########

    # 44: {
    #     "tipo_pregunta" : "seleccion_multiple",
    #     "pregunta": "¿En qué medios de comunicación ha notado la promoción de aplicaciones para el tratamiento de niños con TEA?",
    #     "respuesta": {
    #         "Redes Sociales": 43,
    #         "Revistas especializadas": 0,
    #         "Televisión": 0,
    #         "Periódico" : 0,
    #     }
    # },
    # 45: {
    #     "tipo_pregunta" : una_opcion,
    #     "pregunta": "¿Con qué frecuencia ha visto alguna publicidad a cerca de aplicaciones que den tratamiento a los niños con TEA?",
    #     "respuesta": {
    #         "Diario": 10,
    #         "Semanal": 11,
    #         "Quincenal": 4,
    #         "Mensual": 18,
    #     }
    # },
    
    #                 ####### TERMINA SI CONOCE ANUNCIOS PUBLICITARIOS ########

    #                 ####### INICIO SI NO CONOCE ANUNCIOS PUBLICITARIOS ########

    # 46: {
    #     "tipo_pregunta" : "seleccion_multiple",
    #     "pregunta": "¿Cuáles de los siguientes medios de comunicación le gustaría ver anuncios a cerca de una aplicación que ayude con el tratamiento de los niños con TEA?",
    #     "respuesta": {
    #         "Redes sociales": 240,
    #         "Revistas especializadas": 40,
    #         "Televisión": 40,
    #         "Periódico": 0,
    #     }
    # },
    # 47: {
    #     "tipo_pregunta" : "seleccion_multiple",
    #     "pregunta": "¿Qué factores le llamaría la atención en un anuncio publicitario a cerca de una aplicación que ayude en el tratamiento de los niños con TEA?",
    #     "respuesta": {
    #         "Diseño": 240,
    #         "Mensaje": 10,
    #         "Vistosidad": 10,
    #         "Imagen": 240,
    #         "Lenguaje" : 240,
    #     }
    # },

    #                 ####### TERMINA SI NO CONOCE ANUNCIOS PUBLICITARIOS ########

    # ######### TERMINA DE ANUNCIOS PUBLICITARIOS #########

    # ######### INICIO DE RESPUESTAS A NO #########
    # #PREGUNTA DE NO "¿Estaría dispuesto a descargar su hijo con una nueva aplicación que ayude en el tratamiento TEA con las cualidades que usted desea?"
    # 48: {
    #     "tipo_pregunta" : "seleccion_multiple",
    #     "pregunta": "¿Por qué su hijo no tiene ningún dispositivo inteligente?",
    #     "respuesta": {
    #         "Pienso que la tecnología es muy peligrosa para mi hijo": 90,
    #         "No tenemos dinero suficiente para comprarle un dispositivo inteligente": 10,
    #         "Considero que un dispositivo inteligente causaría más perjuicios a su capacidad": 50,
    #     }
    # },


    # #PREGUNTA DE NO "¿Por qué no estaría dispuesto a descargar a su hijo una nueva aplicación que ayude en el tratamiento de TEA?"

    # 49: {
    #     "tipo_pregunta" : "seleccion_multiple",
    #     "pregunta": "¿Por qué no estaría dispuesto a descargar a su hijo una nueva aplicación que ayude en el tratamiento de TEA?",
    #     "respuesta": {
    #         "Considero que el tener aplicaciones instaladas en el teléfono es un riesgo para mi hijo": 2,
    #         "Los factores que me me plantearon no me son muy convincentes": 0,
    #         "No tengo el ideal que una aplicación pueda ayudar al tratamiento de TEA": 4,
    #     }
    # },



