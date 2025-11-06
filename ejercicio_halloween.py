#Importa la libreria random
import random

#Variables
intentos = 3
capturado = False

# Lista de monstruos y sus niveles de dificultad 
monstruos = { 'vampiro': 3, 'momia': 2, 'bruja': 4, 'esqueleto': 1, 'fantasma': 5 } 

# Lista de objetos para capturar 
objetos = ['estaca', 'poción mágica', 'hechizo']

#Efectividad de los objetos
efectividad = {'estaca': 0.4, 'poción mágica': 0.6, 'hechizo': 0.8}

#Inicio del juego
print("¡Bienvenido al juego de cazar monstruos para halloween!")
monstruo_elegido = random.choice(list(monstruos.keys()))
dificultad = monstruos[monstruo_elegido]
print("Ha aparecido un:", monstruo_elegido, "con nivel de dificultad:", dificultad)
print("=" * 50)

#Numero de intentos restantes
print("Tienes", intentos, "oportunidades restantes")
print("Elije un objeto para intentar capturar al", monstruo_elegido ,":", objetos)
print("=" * 50)

#Intento de caza
while intentos > 0 and not capturado:
    intento = input("Elije el objeto a utilizar: ").lower()
    if intento in objetos:
        probabilidad_exito = efectividad[intento] / dificultad
        azar = random.random()
        if azar <= probabilidad_exito:
            print(f"Has capturado el/la {monstruo_elegido} con un/a {intento}")
            capturado = True
        else:
            print(f"Fallaste al intentar capturar a el/la {monstruo_elegido} con un/a {intento}")
            intentos -=1
    else:
        print("El objeto no esta")
    print("=" * 50)
