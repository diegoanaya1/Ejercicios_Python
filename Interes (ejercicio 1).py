nombre= input("Escribe tu nombre: ")
ventas= int(input("Cuantas fueron tus ventas: "))


comision= round(ventas * 0.13,2)

print(f"Hola {nombre}, tus comisiones son de ${comision}")