import tabulate

# Listas existentes
equipos = [
    {"id": 1, "nombre": "Parla escuela", "ciudad": "Parla", "activo": True},
    {"id": 2, "nombre": "Real Madrid", "ciudad": "Chamartín", "activo": True},
    {"id": 3, "nombre": "Atlético de Madrid", "ciudad": "Vicálvaro", "activo": True},
    {"id": 4, "nombre": "Rayo Vallecano", "ciudad": "Vallecas", "activo": False}
]

jugadores = [
    {"id": 1, "nombre": "Laura", "posición": "Delantera", "equipo_id":1, "activo": True},
    {"id": 2, "nombre": "Marcos", "posición": "Mediocentro", "equipo_id":2, "activo": True},
    {"id": 3, "nombre": "Juan", "posición": "Defensa", "equipo_id":3, "activo": True},
    {"id": 4, "nombre": "Maria", "posición": "Portera", "equipo_id":4, "activo": False}
]

# Nueva lista de partidos
partidos = [    
    {"id": 1, "jornada": 1, "local_id": 1, "visitante_id": 2, "fecha": "2025-11-10", "hora": "18:30", "jugado": False, "resultado": None},
    {"id": 2, "jornada": 1, "local_id": 3, "visitante_id": 4, "fecha": "2025-11-10", "hora": "20:00", "jugado": False, "resultado": None},
    {"id": 3, "jornada": 2, "local_id": 2, "visitante_id": 3, "fecha": "2025-11-17", "hora": "18:30", "jugado": False, "resultado": None},
    {"id": 4, "jornada": 2, "local_id": 4, "visitante_id": 1, "fecha": "2025-11-17", "hora": "20:00", "jugado": False, "resultado": None},
    {"id": 5, "jornada": 3, "local_id": 1, "visitante_id": 3, "fecha": "2025-11-22", "hora": "18:30", "jugado": False, "resultado": None}
]

# Menús
menu_equipos = ["Crear equipo","Listar equipos","Buscar por id","Actualizar datos","Eliminar equipo","Volver al menú principal"]
menu_jugadores = ["Alta de jugador","Listar jugadores","Buscar por id","Actualizar","Eliminar jugador","Volver al menú principal"]
menu_partidos = ["Crear partido","Listar partidos","Listar por jornada","Reprogramar partido","Eliminar partido","Volver al menú principal"]
menu_principal = ["Menú de equipos","Menú de jugadores","Menú de partidos", "Menu ranking", "Salir del programa"]

# Función para mostrar menú
def mostrar_menu(menu):
    for i, opcion in enumerate(menu, 1):
        print(i, opcion)

# Función para listar equipos activos
def listar_equipos():
    activos = [equipo for equipo in equipos if equipo["activo"]]
    print(tabulate.tabulate(activos, headers="keys", tablefmt="grid"))

# Función para listar jugadores activos
def listar_jugadores():
    activos = [jugador for jugador in jugadores if jugador["activo"]]
    if not activos:
        print("No hay jugadores activos")
        return
    tabla = []
    for j in activos:
        equipo_nombre = next((e["nombre"] for e in equipos if e["id"] == j["equipo_id"]), "Desconocido")
        tabla.append({
            "ID": j["id"],
            "Nombre": j["nombre"],
            "Posición": j["posición"],
            "Equipo": equipo_nombre,
            "Activo": j["activo"]
        })
    print(tabulate.tabulate(tabla, headers="keys", tablefmt="grid"))

# Función para mostrar partidos
def listar_partidos(partidos_filtrados=None):
    from tabulate import tabulate
    if partidos_filtrados is None:
        partidos_filtrados = partidos
    if not partidos_filtrados:
        print("No hay partidos para mostrar")
        return
    tabla = []
    for p in partidos_filtrados:
        local = next((e["nombre"] for e in equipos if e["id"] == p["local_id"]), "Desconocido")
        visitante = next((e["nombre"] for e in equipos if e["id"] == p["visitante_id"]), "Desconocido")
        tabla.append({
            "ID": p["id"],
            "Jornada": p["jornada"],
            "Local": local,
            "Visitante": visitante,
            "Fecha": p["fecha"],
            "Hora": p["hora"],
            "Jugado": p["jugado"],
            "Resultado": p["resultado"]
        })
    print(tabulate(tabla, headers="keys", tablefmt="grid"))