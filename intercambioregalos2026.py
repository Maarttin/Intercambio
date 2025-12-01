import random
import string

# Lista de participantes
participantes = ["EmmaSaHe","Rolaando", "Daaniiel", "Berenice", "Maartiin"]

# Paso 1: Crear una lista mezclada de destinatarios
destinatarios = participantes.copy()
random.shuffle(destinatarios)

# Evitar que alguien se asigne a sí mismo
for i in range(len(participantes)):
    if participantes[i] == destinatarios[i]:
        # Si alguien se toca a sí mismo, intercambiamos con otro
        j = (i + 1) % len(participantes)
        destinatarios[i], destinatarios[j] = destinatarios[j], destinatarios[i]

# Paso 2: Función de cifrado simple (Cifrado César)
def cifrar(texto, desplazamiento=7):
    resultado = ""
    for char in texto.upper():
        if char in string.ascii_uppercase:
            resultado += chr((ord(char) - 65 + desplazamiento) % 26 + 65)
        else:
            resultado += char
    return resultado

def descifrar(texto, desplazamiento=5):
    return cifrar(texto, -desplazamiento)

# Paso 3: Asignar y generar códigos
rifa = {}
for i in range(len(participantes)):
    giver = participantes[i]
    receiver = destinatarios[i]
    codigo = cifrar(receiver, desplazamiento=7)  # cada nombre cifrado
    rifa[giver] = codigo

# Mostrar resultados (solo códigos)
print("Códigos asignados:")
for persona, codigo in rifa.items():
    print(f"{persona} -> {codigo}")
