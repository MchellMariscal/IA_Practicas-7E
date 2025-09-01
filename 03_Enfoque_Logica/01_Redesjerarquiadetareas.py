# HTN para organizar una fiesta
htn = {
    "organizar_fiesta": ["comprar_comida", "decorar", "limpiar_casa"],  
    "comprar_comida": ["hacer_lista", "ir_supermercado", "guardar_comida"],
    "decorar": ["colocar_globos", "poner_musica", "acomodar_mesas"],
    "limpiar_casa": ["barrer", "trapear", "sacar_basura"]
}

# Función para planificar una tarea jerárquica
def planificar_htn(tarea):
    if tarea in htn:  
        return [planificar_htn(sub) for sub in htn[tarea]]
    else:
        return tarea  

# Ejecutamos el plan jerárquico
print("Plan jerárquico:", planificar_htn("organizar_fiesta"))
