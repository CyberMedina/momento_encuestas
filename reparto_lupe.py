from variables import *

pregunta_respuestas = {
    # 1: {
    #     "tipo_pregunta" : una_opcion, 
    #     "pregunta": "¿Es tutor o padre de familia de algún niño con trastorno del espectro autista (TEA)?",
    #     "respuesta": {
    #         "Si": 334,
    #         "No": 10
    #     }
    # },
    # 2: {
    #     "tipo_pregunta" : una_opcion,
    #     "pregunta": "¿Cuántos niñ@o hij@s con trastorno del espectro autista (TEA) tiene a cargo?",
    #     "respuesta": {
    #         "1": 304,
    #         "2": 20,
    #         "3": 10,
    #         "4": 0,
    #     }
    # },
    ######## INICIA PREGUNTAS PARA SOLO 1 HIJO ########
    3:{
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Cuál es el género de su hijo?",
        "respuesta": {
            "Másculino": 222,
            "Femenino": 82,
        }
    },
    4: {
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Cuál es la edad de su hijo?",
        "respuesta" : {
            "5 a 7 años" : 204,
            "8 a 10 años" : 57,
            "11 a 13 años" : 43
        }
    },
    5: {
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Cuál es el grado de autismo de su hijo?",
        "respuesta" : {
            "Nivel 1: Necesita ayuda" : 225,
            "Nivel 2: Necesita ayuda notable" : 57,
            "Nivel 3: Necesita ayuda muy notable" : 22,
        }
    },
    ######## TERMINA PREGUNTAS PARA SOLO 1 HIJO ########

    ######## INICIA PREGUNTAS PARA 2 HIJOS ########
     6:{
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Cuál es el género de su PRIMER hijo?",
        "respuesta": {
            "Másculino": 17,
            "Femenino": 3,
        }
    },
    7: {
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Cuál es la edad de su PRIMER hijo?",
        "respuesta" : {
            "5 a 7 años" : 11,
            "8 a 10 años" : 6,
            "11 a 13 años" : 3
        }
    },
    8: {
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Cuál es el grado de autismo de su PRIMER hijo?",
        "respuesta" : {
            "Nivel 1: Necesita ayuda" : 19,
            "Nivel 2: Necesita ayuda notable" : 1,
            "Nivel 3: Necesita ayuda muy notable" : 0,
        }
    },
    9:{
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Cuál es el género de su SEGUNDO hijo?",
        "respuesta": {
            "Másculino": 18,
            "Femenino": 2,
        }
    },
    10: {
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Cuál es la edad de su SEGUNDO hijo?",
        "respuesta" : {
            "5 a 7 años" : 11,
            "8 a 10 años" : 7,
            "11 a 13 años" : 2
        }
    },
    11: {
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Cuál es el grado de autismo de su SEGUNDO hijo?",
        "respuesta" : {
            "Nivel 1: Necesita ayuda" : 20,
            "Nivel 2: Necesita ayuda notable" : 0,
            "Nivel 3: Necesita ayuda muy notable" : 0,
        }
    },

    ######## TERMINA PREGUNTAS PARA 2 HIJOS ########

    ######## INICIA PREGUNTAS PARA 3 HIJOS ######## 
    12: {
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Cuál es el género de su PRIMER hijo?",
        "respuesta": {
            "Másculino": 7,
            "Femenino": 3,
        }
    },
    13: {
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Cuál es la edad de su PRIMER hijo?",
        "respuesta" : {
            "5 a 7 años" : 10,
            "8 a 10 años" : 0,
            "11 a 13 años" : 0
        }
    },
    14: {
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Cuál es el grado de autismo de su PRIMER hijo?",
        "respuesta" : {
            "Nivel 1: Necesita ayuda" : 0,
            "Nivel 2: Necesita ayuda notable" : 5,
            "Nivel 3: Necesita ayuda muy notable" : 5,
        }
    },
    15:{
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Cuál es el género de su SEGUNDO hijo?",
        "respuesta": {
            "Másculino": 10,
            "Femenino": 0,
        }
    },
    16: {
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Cuál es la edad de su SEGUNDO hijo?",
        "respuesta" : {
            "5 a 7 años" : 8,
            "8 a 10 años" : 0,
            "11 a 13 años" : 2
        }
    },
    17: {
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Cuál es el grado de autismo de su SEGUNDO hijo?",
        "respuesta" : {
            "Nivel 1: Necesita ayuda" : 7,
            "Nivel 2: Necesita ayuda notable" : 2,
            "Nivel 3: Necesita ayuda muy notable" : 1,
        }
    },
    18: {
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Cuál es el género de su TERCER hijo?",
        "respuesta": {
            "Másculino": 2,
            "Femenino": 8,
        }
    },
    19: {
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Cuál es la edad de su TERCER hijo?",
        "respuesta" : {
            "5 a 7 años" : 0,
            "8 a 10 años" : 10,
            "11 a 13 años" : 0
        }
    },
    20: {
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Cuál es el grado de autismo de su TERCER hijo?",
        "respuesta" : {
            "Nivel 1: Necesita ayuda" : 5,
            "Nivel 2: Necesita ayuda notable" : 1,
            "Nivel 3: Necesita ayuda muy notable" : 4,
        }
    },

    ######## TERMINA PREGUNTAS PARA 3 HIJOS ########

    ######## INICIA PREGUNTAS PARA 4 HIJOS ########
    21:{
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Cuál es el género de su PRIMER hijo?",
        "respuesta": {
            "Másculino": 0,
            "Femenino": 0,
        }
    },
    22: {
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Cuál es la edad de su PRIMER hijo?",
        "respuesta" : {
            "5 a 7 años" : 0,
            "8 a 10 años" : 0,
            "11 a 13 años" : 0
        }
    },
    23: {
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Cuál es el grado de autismo de su PRIMER hijo?",
        "respuesta" : {
            "Nivel 1: Necesita ayuda" : 0,
            "Nivel 2: Necesita ayuda notable" : 0,
            "Nivel 3: Necesita ayuda muy notable" : 0,
        }
    },
    24:{
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Cuál es el género de su SEGUNDO hijo?",
        "respuesta": {
            "Másculino": 0,
            "Femenino": 0,
        }
    },
    25: {
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Cuál es la edad de su SEGUNDO hijo?",
        "respuesta" : {
            "5 a 7 años" : 0,
            "8 a 10 años" : 0,
            "11 a 13 años" : 0
        }
    },
    26: {
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Cuál es el grado de autismo de su SEGUNDO hijo?",
        "respuesta" : {
            "Nivel 1: Necesita ayuda" : 0,
            "Nivel 2: Necesita ayuda notable" : 0,
            "Nivel 3: Necesita ayuda muy notable" : 0,
        }
    },
    27: {
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Cuál es el género de su TERCER hijo?",
        "respuesta": {
            "Másculino": 0,
            "Femenino": 0,
        }
    },
    28: {
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Cuál es la edad de su TERCER hijo?",
        "respuesta" : {
            "5 a 7 años" : 0,
            "8 a 10 años" : 0,
            "11 a 13 años" : 0
        }
    },
    29: {
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Cuál es el grado de autismo de su TERCER hijo?",
        "respuesta" : {
            "Nivel 1: Necesita ayuda" : 0,
            "Nivel 2: Necesita ayuda notable" : 0,
            "Nivel 3: Necesita ayuda muy notable" : 0,
        }
    },
    30: {
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Cuál es el género de su CUARTO hijo?",
        "respuesta": {
            "Másculino": 0,
            "Femenino": 0,
        }
    },
    31: {
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Cuál es la edad de su CUARTO hijo?",
        "respuesta" : {
            "5 a 7 años" : 0,
            "8 a 10 años" : 0,
            "11 a 13 años" : 0
        }
    },
    32: {
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Cuál es el grado de autismo de su CUARTO hijo?",
        "respuesta" : {
            "Nivel 1: Necesita ayuda" : 0,
            "Nivel 2: Necesita ayuda notable" : 0,
            "Nivel 3: Necesita ayuda muy notable" : 0,
        }
    },
    ######## TERMINA PREGUNTAS PARA 4 HIJOS ########

    ######## INICIA DATOS SOBRE EL PRODUCTO ########
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

    ######## INICIO DATOS SOBRE EL PRECIO ########
    40: {
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Cuánto estaría dispuesto a pagar en una aplicación que ayude en el tratamiento de TEA?",
        "respuesta": {
            "Opción 1": 186,
            "Opción 2": 50,
            "Opción 3": 4,
        }
    },

    # ######## TERMINA DATOS SOBRE EL PRECIO ########

    # ######## INICIA DATOS SOBRE LA PLAZA ##########
    41: {
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿De qué centro es usted?",
        "respuesta": {
            "Centro de investigación Edu-terapéutico (CIE)": 155,
            "Hogar de protección Pajarito Azul" : 50,
            "Hospital Psicosocial Nacional": 35,
        }
    },
    42: {
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿En qué tienda suele descargar sus aplicaciones a su hijo?",
        "respuesta": {
            "PlayStore (Dispositivos Android)": 160,
            "AppStore (Dispositivos Apple iOS)": 80,
            "Los suelo descargar de internet sin una tienda": 0,
        }
    },

    ######## TERMINA DATOS SOBRE LA PLAZA ##########

    ######### INICIO DE ANUNCIOS PUBLICITARIOS #########
    43: {
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Ha visto anuncios publicitarios a cerca de aplicaciones que den tratamiento a los niños con TEA?",
        "respuesta": {
            "Si": 43,
            "No": 197,
        }
    },

                ####### INICIO SI CONOCE ANUNCIOS PUBLICITARIOS ########

    44: {
        "tipo_pregunta" : "seleccion_multiple",
        "pregunta": "¿En qué medios de comunicación ha notado la promoción de aplicaciones para el tratamiento de niños con TEA?",
        "respuesta": {
            "Redes Sociales": 43,
            "Revistas especializadas": 0,
            "Televisión": 0,
            "Periódico" : 0,
        }
    },
    45: {
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Con qué frecuencia ha visto alguna publicidad a cerca de aplicaciones que den tratamiento a los niños con TEA?",
        "respuesta": {
            "Diario": 10,
            "Semanal": 11,
            "Quincenal": 4,
            "Mensual": 18,
        }
    },
    
                    ####### TERMINA SI CONOCE ANUNCIOS PUBLICITARIOS ########

                    ####### INICIO SI NO CONOCE ANUNCIOS PUBLICITARIOS ########

    46: {
        "tipo_pregunta" : "seleccion_multiple",
        "pregunta": "¿Cuáles de los siguientes medios de comunicación le gustaría ver anuncios a cerca de una aplicación que ayude con el tratamiento de los niños con TEA?",
        "respuesta": {
            "Redes sociales": 240,
            "Revistas especializadas": 40,
            "Televisión": 40,
            "Periódico": 0,
        }
    },
    47: {
        "tipo_pregunta" : "seleccion_multiple",
        "pregunta": "¿Qué factores le llamaría la atención en un anuncio publicitario a cerca de una aplicación que ayude en el tratamiento de los niños con TEA?",
        "respuesta": {
            "Diseño": 240,
            "Mensaje": 10,
            "Vistosidad": 10,
            "Imagen": 240,
            "Lenguaje" : 240,
        }
    },

                    ####### TERMINA SI NO CONOCE ANUNCIOS PUBLICITARIOS ########

    ######### TERMINA DE ANUNCIOS PUBLICITARIOS #########

    ######### INICIO DE RESPUESTAS A NO #########
    #PREGUNTA DE NO "¿Estaría dispuesto a descargar su hijo con una nueva aplicación que ayude en el tratamiento TEA con las cualidades que usted desea?"
    48: {
        "tipo_pregunta" : "seleccion_multiple",
        "pregunta": "¿Por qué su hijo no tiene ningún dispositivo inteligente?",
        "respuesta": {
            "Pienso que la tecnología es muy peligrosa para mi hijo": 90,
            "No tenemos dinero suficiente para comprarle un dispositivo inteligente": 10,
            "Considero que un dispositivo inteligente causaría más perjuicios a su capacidad": 50,
        }
    },


    #PREGUNTA DE NO "¿Por qué no estaría dispuesto a descargar a su hijo una nueva aplicación que ayude en el tratamiento de TEA?"

    49: {
        "tipo_pregunta" : "seleccion_multiple",
        "pregunta": "¿Por qué no estaría dispuesto a descargar a su hijo una nueva aplicación que ayude en el tratamiento de TEA?",
        "respuesta": {
            "Considero que el tener aplicaciones instaladas en el teléfono es un riesgo para mi hijo": 2,
            "Los factores que me me plantearon no me son muy convincentes": 0,
            "No tengo el ideal que una aplicación pueda ayudar al tratamiento de TEA": 4,
        }
    },

}

