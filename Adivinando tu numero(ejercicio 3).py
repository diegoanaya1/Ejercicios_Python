from random import *

print(input("Ingresa tu nombre: "))
print("He pensado un numero entre 1 y 100, a continuacion podras adivinarlo, pero solo tienes 8 intentos")
intentos=0

aleatorio=int(randint(1,101))
#print(aleatorio)
while intentos <8:
    intentos+=1
    numero=int((input("Ingresa el numero que creas que es: ")))
    if numero >100:
        print("Ese numero no es valido")
    elif numero <0:
        print("Ese numero no es valido")

    elif numero < aleatorio:
        print("EL NUMERO ES INCORRECTO Y MENOR AL NUMERO PENSADO")
    elif numero > aleatorio:
        print("EL NUMERO ES INCORRECTO Y MAYOR AL NUMERO PENSADO")
    else:
        print(f"EL NUMERO ES CORRECTO era el {aleatorio}, felicitaciones has adivinado el numero en {intentos} intentos")
        break
        
if numero != aleatorio:
    print(f"El numero que habia pensado era {aleatorio}")





