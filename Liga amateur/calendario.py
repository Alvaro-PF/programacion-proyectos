import utilidades
import datetime

contador_id = 0
opcion = 0

def crear_partido():
    global contador_id
    try:
        jornada = int(input("Introduce la jornada (>=1): "))
        if jornada < 1:
            print("Jornada debe ser ≥ 1")
            return
    except ValueError:
        print("Valor incorrecto")
        return

    local_id = input("ID equipo local: ")
    visitante_id = input("ID equipo visitante: ")

    if local_id == visitante_id:
        print("No se puede enfrentar un equipo consigo mismo")
        return

    local = next((e for e in utilidades.equipos if str(e["id"]) == local_id and e["activo"]), None)
    visitante = next((e for e in utilidades.equipos if str(e["id"]) == visitante_id and e["activo"]), None)
    if not local or not visitante:
        print("Uno o ambos equipos no existen o están inactivos")
        return

    # Evitar duplicados en la misma jornada
    for p in utilidades.partidos:
        if p["jornada"] == jornada and ((p["local_id"] == int(local_id) and p["visitante_id"] == int(visitante_id)) or
                                        (p["local_id"] == int(visitante_id) and p["visitante_id"] == int(local_id))):
            print("Este enfrentamiento ya existe en la jornada")
            return

    fecha = input("Fecha (AAAA-MM-DD): ")
    hora = input("Hora (HH:MM): ")
    try:
        datetime.datetime.strptime(f"{fecha} {hora}", "%Y-%m-%d %H:%M")
    except ValueError:
        print("Fecha u hora inválida")
        return

    contador_id += 1
    partido = {
        "id": contador_id,
        "jornada": jornada,
        "local_id": int(local_id),
        "visitante_id": int(visitante_id),
        "fecha": fecha,
        "hora": hora,
        "jugado": False,
        "resultado": None
    }
    utilidades.partidos.append(partido)
    print("Partido creado")

def listar_partidos():
    utilidades.listar_partidos()

def listar_por_jornada():
    try:
        j = int(input("Introduce jornada: "))
    except ValueError:
        print("Valor inválido")
        return
    partidos_j = [p for p in utilidades.partidos if p["jornada"] == j]
    utilidades.listar_partidos(partidos_j)

def reprogramar_partido():
    id_p = input("ID del partido a reprogramar: ")
    p = next((x for x in utilidades.partidos if str(x["id"]) == id_p), None)
    if not p:
        print("Partido no encontrado")
        return
    if p["jugado"]:
        print("No se puede reprogramar un partido ya jugado")
        return
    fecha = input(f"Nueva fecha (actual: {p['fecha']}): ")
    hora = input(f"Nueva hora (actual: {p['hora']}): ")
    try:
        datetime.datetime.strptime(f"{fecha} {hora}", "%Y-%m-%d %H:%M")
    except ValueError:
        print("Fecha u hora inválida")
        return
    p["fecha"] = fecha
    p["hora"] = hora
    print("Partido reprogramado")

def eliminar_partido():
    id_p = input("ID del partido a eliminar: ")
    p = next((x for x in utilidades.partidos if str(x["id"]) == id_p), None)
    if not p:
        print("Partido no encontrado")
        return
    if p["jugado"]:
        print("No se puede eliminar un partido ya jugado")
        return
    utilidades.partidos.remove(p)
    print("Partido eliminado")

def menu_partidos():
    opcion = 0
    while opcion != 6:
        utilidades.mostrar_menu(utilidades.menu_partidos)
        opcion = int(input("Qué hacer: "))
        match opcion:
            case 1:
                crear_partido()
            case 2:
                listar_partidos()
            case 3:
                listar_por_jornada()
            case 4:
                reprogramar_partido()
            case 5:
                eliminar_partido()
            case 6:
                print("Volviendo al menú principal")
            case _:
                print("Opción no válida")