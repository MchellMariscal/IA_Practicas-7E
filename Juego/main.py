import pygame
import random
import json
import os
import sys

pygame.init()

ANCHO, ALTO = 900, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Adivina la Canción - Soda Stereo & Gustavo Cerati")

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
fuente = pygame.font.Font(None, 40)
pequena = pygame.font.Font(None, 28)

DATA_FILE = "songs_150.json"

# 🔹 Cargar canciones o crear lista vacía si no existe
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        try:
            canciones = json.load(f)
        except json.JSONDecodeError:
            canciones = []
else:
    canciones = []

# 🔹 Si no hay canciones, crear una por defecto
if not canciones:
    print("⚠️ No se encontraron canciones. Se agregará una de ejemplo.")
    canciones = [
        {
            "titulo": "Persiana Americana",
            "artista": "Soda Stereo",
            "album": "Signos",
            "anio": 1986,
            "emocion": "energética",
            "portada": "portadas/soda_signos.jpg"
        }
    ]
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(canciones, f, ensure_ascii=False, indent=2)

def mostrar_texto(texto, y, color=BLANCO):
    superficie = fuente.render(texto, True, color)
    rect = superficie.get_rect(center=(ANCHO//2, y))
    ventana.blit(superficie, rect)

def mostrar_portada(ruta_imagen):
    try:
        imagen = pygame.image.load(ruta_imagen)
        imagen = pygame.transform.scale(imagen, (400, 400))
        ventana.blit(imagen, (ANCHO//2 - 200, 120))
    except:
        mostrar_texto("No se encontró la portada.", 300, (255, 100, 100))

def guardar_canciones():
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(canciones, f, ensure_ascii=False, indent=2)

# 🔹 Canción inicial
cancion_actual = random.choice(canciones)
mensaje = f"¿La canción pertenece al álbum '{cancion_actual['album']}'?"
mostrar_imagen = False
ejecutando = True

while ejecutando:
    ventana.fill(NEGRO)
    mostrar_texto("Adivina la canción 🎵", 60)
    mostrar_texto(mensaje, 150)
    mostrar_texto("Presiona: S = Sí | N = No | Espacio = Siguiente | Q = Salir", 520, (200, 200, 200))

    if mostrar_imagen:
        mostrar_portada(cancion_actual["portada"])
        mostrar_texto(f"🎶 {cancion_actual['titulo']} ({cancion_actual['anio']})", 90, (180, 220, 255))

    pygame.display.flip()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_q:
                ejecutando = False
            elif evento.key == pygame.K_s:
                mostrar_imagen = True
            elif evento.key == pygame.K_n:
                print("\n🤖 Nueva canción detectada. Vamos a agregarla.")
                titulo = input("Título de la canción: ")
                artista = input("Artista: ")
                album = input("Álbum: ")
                anio = input("Año: ")
                emocion = input("Emoción: ")
                portada = input("Ruta de portada (portadas/xxx.jpg): ")
                nueva = {
                    "titulo": titulo,
                    "artista": artista,
                    "album": album,
                    "anio": int(anio),
                    "emocion": emocion,
                    "portada": portada
                }
                canciones.append(nueva)
                guardar_canciones()
                print("✅ Canción agregada con éxito.")
                cancion_actual = random.choice(canciones)
                mensaje = f"¿La canción pertenece al álbum '{cancion_actual['album']}'?"
                mostrar_imagen = False
            elif evento.key == pygame.K_SPACE:
                cancion_actual = random.choice(canciones)
                mensaje = f"¿La canción pertenece al álbum '{cancion_actual['album']}'?"
                mostrar_imagen = False

pygame.quit()
sys.exit()
