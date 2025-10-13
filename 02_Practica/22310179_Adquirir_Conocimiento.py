import json
import os

# Constantes para el manejo de archivos
FILE_NAME = "datos.json"

def cargar_conocimiento():
    """Carga el conocimiento desde un archivo JSON, o retorna un conocimiento por defecto si el archivo no existe."""
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("Error al leer el archivo, se utilizarán datos por defecto.")
            return obtener_conocimiento_default()
    else:
        return obtener_conocimiento_default()

def obtener_conocimiento_default():
    """Devuelve la base de conocimiento predeterminada."""
    return {
        "hola": "¡Hola!",
        "como estas": "Estoy bien,y tú?",
        "te gustaria hablar?": "Podemos hablar de música o lo que sea."
    }

def guardar_conocimiento(knowledge_base):
    """Guarda el conocimiento actualizado en el archivo JSON."""
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(knowledge_base, file, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Error al guardar el archivo: {e}")

def procesar_entrada_usuario(user_input, knowledge_base):
    """Procesa la entrada del usuario y responde según el conocimiento."""
    user_input = user_input.lower().strip()

    if user_input == "salir":
        return False  # Termina el chat
    elif user_input in knowledge_base:
        print(f"Bot: {knowledge_base[user_input]}")
    else:
        print("Bot: No conozco esa respuesta.")
        nueva_respuesta = input("¿Qué debería responder cuando digan eso?: ")
        knowledge_base[user_input] = nueva_respuesta
        print("Bot: Gracias, he aprendido algo nuevo!")
    return True  # Continúa el chat

def iniciar_chat():
    """Inicia el chat y permite la interacción con el usuario."""
    knowledge_base = cargar_conocimiento()
    print("=== Bienvenido al Chat con Aprendizaje ===")
    print("Escribe 'salir' para terminar.\n")

    while True:
        user_input = input("Tú: ")
        if not procesar_entrada_usuario(user_input, knowledge_base):
            guardar_conocimiento(knowledge_base)
            print("Chat finalizado. ¡Hasta luego!")
            break

if __name__ == "__main__":
    iniciar_chat()
