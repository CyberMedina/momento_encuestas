una_opcion = "una_opcion"

pregunta_respuestas = {
    1: {
        "tipo_pregunta": una_opcion,
        "pregunta": "¿Posee usted un vehículo?",
        "respuesta": {
            "Si": 350,
            "No": 30,
        },
        "accion_post_pregunta": "siguiente"  # ← aquí
    },
    2: {
        "tipo_pregunta": una_opcion,
        "pregunta": "¿Cuál es su edad?",
        "respuesta": {
            "Menos de 18": 0,
            "18 - 25": 90,
            "26 - 35": 150,
            "36 - 50": 100,
            "Más de 50": 10,
        }
    },
    3: {
        "tipo_pregunta": una_opcion,
        "pregunta": "¿Cuál es su ocupación?",
        "respuesta": {
            "Mecánico": 170,
            "Dueño de un taller": 10,
            "Dueño de un vehículo particular": 160,
            "Gestor de flotas": 10,
            "Otros:": 0,
        }
    },
    4: {
        "tipo_pregunta": una_opcion,
        "pregunta": "¿En que distrito habita o se encuentra su negocio?",
        "respuesta": {
            "Distrito I": 80,
            "Distrito II": 80,
            "Distrito III": 100,
            "Distrito IV": 15,
            "Distrito V": 50,
            "Distrito VI": 25,
            "Otros:": 0,
        },
        "accion_post_pregunta": "siguiente"  # ← aquí
    },
    5: {
        "tipo_pregunta": una_opcion,
        "pregunta": "¿Ha usado alguna vez una aplicación para gestionar el mantenimiento de su vehículo?",
        "respuesta": {
            "Si": 10,
            "No": 340,
        },
        "respuesta_texto_si": ["MiCarroApp", "AutoGestor", "DrAuto", "Ninguna en particular"]
        
    },
    6: {
        "tipo_pregunta": una_opcion,
        "pregunta": "¿Usa actualmente una aplicación para gestionar el mantenimiento de su vehículo?",
        "respuesta": {
            "Si": 10,
            "No": 340,
        },
        "respuesta_texto_si": ["TallerApp", "Mecánico Pro", "AutoCheck", "App de mi taller"]
    },
    7: {
        "tipo_pregunta": una_opcion,
        "pregunta": "¿Estaría interesado en usar una aplicación que de recomendaciones de mantenimiento para su vehículo utilizando inteligencia artificial y la opinión de expertos?",
        "respuesta": {
            "Si": 320,
            "No": 30,
        },
        "accion_post_pregunta": "enviar"  # ← aquí
    },
}
