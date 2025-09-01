import random

# Preferencias de disponibilidad por empleado
# Empleado 0 prefiere los turnos 0 o 1, etc.
preferencias = {
    0: [0, 1],
    1: [1, 2],
    2: [0, 2],
    3: [1],
    4: [0, 2, 3],
    5: [2, 3],
    6: [0, 3],
    7: [1, 3]
}

n = len(preferencias)  # Número de empleados

# Función para contar conflictos: solo si el turno no está en sus preferencias
def contar_conflictos(asignaciones, empleado, turno):
    return 0 if turno in preferencias[empleado] else 1

# Encuentra el turno con el menor número de conflictos para un empleado
def encontrar_turno_min_conflictos(asignaciones, empleado):
    min_conflictos = float('inf')
    mejores_turnos = []

    for turno in range(n):  # Se asume que hay n posibles turnos (0 a n-1)
        conflictos = contar_conflictos(asignaciones, empleado, turno)
        if conflictos < min_conflictos:
            min_conflictos = conflictos
            mejores_turnos = [turno]
        elif conflictos == min_conflictos:
            mejores_turnos.append(turno)

    return random.choice(mejores_turnos)

# Algoritmo de mínimos conflictos
def asignar_turnos(n, max_iter=1000):
    asignaciones = [random.randint(0, n - 1) for _ in range(n)]  # Asignación inicial

    for _ in range(max_iter):
        conflictos = [emp for emp in range(n) if contar_conflictos(asignaciones, emp, asignaciones[emp]) > 0]

        if not conflictos:
            return asignaciones  # Solución sin conflictos

        emp = random.choice(conflictos)
        asignaciones[emp] = encontrar_turno_min_conflictos(asignaciones, emp)

    return asignaciones  # Retorna mejor asignación encontrada

# Ejecutar el algoritmo
asignaciones = asignar_turnos(n)

# Mostrar resultados
print("Asignación de turnos:")
for empleado, turno in enumerate(asignaciones):
    conflicto = "" if turno in preferencias[empleado] else "❌ NO preferido"
    print(f"Empleado {empleado} → Turno {turno} {conflicto}")
