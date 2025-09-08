import json
import os

# Nombre del archivo donde se guardará el conocimiento
archivo_conocimiento = "conocimiento.json"

def cargar_conocimiento():
    """
    Carga el conocimiento desde el archivo JSON si existe.
    Si no existe, retorna un diccionario con frases precargadas.
    """
    if os.path.exists(archivo_conocimiento):
        # Abrimos el archivo y cargamos su contenido como diccionario
        with open(archivo_conocimiento, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        # Conocimiento base inicial
        return {
            "hola": "¡Hola! ¿Cómo estás?",
            "como estas": "Muy bien, gracias. ¿Y tú?",
            "de que te gustaria hablar": "Podemos hablar de tecnología, música o lo que quieras."
        }

def guardar_conocimiento(conocimiento):
    """
    Guarda el conocimiento en el archivo JSON,
    para que no se pierda al cerrar el programa.
    """
    with open(archivo_conocimiento, "w", encoding="utf-8") as f:
        json.dump(conocimiento, f, indent=4, ensure_ascii=False)

def chat():
    """
    Inicia el chat en consola.
    Si el usuario pregunta algo que no está en la base de conocimiento,
    se le pedirá la respuesta y se guardará automáticamente.
    """
    conocimiento = cargar_conocimiento()
    print("Chat iniciado. Escribe 'salir' para terminar.\n")
    
    while True:
        # Se lee la pregunta del usuario
        pregunta = input("Tú: ").strip().lower()
        
        # Opción para terminar el chat
        if pregunta == "salir":
            print("Chat finalizado.")
            break
        
        # Si la pregunta ya existe en la base, se responde
        if pregunta in conocimiento:
            print("Bot:", conocimiento[pregunta])
        else:
            # Si no se conoce la respuesta, se pide al usuario enseñarla
            print("Bot: No conozco esa respuesta.")
            nueva = input("¿Qué debería responder a eso?: ").strip()
            conocimiento[pregunta] = nueva
            # Se guarda el nuevo conocimiento en el archivo
            guardar_conocimiento(conocimiento)
            print("Bot: Gracias, he aprendido algo nuevo.")

if __name__ == "__main__":
    chat()
