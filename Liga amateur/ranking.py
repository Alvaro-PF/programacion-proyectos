import utilidades

opcion = 0

def registrar_resultado():
    # Mostrar partidos pendientes
    pendientes = [p for p in utilidades.partidos if not p["jugado"]]
    if not pendientes:
        print("No hay partidos pendientes")
        return
    utilidades.listar_partidos(pendientes)
    
    id_p = input("Introduce el ID del partido a registrar: ")
    partido = next((p for p in pendientes if str(p["id"]) == id_p), None)
    if not partido:
        print("ID inválido o partido ya jugado")
        return

    try:
        gL = int(input("Goles equipo local: "))
        gV = int(input("Goles equipo visitante: "))
        if gL < 0 or gV < 0:
            raise ValueError
    except ValueError:
        print("Los goles deben ser enteros ≥ 0")
        return

    partido["resultado"] = (gL, gV)
    partido["jugado"] = True
    print("Resultado registrado")

def clasificacion():
    tabla = {}
    for e in utilidades.equipos:
        tabla[e["id"]] = {"Equipo": e["nombre"], "PJ":0,"G":0,"E":0,"P":0,"GF":0,"GC":0,"DG":0,"PTS":0}

    for p in utilidades.partidos:
        if not p["jugado"]:
            continue
        local = tabla[p["local_id"]]
        visitante = tabla[p["visitante_id"]]
        gL, gV = p["resultado"]

        local["PJ"] += 1
        visitante["PJ"] += 1
        local["GF"] += gL
        local["GC"] += gV
        visitante["GF"] += gV
        visitante["GC"] += gL

        if gL > gV:
            local["G"] += 1
            visitante["P"] += 1
            local["PTS"] += 3
        elif gL < gV:
            visitante["G"] += 1
            local["P"] += 1
            visitante["PTS"] += 3
        else:
            local["E"] += 1
            visitante["E"] += 1
            local["PTS"] += 1
            visitante["PTS"] += 1

    for e in tabla.values():
        e["DG"] = e["GF"] - e["GC"]

    # Ordenar por PTS desc, luego DG desc, luego GF desc
    lista = sorted(tabla.values(), key=lambda x: (x["PTS"], x["DG"], x["GF"]), reverse=True)
    
    from tabulate import tabulate
    print(tabulate(lista, headers="keys", tablefmt="grid"))

def estadisticas_equipo():
    try:
        equipo_id = int(input("Introduce el ID del equipo: "))
    except ValueError:
        print("ID inválido")
        return

    e = next((eq for eq in utilidades.equipos if eq["id"] == equipo_id), None)
    if not e:
        print("Equipo no encontrado")
        return

    resumen = {"PJ":0,"G":0,"E":0,"P":0,"GF":0,"GC":0,"DG":0,"PTS":0}
    for p in utilidades.partidos:
        if not p["jugado"]:
            continue
        if p["local_id"] == equipo_id:
            gL, gV = p["resultado"]
            resumen["PJ"] +=1
            resumen["GF"] += gL
            resumen["GC"] += gV
            if gL>gV:
                resumen["G"] +=1
                resumen["PTS"] +=3
            elif gL<gV:
                resumen["P"] +=1
            else:
                resumen["E"] +=1
                resumen["PTS"] +=1
        elif p["visitante_id"] == equipo_id:
            gL, gV = p["resultado"]
            resumen["PJ"] +=1
            resumen["GF"] += gV
            resumen["GC"] += gL
            if gV>gL:
                resumen["G"] +=1
                resumen["PTS"] +=3
            elif gV<gL:
                resumen["P"] +=1
            else:
                resumen["E"] +=1
                resumen["PTS"] +=1
    resumen["DG"] = resumen["GF"] - resumen["GC"]
    from tabulate import tabulate
    print(tabulate([resumen], headers="keys", tablefmt="grid"))

def menu_resultados():
    opcion = 0
    while opcion != 4:
        menu = ["Registrar resultado","Ver clasificación","Estadísticas de equipo","Volver al menú principal"]
        utilidades.mostrar_menu(menu)
        try:
            opcion = int(input("Qué hacer: "))
        except ValueError:
            print("Opción inválida")
            continue

        match opcion:
            case 1:
                registrar_resultado()
            case 2:
                clasificacion()
            case 3:
                estadisticas_equipo()
            case 4:
                print("Volviendo al menú principal")
            case _:
                print("Opción no válida")
