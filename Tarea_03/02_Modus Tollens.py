# Ejemplo de Modus Tollens
# Regla: Si P -> Q, y Q es falso, entonces P es falso

# Premisas
P = True    # Estudié
Q = False   # No aprobé el examen

print("\nEjemplo Modus Tollens:")
print("Si estudio, entonces aprobaré el examen.")

if not Q:
    print("No aprobé el examen.")
    print("Por lo tanto, no estudié.")
