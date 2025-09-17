import random

# =========================
# SISTEMA EXPERTO: Limpieza del Hogar (Markov)
# =========================

# Definimos los estados del hogar
estados = ["todo limpio", "piso sucio", "ventanas sucias", "ropa acumulada", "trastes sucios", "baño sucio"]

# Matriz de transiciones Markovianas
# transiciones[estado_actual][estado_siguiente] = probabilidad
transiciones = {
    "todo limpio": {
        "todo limpio": 0.7,
        "piso sucio": 0.1,
        "ventanas sucias": 0.05,
        "ropa acumulada": 0.05,
        "trastes sucios": 0.05,
        "baño sucio": 0.05
    },
    "piso sucio": {
        "todo limpio": 0.6,  # si limpias
        "piso sucio": 0.4
    },
    "ventanas sucias": {
        "todo limpio": 0.6,
        "ventanas sucias": 0.4
    },
    "ropa acumulada": {
        "todo limpio": 0.6,
        "ropa acumulada": 0.4
    },
    "trastes sucios": {
        "todo limpio": 0.7,
        "trastes sucios": 0.3
    },
    "baño sucio": {
        "todo limpio": 0.5,
        "baño sucio": 0.5
    }
}

# Recomendaciones de limpieza
recomendaciones = {
    "piso sucio": "Debes barrer y trapear el piso.",
    "ventanas sucias": "Debes limpiar las ventanas con un trapo húmedo.",
    "ropa acumulada": "Debes lavar la ropa y doblarla.",
    "trastes sucios": "Debes lavar los trastes.",
    "baño sucio": "Debes limpiar el baño con desinfectante.",
    "todo limpio": "No es necesario limpiar ahora, puedes descansar."
}

def siguiente_estado(estado_actual):
    """
    Calcula el siguiente estado según la matriz de transiciones de Markov.
    """
    posibles = list(transiciones[estado_actual].keys())
    probabilidades = list(transiciones[estado_actual].values())
    return random.choices(posibles, probabilidades)[0]

def motor_inferencia(estado):
    """
    Motor de inferencia que recomienda acciones según el estado actual.
    """
    return recomendaciones.get(estado, "No tengo una recomendación para ese estado.")

def consultar_sistema():
    """
    Interfaz de consulta del sistema experto con dinámica Markoviana.
    """
    estado = "todo limpio"  # comenzamos con la casa limpia
    print("=== SISTEMA EXPERTO DE LIMPIEZA DEL HOGAR (MARKOV) ===")
    print("El sistema simula cómo se ensucia o se mantiene limpia la casa con el tiempo.")
    print("Escribe 'salir' para terminar.\n")

    while True:
        print(f"Estado actual de la casa: {estado}")
        print(f"Recomendación: {motor_inferencia(estado)}\n")

        accion = input("Presiona ENTER para avanzar al siguiente día o escribe 'salir': ").lower()
        if accion == "salir":
            print("Saliendo del sistema experto. ¡Tu casa estará impecable!")
            break

        # Avanzar en la cadena de Markov
        estado = siguiente_estado(estado)

# -------------------
# EJECUCIÓN
# -------------------
if __name__ == "__main__":
    consultar_sistema()
