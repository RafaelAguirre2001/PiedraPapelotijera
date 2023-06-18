import random

def obtener_opcion_usuario():
    opcion_valida = False
    while not opcion_valida:
        opcion = input("Elige una opción (piedra, papel, tijera): ").lower()
        if opcion in ["piedra", "papel", "tijera"]:
            opcion_valida = True
        else:
            print("Opción inválida. Por favor, intenta nuevamente.")
    return opcion

def obtener_opcion_computadora():
    opciones = ["piedra", "papel", "tijera"]
    return random.choice(opciones)

def determinar_ganador(usuario, computadora):
    if usuario == computadora:
        return "Empate"
    elif (usuario == "piedra" and computadora == "tijera") or (usuario == "papel" and computadora == "piedra") or (usuario == "tijera" and computadora == "papel"):
        return "¡Ganaste!"
    else:
        return "¡Perdiste!"

def jugar_piedra_papel_tijera():
    print("Bienvenido a Piedra, Papel o Tijera.")
    usuario = obtener_opcion_usuario()
    computadora = obtener_opcion_computadora()
    print("Tu elección:", usuario)
    print("Elección de la computadora:", computadora)
    resultado = determinar_ganador(usuario, computadora)
    print(resultado)
jugar_piedra_papel_tijera()
