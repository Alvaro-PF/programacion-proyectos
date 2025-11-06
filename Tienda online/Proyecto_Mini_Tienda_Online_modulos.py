def crear_articulo(articulos):                
                id_añadir = input("Introduce id articulo: ") 
                encontrado = False 
                # Se verifica si el ID ya existe 
                for articulo in articulos: 
                    if str(articulo["id"]) == id_añadir: 
                        print("El articulo ya esta") 
                        encontrado = True 
                # Si no existe, se pide la información del nuevo artículo 
                if not encontrado: 
                    nombre = input("Ingresa un nombre: ") 
                    precio = float(input("Ingrese precio: ")) 
                    stock = int(input("Ingresa stock: ")) 
                    activo = input("¿Está activo?(s/n): ").lower() == "s" 
                    nuevo_articulo = { 
                        "id": int(id_añadir), 
                        "nombre": nombre, 
                        "precio": precio, 
                        "stock": stock, 
                        "activo": activo 
                    } 
                    articulos.append(nuevo_articulo) 
                    print("Articulo añadido")

def listar_articulo(articulos):
                for art in articulos: 
                    print(list(art.values()))  # Muestra los valores de cada artículo 
                print("Mostrando el menu de nuevo...")

def buscar_articulo_id(articulos):
                id_elejido = input("Di el id del articulo: ") 
                encontrado = False 
                for articulo in articulos: 
                    if str(articulo["id"]) == id_elejido: 
                        print("Artículo encontrado:", articulo)

def actualizar_articulo(articulos):
                id_actualizar = input("Articulo a actualizar: ") 
                for articulo in articulos: 
                    if str(articulo["id"]) == id_actualizar: 
                        print("Articulo encontrado", articulo) 
 
                        # Se pide nueva información, si se deja vacío se mantiene el valor actual 
                        nuevo_nombre = input(f"Nuevo nombre (actual: {articulo['nombre']}): ") 
                        if nuevo_nombre: 
                            articulo["nombre"] = nuevo_nombre 
 
                        nuevo_precio = input(f"Nuevo precio (actual: {articulo['precio']}): ") 
                        if nuevo_precio: 
                            articulo["precio"] = float(nuevo_precio) 
 
                        nuevo_stock = input(f"Nuevo stock (actual: {articulo['stock']}): ") 
                        if nuevo_stock: 
                            articulo["stock"] = int(nuevo_stock) 
 
                        nuevo_estado = input(f"Nuevo estado (actual: {articulo['activo']}) [True/False]: ") 
                        if nuevo_estado.lower() in ["true", "false"]: 
                            articulo["activo"] = nuevo_estado.lower() == "true"

def eliminar_articulo(articulos):
                id_eliminar = input("Di el id del articulo a eliminar: ") 
                encontrado = False 
                for i, articulo in enumerate(articulos): 
                    if str(articulo["id"]) == id_eliminar: 
                        del articulos[i]  # Elimina el artículo de la lista 
                        print("Eliminando articulo...") 
                        encontrado = True 
                if not encontrado: 
                    print("No esta ese producto")

def articulo_activo_inactivo(articulos):
                id_alternar = input("ID del artículo para alternar estado: ") 
                for articulo in articulos: 
                    if str(articulo["id"]) == id_alternar: 
                        articulo["activo"] = not articulo["activo"]  # Cambia True por False 
                        print(f"Estado cambiado a: {articulo['activo']}")

def crear_usuario(usuarios):
                # Opción para crear un nuevo usuario 
                id_añadir = input("Introduce el id del usuario: ") 
                encontrado = False 
                for usuario in usuarios: 
                    if str(usuario["id"]) == id_añadir: 
                        print("El usuario ya está registrado.") 
                        encontrado = True 
                if not encontrado: 
                    nombre = input("Ingresa un nombre: ") 
                    email = input("Ingresa el email (con @): ") 
                    activo = input("¿Está activo? (s/n): ").lower() == "s" 
                    nuevo_usuario = { 
                        "id": int(id_añadir), 
                        "nombre": nombre, 
                        "email": email, 
                        "activo": activo 
                    } 
                    usuarios.append(nuevo_usuario) 
                    print("Usuario añadido correctamente.")

def listar_usuario(usuarios):
                # Opción para listar todos los usuarios 
                for usu in usuarios: 
                    print(list(usu.values())) 
                print("Volviendo al menú...")

def buscar_usuario_id(usuarios):
                # Opción para buscar un usuario por su ID 
                id_elejido = input("Introduce el ID del usuario: ") 
                encontrado = False 
                for usuario in usuarios: 
                    if str(usuario["id"]) == id_elejido: 
                        print("Usuario encontrado:", usuario) 
                        encontrado = True 
                if not encontrado: 
                    print("No se encontró ningún usuario con ese ID.")

def actualizar_usuario(usuarios):
                # Opción para actualizar los datos de un usuario 
                id_actualizar = input("ID del usuario a actualizar: ") 
                for usuario in usuarios: 
                    if str(usuario["id"]) == id_actualizar: 
                        print("Usuario encontrado:", usuario) 
                        
                        nuevo_nombre = input(f"Nuevo nombre (actual: {usuario['nombre']}): ") 
                        if nuevo_nombre: 
                            usuario["nombre"] = nuevo_nombre 
                        
                        nuevo_email = input(f"Nuevo email (actual: {usuario['email']}): ") 
                        if nuevo_email: 
                            usuario["email"] = nuevo_email 
                        
                        nuevo_estado = input(f"Nuevo estado (actual: {usuario['activo']}) [True/False]: ") 
                        if nuevo_estado.lower() in ["true", "false"]: 
                            usuario["activo"] = nuevo_estado.lower() == "true"

def eliminar_usuario(usuarios):
                # Opción para eliminar un usuario por su ID 
                id_eliminar = input("Introduce el ID del usuario a eliminar: ") 
                encontrado = False 
                for i, usuario in enumerate(usuarios): 
                    if str(usuario["id"]) == id_eliminar: 
                        del usuarios[i] 
                        print("Usuario eliminado correctamente.") 
                        encontrado = True 
                if not encontrado: 
                    print("No se encontró ningún usuario con ese ID.")

def usuario_activo_inactivo(usuarios):
                # Opción para alternar el estado activo/inactivo de un usuario 
                id_alternar = input("ID del usuario para alternar estado: ") 
                for usuario in usuarios: 
                    if str(usuario["id"]) == id_alternar: 
                        usuario["activo"] = not usuario["activo"] 
                        print(f"Estado cambiado a: {usuario['activo']}")

def seleccionar_usuario_activo(usuarios):
                # Activa un usuario para poder comprar 
                id_usuario = int(input("Introduce el ID del usuario: ")) 
                usuario = buscar_usuario_por_id(usuarios, id_usuario) 
                if usuario and usuario["activo"]: 
                    usuario_activo = id_usuario 
                    print(f"Usuario activo: {usuario['nombre']}") 
                else: 
                    print("Usuario no encontrado o inactivo.")

def añadri_articulo_carrito(articulos):
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