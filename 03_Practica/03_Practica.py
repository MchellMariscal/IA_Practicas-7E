# -------------------------------
# 🎶 ADIVINA LA CANCIÓN - SODA STEREO & GUSTAVO CERATI 🎶
# Juego de adivinanza con aprendizaje automático
# -------------------------------

# Importamos librerías necesarias
import json   # Para guardar y cargar el conocimiento en formato JSON
import os     # Para verificar si el archivo de conocimiento existe

# Nombre del archivo donde se guardará la base de datos del juego
ARCHIVO_CONOCIMIENTO = "canciones_cerati.json"


# ----------------------------------------
# 🔹 FUNCIÓN: cargar_conocimiento()
# Carga la base de datos de canciones y preguntas si existe.
# Si no existe, crea una base inicial con algunas canciones.
# ----------------------------------------
def cargar_conocimiento():
    # Si ya existe el archivo JSON, lo abrimos y lo leemos
    if os.path.exists(ARCHIVO_CONOCIMIENTO):
        with open(ARCHIVO_CONOCIMIENTO, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        # Si no existe, se crea una base de conocimiento inicial
        # con preguntas básicas y algunas canciones de inicio
        return {
            "pregunta": "¿Es una canción de Soda Stereo?",  # Primera pregunta raíz
            "si": {  # Si el usuario responde "sí"...
                "pregunta": "¿La canción es de los años 80?",
                "si": {
                    "pregunta": "¿Tiene un sonido muy rockero?",
                    "si": {"cancion": "Nada Personal"},
                    "no": {"cancion": "Trátame Suavemente"}
                },
                "no": {
                    "pregunta": "¿Es una de las canciones más famosas?",
                    "si": {"cancion": "De Música Ligera"},
                    "no": {"cancion": "Zoom"}
                }
            },
            "no": {  # Si el usuario responde "no" (es de Cerati solista)
                "pregunta": "¿Pertenece al álbum Bocanada?",
                "si": {"cancion": "Puente"},
                "no": {
                    "pregunta": "¿Pertenece a su etapa final como solista?",
                    "si": {"cancion": "Crimen"},
                    "no": {"cancion": "Cosas Imposibles"}
                }
            }
        }


# ----------------------------------------
# 🔹 FUNCIÓN: guardar_conocimiento(data)
# Guarda la información aprendida en el archivo JSON
# ----------------------------------------
def guardar_conocimiento(data):
    # Se abre el archivo y se guarda el contenido actualizado del árbol
    with open(ARCHIVO_CONOCIMIENTO, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


# ----------------------------------------
# 🔹 FUNCIÓN: jugar(nodo)
# Es la parte principal del juego.
# Recorre el árbol de preguntas hasta llegar a una canción final.
# ----------------------------------------
def jugar(nodo):
    # Si el nodo contiene una canción, estamos en una hoja del árbol
    if "cancion" in nodo:
        respuesta = input(f"¿Tu canción es '{nodo['cancion']}'? (si/no): ").strip().lower()
        if respuesta == "si":
            print("🎸 ¡La adiviné! Soy un genio del rock argentino 😎")
            return nodo  # No cambia el árbol, ya la conocía
        else:
            # Si no la adivinó, se llama a la función aprender()
            return aprender(nodo)
    else:
        # Si es una pregunta, la mostramos al usuario
        respuesta = input(nodo["pregunta"] + " (si/no): ").strip().lower()
        # Si responde "sí", seguimos por la rama "si"
        if respuesta == "si":
            nodo["si"] = jugar(nodo["si"])
        # Si responde "no", seguimos por la rama "no"
        else:
            nodo["no"] = jugar(nodo["no"])
        # Retornamos el nodo actualizado (por si aprendió algo nuevo)
        return nodo


# ----------------------------------------
# 🔹 FUNCIÓN: aprender(nodo)
# Se ejecuta cuando el programa no logra adivinar la canción.
# El usuario enseña una nueva canción y una pregunta que la diferencie.
# ----------------------------------------
def aprender(nodo):
    # Pedimos al usuario el nombre de la canción que pensaba
    nueva_cancion = input("😅 No la conozco... ¿Cuál era tu canción?: ").strip()
    
    # Pedimos una pregunta para poder distinguir entre la nueva canción y la anterior
    nueva_pregunta = input(
        f"Escribe una pregunta para diferenciar '{nueva_cancion}' de '{nodo['cancion']}'\n"
        f"(responde 'sí' para '{nueva_cancion}' y 'no' para '{nodo['cancion']}'):\n> "
    ).strip()
    
    # Creamos un nuevo nodo (pregunta) con dos respuestas
    return {
        "pregunta": nueva_pregunta,
        "si": {"cancion": nueva_cancion},  # Respuesta afirmativa: la nueva canción
        "no": nodo                         # Respuesta negativa: la anterior
    }


# ----------------------------------------
# 🔹 FUNCIÓN: main()
# Es el punto principal del programa. Controla el flujo general.
# ----------------------------------------
def main():
    # Mensaje de bienvenida
    print("🎶 Bienvenido al Adivinador de Canciones de Soda Stereo y Gustavo Cerati 🎶")
    print("Responde solo con 'si' o 'no'.\n")

    # Cargamos o creamos el conocimiento inicial
    conocimiento = cargar_conocimiento()

    # Bucle principal del juego
    while True:
        # Llamamos a la función principal que hace las preguntas
        conocimiento = jugar(conocimiento)
        
        # Guardamos lo aprendido después de cada partida
        guardar_conocimiento(conocimiento)

        # Preguntamos si el jugador quiere continuar
        otra = input("\n¿Quieres jugar otra vez? (si/no): ").strip().lower()
        if otra != "si":
            print("👋 ¡Gracias por jugar! Nos vemos en la próxima canción.")
            break


# ----------------------------------------
# 🔹 Punto de entrada
# Esta línea asegura que el juego se ejecute solo si el archivo se corre directamente.
# ----------------------------------------
if __name__ == "__main__":
    main()
