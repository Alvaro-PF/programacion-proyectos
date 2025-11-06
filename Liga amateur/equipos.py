import utilidades

contador_id = 4
opcion = 0

def crear_equipo():
    global contador_id
    nombre = input("Introduce nombre: ")
    while nombre == "":
        print("Campo no puede estar vacío")
        nombre = input("Introduce nombre: ")

    for equipo in utilidades.equipos:
        if equipo["nombre"].lower() == nombre.lower():
            print("El equipo ya existe")
            return

    ciudad = input("Introduce la ciudad: ")
    while ciudad == "":
        print("Campo no puede estar vacío")
        ciudad = input("Introduce la ciudad: ")

    contador_id += 1
    nuevo_equipo = {
        "id": contador_id,
        "nombre": nombre,
        "ciudad": ciudad,
        "activo": True
    }
    utilidades.equipos.append(nuevo_equipo)
    print("Equipo añadido")

def buscar_por_id():
    id_equipo = input("Id del equipo: ")
    for equipo in utilidades.equipos:
        if str(equipo["id"]) == id_equipo:
            print(list(equipo.values()))
            return
    print("Equipo no encontrado")

def actualizar_por_id():
    id_equipo = input("Id equipo a actualizar: ")
    for equipo in utilidades.equipos:
        if str(equipo["id"]) == id_equipo:
            nuevo_nombre = input(f"Nuevo nombre (actual: {equipo['nombre']}): ")
            if nuevo_nombre:
                equipo["nombre"] = nuevo_nombre
            nueva_ciudad = input(f"Nueva ciudad (actual: {equipo['ciudad']}): ")
            if nueva_ciudad:
                equipo["ciudad"] = nueva_ciudad
            print("Equipo actualizado")
            return
    print("Equipo no encontrado")

def eliminar_equipo():
    id_equipo = input("Id equipo a eliminar: ")
    for equipo in utilidades.equipos:
        if str(equipo["id"]) == id_equipo:
            equipo["activo"] = False
            print("Eliminado (marcado como inactivo)")
            return
    print("Equipo no encontrado")

def menu_equipos():
    opcion = 0
    while opcion != 6:
        utilidades.mostrar_menu(utilidades.menu_equipos)
        opcion = int(input("Qué hacer: "))
        match opcion:
            case 1:
                crear_equipo()
            case 2:
                utilidades.listar_equipos()
            case 3:
                buscar_por_id()
            case 4:
                actualizar_por_id()
            case 5:
                eliminar_equipo()
            case 6:
                print("Volviendo al menú principal")
            case _:
                print("Opción no válida")