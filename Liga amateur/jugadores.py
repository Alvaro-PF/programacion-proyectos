import utilidades

contador_id = 4
opcion = 0

def alta_jugador():
    global contador_id
    nombre = input("Introduce nombre: ")
    while nombre == "":
        print("Campo no puede estar vacío")
        nombre = input("Introduce nombre: ")

    for jugador in utilidades.jugadores:
        if jugador["nombre"].lower() == nombre.lower():
            print("El jugador ya existe")
            return

    posicion = input("Introduce la posición: ")
    while posicion == "":
        print("Campo no puede estar vacío")
        posicion = input("Introduce la posición: ")

    equipo_id = input("Introduce el ID del equipo: ")
    equipo_valido = any(str(e["id"]) == equipo_id and e["activo"] for e in utilidades.equipos)
    while not equipo_valido:
        print("El equipo no existe o está inactivo")
        equipo_id = input("Introduce el ID del equipo: ")
        equipo_valido = any(str(e["id"]) == equipo_id and e["activo"] for e in utilidades.equipos)

    contador_id += 1
    nuevo_jugador = {
        "id": contador_id,
        "nombre": nombre,
        "posición": posicion,
        "equipo_id": int(equipo_id),
        "activo": True
    }
    utilidades.jugadores.append(nuevo_jugador)
    print("Jugador añadido")

def buscar_por_id():
    id_jugador = input("Id del jugador: ")
    for jugador in utilidades.jugadores:
        if str(jugador["id"]) == id_jugador:
            print(list(jugador.values()))
            return
    print("Jugador no encontrado")

def actualizar_por_id():
    id_jugador = input("Id jugador a actualizar: ")
    for jugador in utilidades.jugadores:
        if str(jugador["id"]) == id_jugador:
            nuevo_nombre = input(f"Nuevo nombre (actual: {jugador['nombre']}): ")
            if nuevo_nombre:
                jugador["nombre"] = nuevo_nombre
            nueva_posicion = input(f"Nueva posición (actual: {jugador['posición']}): ")
            if nueva_posicion:
                jugador["posición"] = nueva_posicion
            print("Jugador actualizado")
            return
    print("Jugador no encontrado")

def eliminar_jugador():
    id_jugador = input("Id jugador a eliminar: ")
    for jugador in utilidades.jugadores:
        if str(jugador["id"]) == id_jugador:
            jugador["activo"] = False
            print("Eliminado (marcado como inactivo)")
            return
    print("Jugador no encontrado")

def menu_jugadores():
    opcion = 0
    while opcion != 6:
        utilidades.mostrar_menu(utilidades.menu_jugadores)
        opcion = int(input("Qué hacer: "))
        match opcion:
            case 1:
                alta_jugador()
            case 2:
                utilidades.listar_jugadores()
            case 3:
                buscar_por_id()
            case 4:
                actualizar_por_id()
            case 5:
                eliminar_jugador()
            case 6:
                print("Volviendo al menú principal")
            case _:
                print("Opción no válida")