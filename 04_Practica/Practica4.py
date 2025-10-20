import random

# --- Datos del juego ---
culpables = ["Edwin Grey", "Mary Lou", "Sheriff Miller", "Dr. Harlan", "Lucy Harper"]
armas = ["Hacha oxidada", "Cuchillo de carnicero", "Revólver antiguo", "Llave inglesa", "Cuerda de cáñamo"]
lugares = ["Granja abandonada", "Motel Red Creek", "Comisaría del pueblo", "Tienda de antigüedades", "Bosque de Plainfield"]

# --- Elección secreta ---
culpable_real = random.choice(culpables)
arma_real = random.choice(armas)
lugar_real = random.choice(lugares)

print("🩸 BIENVENIDO AL MISTERIO DE PLAINFIELD 🩸")
print("\nHa ocurrido un crimen en el pueblo. Deberás interrogar, investigar y deducir quién fue el culpable.\n")

print("Personas sospechosas:", culpables)
print("Lugares a investigar:", lugares)
print("Posibles armas:", armas)
print("\nTienes 5 intentos para resolver el caso...\n")

intentos = 5

# --- Juego principal ---
while intentos > 0:
    print(f"Intentos restantes: {intentos}")
    culpable = input("\n👤 ¿A quién acusas?: ").strip()
    arma = input("🔪 ¿Con qué arma crees que fue?: ").strip()
    lugar = input("🏚️ ¿Dónde ocurrió?: ").strip()

    aciertos = 0
    pistas = []

    # --- Culpable ---
    if culpable == culpable_real:
        aciertos += 1
        pistas.append(f"🕵️ Se confirma que {culpable} fue visto comportándose de forma extraña después del crimen.")
    else:
        pistas.append(f"❌ Algunos testigos aseguran que {culpable} no estaba cerca del lugar del crimen.")

    # --- Arma ---
    if arma == arma_real:
        aciertos += 1
        pistas.append(f"🔍 Se encontró una huella parcial en el {arma}.")
    else:
        pistas.append(f"❌ El {arma} fue revisado y no tenía relación con la escena.")

    # --- Lugar ---
    if lugar == lugar_real:
        aciertos += 1
        pistas.append(f"🏠 Vecinos escucharon ruidos extraños en el {lugar}.")
    else:
        pistas.append(f"❌ En el {lugar} no se hallaron evidencias importantes.")

    print("\nPistas del investigador:")
    for p in pistas:
        print(p)

    if aciertos == 3:
        print("\n🎉 ¡Has resuelto el misterio! 🎉")
        break

    intentos -= 1
    print("\nSigue investigando...\n")

# --- Finales narrativos ---
if aciertos == 3:
    print("\n📜 VEREDICTO FINAL 📜\n")
    if culpable_real == "Edwin Grey":
        print("El granjero Edwin Grey fue hallado en su vieja granja. Vecinos lo vieron entrar con una linterna y un hacha oxidada.")
        print("En su sótano se hallaron objetos pertenecientes a las víctimas. Fue detenido sin oponer resistencia.")
    elif culpable_real == "Mary Lou":
        print("Mary Lou, la mesera del Motel Red Creek, fue descubierta tras las cámaras de seguridad.")
        print("El cuchillo de carnicero con su nombre estaba en el cuarto 7, junto a las pertenencias de la víctima.")
    elif culpable_real == "Sheriff Miller":
        print("El Sheriff Miller trató de encubrir su crimen. En la comisaría se encontró su viejo revólver con una bala disparada.")
        print("La libreta de registros tenía fechas tachadas coincidiendo con las desapariciones.")
    elif culpable_real == "Dr. Harlan":
        print("El Dr. Harlan escondía un taller en la trastienda de su tienda de antigüedades.")
        print("La llave inglesa fue hallada con manchas sospechosas y restos de metal deformado.")
    elif culpable_real == "Lucy Harper":
        print("Lucy Harper, la periodista, se obsesionó con el caso. En el bosque de Plainfield se encontró su cámara junto a una cuerda de cáñamo.")
        print("Intentaba recrear la escena para escribir su última historia...")
    print("\nCaso cerrado. 🕯️")
else:
    print("\n💀 El caso no fue resuelto a tiempo...")
    print(f"La verdad era: {culpable_real} en {lugar_real} con {arma_real}.")
