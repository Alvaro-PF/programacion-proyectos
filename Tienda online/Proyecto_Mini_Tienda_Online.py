# Lista de artículos disponibles en la tienda 
articulos = [ 
{"id": 1, "nombre": "Teclado", "precio": 25.0, "stock": 15, 
"activo": True}, 
{"id": 2, "nombre": "Monitor", "precio": 180.75, "stock": 8, 
"activo": True}, 
    {"id": 3, "nombre": "Auriculares", "precio": 45.9, "stock": 12, 
"activo": False}, 
    {"id": 4, "nombre": "Micrófono", "precio": 60.0, "stock": 5, 
"activo": True} 
] 
 
usuarios = [ 
    {"id": 1, "nombre": "Ana", "email": "ana@example.com", "activo": 
True}, 
    {"id": 2, "nombre": "Luis", "email": "luis@example.com", "activo": 
True}, 
    {"id": 3, "nombre": "Marta", "email": "marta@example.com", "activo": 
False}, 
    {"id": 4, "nombre": "Carlos", "email": "carlos@example.com", 
"activo": True} 
] 
 
#Nuevas estructuras para vender 
ventas = [] 
carrito_actual = [] 
usuario_activo = None 

# Modulos
from Proyecto_Mini_Tienda_Online_modulos import (crear_articulo, listar_articulo, buscar_articulo_id, actualizar_articulo, eliminar_articulo, articulo_activo_inactivo)
from Proyecto_Mini_Tienda_Online_modulos import (crear_usuario, listar_usuario, buscar_usuario_id, actualizar_usuario, eliminar_usuario, usuario_activo_inactivo)
from Proyecto_Mini_Tienda_Online_modulos import (seleccionar_usuario_activo, añadir_articulo_carrito, quitar_articulo_carrito, ver_carrito, confirmar_compra, historial_ventas_usuario, vaciar_carrito)

# Busca un artículo por ID 
def buscar_articulo_por_id(articulos, id_buscar): 
    for articulo in articulos: 
        if articulo["id"] == id_buscar: 
            return articulo 
    return None 
 
# Busca un usuario por ID 
def buscar_usuario_por_id(usuarios, id_buscar): 
    for usuario in usuarios: 
        if usuario["id"] == id_buscar: 
            return usuario 
    return None 
 
# Función que imprime las opciones disponibles del menú 
def mostrar_menu_articulos(): 
    menu = [ 
        "Crear artículo", 
        "Listar artículos", 
        "Buscar artículo por id", 
        "Actualizar artículo", 
        "Eliminar artículo", 
        "Alternar activo/inactivo", 
        "Salir" 
    ] 
    for i, opcion in enumerate(menu, 1): 
        print(i, opcion) 
 
# Función que gestiona la interacción con el usuario 
def menu_articulos(): 
    opcion = 0  # Variable que guarda la opción elegida 
    while opcion != 7:  # El bucle se repite hasta que se elija la opción 7 (salir) 
        mostrar_menu_articulos() 
        opcion = int(input("Elige una opción (1-7): "))  # Se pide al usuario una opción 
        match opcion: 
            case 1: 
                crear_articulo(articulos)
 
            case 2: 
                listar_articulo(articulos) 
 
            case 3: 
                buscar_articulo_id(articulos)
 
            case 4: 
                actualizar_articulo(articulos)
 
            case 5: 
                eliminar_articulo(articulos)
 
            case 6: 
                articulo_activo_inactivo(articulos)
 
            case 7: 
                print("Saliendo del programa...")  # Mensaje de salida 
 
            case _: 
                print("Opción inválida, intenta de nuevo.")  # Si el número no está entre 1 y 7 
 
# Muestra el menú de opciones para gestionar usuarios 
def mostrar_menu_usuarios(): 
    menu = [ 
        "Crear usuario", 
        "Listar usuario", 
        "Buscar usuario por id", 
        "Actualizar usuario", 
        "Eliminar usuario", 
        "Alternar activo/inactivo", 
        "Salir" 
    ] 
    for i, opcion in enumerate(menu, 1): 
        print(i, opcion) 
 
# Función principal que gestiona la interacción con el usuario 
def menu_usuarios(): 
    opcion = 0 
    while opcion != 7:  # Repite el menú hasta que se elija la opción de salir 
        mostrar_menu_usuarios() 
        opcion = int(input("Elige una opción (1-7): ")) 
        
        match opcion: 
            case 1: 
                crear_usuario(usuarios) 
 
            case 2: 
                listar_usuario(usuarios)
 
            case 3: 
                buscar_usuario_id(usuarios) 
 
            case 4: 
                actualizar_usuario(usuarios) 
 
            case 5: 
                eliminar_usuario(usuarios) 
 
            case 6: 
                usuario_activo_inactivo(usuarios) 
 
            case 7: 
                # Opción para salir del programa 
                print("Saliendo del programa...") 
 
            case _: 
                # Manejo de opción inválida 
                print("Opción inválida, intenta de nuevo.") 
    
from Proyecto_Mini_Tienda_Online_modulos import (seleccionar_usuario_activo, añadir_articulo_carrito, quitar_articulo_carrito, ver_carrito, confirmar_compra, historial_ventas_usuario, vaciar_carrito)
 
def menu_ventas(): 
    global usuario_activo  # Se usa para cambiar el usuario que está comprando 
    opcion = 0 
    while opcion != 8: 
        # Menú principal de opciones 
        print("\nVENTAS / CARRITO") 
        print("1. Seleccionar usuario activo") 
        print("2. Añadir artículo al carrito") 
        print("3. Quitar artículo del carrito") 
        print("4. Ver carrito (detalle y total)") 
        print("5. Confirmar compra") 
        print("6. Historial de ventas por usuario") 
        print("7. Vaciar carrito") 
        print("8. Volver") 
        opcion = int(input("Elige una opción (1-8): ")) 
        match opcion: 
            case 1: 
                seleccionar_usuario_activo(ventas) 
 
            case 2: 
                # Añade un artículo al carrito si hay usuario activo 
                if usuario_activo is None: 
                    print("Primero selecciona un usuario activo.") 
                    return 
                id_articulo = int(input("ID del artículo: "))
                articulo = buscar_articulo_por_id(articulos, id_articulo)
                if not articulo or not articulo["activo"]: 
                    print("Artículo no válido o inactivo.") 
                    return 
                cantidad = int(input("Cantidad: ")) 
                if cantidad < 1 or cantidad > articulo["stock"]: 
                    print("Cantidad inválida o excede el stock.") 
                    return 
                # Si ya está en el carrito, suma la cantidad 
                for i, (aid, cant) in enumerate(carrito_actual): 
                    if aid == id_articulo: 
                        carrito_actual[i] = (aid, cant + cantidad) 
                        print("Cantidad actualizada en el carrito.") 
                        return 
                # Si no está, lo añade como nuevo 
                carrito_actual.append((id_articulo, cantidad)) 
                print("Artículo añadido al carrito.") 
 
            case 3: 
                # Elimina un artículo del carrito por su ID 
                id_articulo = int(input("ID del artículo a quitar: ")) 
                for i, (aid, _) in enumerate(carrito_actual): 
                    if aid == id_articulo: 
                        del carrito_actual[i] 
                        print("Artículo eliminado del carrito.") 
                        return 
                print("Ese artículo no está en el carrito.") 
 
            case 4: 
                # Muestra el contenido del carrito y el total 
                total = 0 
                for aid, cantidad in carrito_actual: 
                    articulo = buscar_articulo_por_id(articulos, aid) 
                    if articulo: 
                        subtotal = articulo["precio"] * cantidad 
                        print(f"{articulo['nombre']} x{cantidad} = {subtotal:.2f}") 
                        total += subtotal 
                print(f"Total del carrito: {total:.2f}") 
 
            case 5: 
                # Registra la compra si hay usuario y carrito 
                if usuario_activo is None: 
                    print("No hay usuario activo.") 
                    return 
                if not carrito_actual: 
                    print("El carrito está vacío.") 
                    return 
                items = [] 
                for aid, cantidad in carrito_actual: 
                    articulo = buscar_articulo_por_id(articulos, aid) 
                    if not articulo or not articulo["activo"] or cantidad > articulo["stock"]: 
                        print(f"Error con el artículo {aid}. Verifica stock y estado.") 
                        return 
                    articulo["stock"] -= cantidad  # Resta stock 
                    items.append((aid, cantidad, articulo["precio"]))  # Guarda snapshot 
                total = sum(cant * precio for _, cant, precio in items) 
                venta = { 
                    "id_venta": len(ventas) + 1, 
                    "usuario_id": usuario_activo, 
                    "items": items, 
                    "total": round(total, 2) 
                } 
                ventas.append(venta)  # Registra la venta 
                carrito_actual.clear()  # Limpia el carrito 
                print("Compra confirmada. Venta registrada.") 
 
            case 6: 
                # Muestra las ventas del usuario activo 
                if usuario_activo is None: 
                    print("No hay usuario activo.") 
                    return 
                print(f"Historial de ventas del usuario {usuario_activo}:") 
                for venta in ventas: 
                    if venta["usuario_id"] == usuario_activo: 
                        print(f"Venta #{venta['id_venta']} - Total: {venta['total']:.2f}") 
                        for aid, cant, precio in venta["items"]: 
                            print(f"  Artículo {aid} x{cant} @ {precio:.2f}") 
 
            case 7: 
                # Limpia el carrito actual 
                carrito_actual.clear() 
                print("Carrito vaciado.") 
 
            case 8: 
                # Vuelve al menú principal 
                print("Volviendo al menú principal...") 
 
            case _:  # Opción inválida 
                print("Opción inválida.") 
 
 
 
# Lista con las opciones principales del menú 
opciones_menu = ["Menu articulos", "Menu usuarios", "Menu ventas"] 
 
# Muestra las opciones numeradas en pantalla 
for i, opcion in enumerate(opciones_menu, 1): 
    print(i, opcion) 
 
# Solicita al usuario que elija una opción del menú 
opcion = int(input("Elije a que menu acceder: ")) 
 
# Llama al menú correspondiente según la opción elegida 
if opcion == 1: 
    menu_articulos() 
elif opcion == 2: 
    menu_usuarios() 
elif opcion == 3: 
    menu_ventas() 
else: 
    # Muestra un mensaje si la opción no es válida 
    print("Opcion invalida")