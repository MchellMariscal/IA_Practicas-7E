# Ejemplo de Modus Ponens
# Regla: Si P -> Q, y P es verdadero, entonces Q es verdadero

# Premisas
P = True   # Está lloviendo
Q = True   # La calle está mojada

print("Ejemplo Modus Ponens:")
print("Si llueve, entonces la calle estará mojada.")

if P:
    print("Está lloviendo.")
    if Q:
        print("Por lo tanto, la calle está mojada.")
    else:
        print("Algo no cuadra con la inferencia.")
