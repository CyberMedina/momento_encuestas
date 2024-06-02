from variables import *

pregunta_respuestas = {
    1: {
        "tipo_pregunta" : una_opcion, 
        "pregunta": "¿Es tutor o padre de familia de algún niño con trastorno del espectro autista (TEA)?",
        "respuesta": {
            "Sí": 5,
            "No": 2
        }
    },
    2: {
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Cuántos niñ@o hij@s con trastorno del espectro autista (TEA) tiene a cargo?",
        "respuesta": {
            "1": 3,
            "2": 1,
            "3": 1,
            "4": 0,
        }
    },
    ######## INICIA PREGUNTAS PARA SOLO 1 HIJO ########
    3:{
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Cuál es el género de su hijo?",
        "respuesta": {
            "Masculino": 2,
            "Femenino": 1,
        }
    },
    4: {
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Cuál es la edad de su hijo?",
        "respuesta" : {
            "5 a 7 años" : 1,
            "8 a 10 años" : 2,
            "11 a 13 años" : 1
        }
    },
    5: {
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Cuál es el grado de autismo de su hijo?",
        "respuesta" : {
            "Nivel 1" : 1,
            "Nivel 2" : 2,
            "Nivel 3" : 0,
        }
    },
    ######## TERMINA PREGUNTAS PARA SOLO 1 HIJO ########

    ######## INICIA PREGUNTAS PARA 2 HIJOS ########
     6:{
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Cuál es el género de su PRIMER hijo?",
        "respuesta": {
            "Masculino": 1,
            "Femenino": 0,
        }
    },
    7: {
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Cuál es la edad de su PRIMER hijo?",
        "respuesta" : {
            "5 a 7 años" : 0,
            "8 a 10 años" : 1,
            "11 a 13 años" : 0
        }
    },
    8: {
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Cuál es el grado de autismo de su PRIMER hijo?",
        "respuesta" : {
            "Nivel 1" : 1,
            "Nivel 2" : 0,
            "Nivel 3" : 0,
        }
    },
    9:{
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Cuál es el género de su SEGUNDO hijo?",
        "respuesta": {
            "Masculino": 0,
            "Femenino": 1,
        }
    },
    10: {
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Cuál es la edad de su SEGUNDO hijo?",
        "respuesta" : {
            "5 a 7 años" : 0,
            "8 a 10 años" : 1,
            "11 a 13 años" : 0
        }
    },
    11: {
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Cuál es el grado de autismo de su SEGUNDO hijo?",
        "respuesta" : {
            "Nivel 1" : 0,
            "Nivel 2" : 1,
            "Nivel 3" : 0,
        }
    },

    ######## TERMINA PREGUNTAS PARA 2 HIJOS ########

    ######## INICIA PREGUNTAS PARA 3 HIJOS ######## 
    12: {
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Cuál es el género de su PRIMER hijo?",
        "respuesta": {
            "Masculino": 1,
            "Femenino": 0,
        }
    },
    13: {
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Cuál es la edad de su PRIMER hijo?",
        "respuesta" : {
            "5 a 7 años" : 1,
            "8 a 10 años" : 0,
            "11 a 13 años" : 0
        }
    },
    14: {
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Cuál es el grado de autismo de su PRIMER hijo?",
        "respuesta" : {
            "Nivel 1" : 1,
            "Nivel 2" : 0,
            "Nivel 3" : 0,
        }
    },
    15:{
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Cuál es el género de su SEGUNDO hijo?",
        "respuesta": {
            "Masculino": 1,
            "Femenino": 0,
        }
    },
    16: {
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Cuál es la edad de su SEGUNDO hijo?",
        "respuesta" : {
            "5 a 7 años" : 0,
            "8 a 10 años" : 1,
            "11 a 13 años" : 0
        }
    },
    17: {
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Cuál es el grado de autismo de su SEGUNDO hijo?",
        "respuesta" : {
            "Nivel 1" : 1,
            "Nivel 2" : 0,
            "Nivel 3" : 0,
        }
    },
    18: {
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Cuál es el género de su TERCER hijo?",
        "respuesta": {
            "Masculino": 0,
            "Femenino": 1,
        }
    },
    19: {
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Cuál es la edad de su TERCER hijo?",
        "respuesta" : {
            "5 a 7 años" : 0,
            "8 a 10 años" : 1,
            "11 a 13 años" : 0
        }
    },
    20: {
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Cuál es el grado de autismo de su TERCER hijo?",
        "respuesta" : {
            "Nivel 1" : 1,
            "Nivel 2" : 0,
            "Nivel 3" : 0,
        }
    },

    ######## TERMINA PREGUNTAS PARA 3 HIJOS ########

    ######## INICIA PREGUNTAS PARA 4 HIJOS ########
    21:{
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Cuál es el género de su PRIMER hijo?",
        "respuesta": {
            "Masculino": 0,
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
            "Nivel 1" : 0,
            "Nivel 2" : 0,
            "Nivel 3" : 0,
        }
    },
    24:{
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Cuál es el género de su SEGUNDO hijo?",
        "respuesta": {
            "Masculino": 0,
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
            "Nivel 1" : 0,
            "Nivel 2" : 0,
            "Nivel 3" : 0,
        }
    },
    27: {
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Cuál es el género de su TERCER hijo?",
        "respuesta": {
            "Masculino": 0,
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
            "Nivel 1" : 0,
            "Nivel 2" : 0,
            "Nivel 3" : 0,
        }
    },
    30: {
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Cuál es el género de su CUARTO hijo?",
        "respuesta": {
            "Masculino": 0,
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
            "Nivel 1" : 0,
            "Nivel 2" : 0,
            "Nivel 3" : 0,
        }
    },
    ######## TERMINA PREGUNTAS PARA 4 HIJOS ########

    ######## INICIA DATOS SOBRE EL PRODUCTO ########
    33: {
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Su hijo cuenta con algún dispositivo inteligente? (Teléfono celular, tablet, computadora, consola de videojuegos)",
        "respuesta": {
            "Sí": 3,
            "No": 2,
        }
    },
    34: {
        "tipo_pregunta" : "seleccion_multiple",
        "pregunta": "¿Qué tipo de aparato inteligente es el que utiliza más su hijo?",
        "respuesta": {
            "Teléfono celular": 3,
            "Tablet": 2,
            "Computadora": 0,
            "Consola de videojuegos": 0,
        }
    },
    35: {
        "tipo_pregunta" : "seleccion_multiple",
        "pregunta": "¿Qué tipo de aplicaciones tiene instalado?",
        "respuesta": {
            "Videojuegos": 1,
            "Aplicaciones terapeuticas para TEA o aplicaciones que considera que ayudan a la situación actual de su hijo": 4,
            "Aplicaciones para videos": 3,
            "Aplicaciones educativas": 0,
        }
    },
    36: {
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Cuánto tiempo al día pasa su hijo en el celular?",
        "respuesta": {
            "1 Hora": 3,
            "2 Horas": 2,
            "3 Horas": 2,
            "4 Horas": 0,
            "5 Horas o más" : 0
        }
    },
    37: {
        "tipo_pregunta" : "seleccion_multiple",
        "pregunta": "¿Qué tipo de aplicaciones o videojuegos que ayuden al tratamiento del TEA conoce o tiene instalado en su dispositivo inteligente de su hijo?",
        "respuesta": {
            "Otismo | Educación Especial (Empresa: Otsimo)" : 3,
            "Terapia del lenguaje cogniti (Empresa: ImagiRation LLC)" : 3,
            "Juegos para niños con autismo (Empresa: IDZ Digital Private Limited)" : 0,
        }
    },
    38: {
        "tipo_pregunta" : "seleccion_multiple",
        "pregunta": "Indique ¿Qué factores tomaría en cuenta a la hora de instalar una aplicación que ayude a tratar el TEA?",
        "respuesta" : {
            "Precio de aplicación o suscripción" : 3,
            "Asistente inteligente que ayude a desarrollar la interacciones sociales": 4,
            "Creación de reportes mediante IA para detectar los factores que más estén perjudicando al tratante trata" : 4,
            "Variedad de juegos para el tratamiento de la TEA" : 3,
            "Variedad de estimulos visuales y sonoros que ayuden a tranquilizar el tratante": 0,
            "El tamaño de la aplicación" : 0,
            "Qué sea multiplataforma" : 0,
        }
    },
    39:{
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Estaría dispuesto a descargar su hijo con una nueva aplicación que ayude en el tratamiento TEA con las cualidades que usted desea?",
        "respuesta": {
            "Sí": 2,
            "No": 2,
        }

    },
    ######## TERMINA DATOS SOBRE EL PRODUCTO ########

    ######## INICIO DATOS SOBRE EL PRECIO ########
    40: {
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Cuánto estaría dispuesto a pagar en una aplicación que ayude en el tratamiento de TEA?",
        "respuesta": {
            "Opción 1": 3,
            "Opción 2": 1,
            "Opción 3": 0,
        }
    },

    ######## TERMINA DATOS SOBRE EL PRECIO ########

    ######## INICIA DATOS SOBRE LA PLAZA ##########
    41: {
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿De qué centro es usted?",
        "respuesta": {
            "Centro de investigación Edu-terapéutico (CIE)": 3,
            "Hogar de protección Pajarito Azul: 100" : 1,
            "Hospital Psicosocial Nacional": 0,
        }
    },
    42: {
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿En qué tienda suele descargar sus aplicaciones a su hijo?",
        "respuesta": {
            "PlayStore (Dispositivos Android)": 3,
            "AppStore (Dispositivos Apple iOS)": 1,
            "Los suelo descargar de internet sin una tienda": 0,
        }
    },

    ######## TERMINA DATOS SOBRE LA PLAZA ##########

    ######### INICIO DE ANUNCIOS PUBLICITARIOS #########
    43: {
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Ha visto anuncios publicitarios a cerca de aplicaciones que den tratamiento a los niños con TEA?",
        "respuesta": {
            "Sí": 3,
            "No": 1,
        }
    },

                ####### INICIO SI CONOCE ANUNCIOS PUBLICITARIOS ########

    44: {
        "tipo_pregunta" : "seleccion_multiple",
        "pregunta": "¿En qué medios de comunicación ha notado la promoción de aplicaciones para el tratamiento de niños con TEA?",
        "respuesta": {
            "Redes Sociales": 3,
            "Revistas especializadas": 3,
            "Televisión": 3,
            "Periódico" : 1,
        }
    },
    45: {
        "tipo_pregunta" : una_opcion,
        "pregunta": "¿Con qué frecuencia ha visto alguna publicidad a cerca de aplicaciones que den tratamiento a los niños con TEA?",
        "respuesta": {
            "Diario": 1,
            "Semanal": 0,
            "Quincenal": 2,
            "Mensual": 0,
        }
    },
    
                    ####### TERMINA SI CONOCE ANUNCIOS PUBLICITARIOS ########

                    ####### INICIO SI NO CONOCE ANUNCIOS PUBLICITARIOS ########

    46: {
        "tipo_pregunta" : "seleccion_multiple",
        "pregunta": "¿Cuáles de los siguientes medios de comunicación le gustaría ver anuncios a cerca de una aplicación que ayude con el tratamiento de los niños con TEA?",
        "respuesta": {
            "Redes sociales": 4,
            "Revistas especializadas": 4,
            "Televisión": 3,
            "Periódico": 0,
        }
    },
    47: {
        "tipo_pregunta" : "seleccion_multiple",
        "pregunta": "¿Qué factores le llamaría la atención en un anuncio publicitario a cerca de una aplicación que ayude en el tratamiento de los niños con TEA?",
        "respuesta": {
            "Diseño": 4,
            "Mensaje": 4,
            "Vistosidad": 4,
            "Imagen": 4,
            "Lenguaje" : 4,
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
            "Pienso que la tecnología es muy peligrosa para mi hijo": 2,
            "No tenemos dinero suficiente para comprarle un dispositivo inteligente": 2,
            "Considero que un dispositivo inteligente causaría más perjuicios a su capacidad": 1,
        }
    },


    #PREGUNTA DE NO "¿Por qué no estaría dispuesto a descargar a su hijo una nueva aplicación que ayude en el tratamiento de TEA?"

    49: {
        "tipo_pregunta" : "seleccion_multiple",
        "pregunta": "¿Por qué no estaría dispuesto a descargar a su hijo una nueva aplicación que ayude en el tratamiento de TEA?",
        "respuesta": {
            "Considero que el tener aplicaciones instaladas en el teléfono es un riesgo para mi hijo": 1,
            "Los factores que me me plantearon no me son muy convincentes": 2,
            "No tengo el ideal que una aplicación pueda ayudar al tratamiento de TEA": 1,
        }
    },

}

