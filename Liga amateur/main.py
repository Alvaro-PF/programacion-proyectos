import equipos
import jugadores
import calendario
import ranking
import utilidades

opcion = 0
while opcion != 5:
    utilidades.mostrar_menu(utilidades.menu_principal)
    try:
        opcion = int(input("Elige una opción: "))
    except ValueError:
        print("Opción inválida")
        continue
    match opcion:
        case 1:
            equipos.menu_equipos()
        case 2:
            jugadores.menu_jugadores()
        case 3:
            calendario.menu_partidos()
        case 4:
            ranking.menu_resultados()
        case 5:
            print("Saliendo del programa")
        case _:
            print("Opción no válida")
