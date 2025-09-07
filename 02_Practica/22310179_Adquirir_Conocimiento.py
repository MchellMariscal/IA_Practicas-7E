# Mini chat con adquisición de conocimiento
# Autor: Michell Mariscal
# Proyecto: Registro_Adquirir_Conocimiento

# Base de datos inicial (diccionario con pares pregunta-respuesta)
knowledge_base = {
    "hola": "¡Hola! ¿Cómo estás?",
    "como estas": "Estoy bien, gracias. ¿Y tú?",
    "de que te gustaria hablar": "Podemos hablar de tecnología, música o lo que quieras."
}

def chat():
    print("=== Bienvenido al Chat con Aprendizaje ===")
    print("Escribe 'salir' para terminar.\n")

    while True:
        user_input = input("Tú: ").lower().strip()

        if user_input == "salir":
            print("Chat finalizado. ¡Hasta luego!")
            break

        # Buscar respuesta en la base de datos
        if user_input in knowledge_base:
            print("Bot:", knowledge_base[user_input])
        else:
            print("Bot: No conozco esa respuesta.")
            new_response = input("¿Qué debería responder cuando digan eso?: ")
            # Guardar en la base de datos
            knowledge_base[user_input] = new_response
            print("Bot: Gracias, he aprendido algo nuevo!")

# Ejecutar chat
if __name__ == "__main__":
    chat()
