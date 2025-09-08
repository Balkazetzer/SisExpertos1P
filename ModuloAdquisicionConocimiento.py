import json
import os

archivo_conocimiento = "conocimiento.json"

def cargar_conocimiento():
    if os.path.exists(archivo_conocimiento):
        with open(archivo_conocimiento, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        # Conocimiento base precargado
        return {
            "hola": "¡Hola! ¿Cómo estás?",
            "como estas": "Muy bien, gracias. ¿Y tú?",
            "de que te gustaria hablar": "Podemos hablar de tecnología, música o lo que quieras."
        }

def guardar_conocimiento(conocimiento):
    with open(archivo_conocimiento, "w", encoding="utf-8") as f:
        json.dump(conocimiento, f, indent=4, ensure_ascii=False)

def chat():
    conocimiento = cargar_conocimiento()
    print("Chat iniciado. Escribe 'salir' para terminar.\n")
    
    while True:
        pregunta = input("Tú: ").strip().lower()
        
        if pregunta == "salir":
            print("Chat finalizado.")
            break
        
        if pregunta in conocimiento:
            print("Bot:", conocimiento[pregunta])
        else:
            print("Bot: No conozco esa respuesta.")
            nueva = input("¿Qué debería responder a eso?: ").strip()
            conocimiento[pregunta] = nueva
            guardar_conocimiento(conocimiento)
            print("Bot: Gracias, he aprendido algo nuevo.")

if __name__ == "__main__":
    chat()
