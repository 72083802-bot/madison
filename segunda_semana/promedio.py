nota1 = float(input("ingrese la nota 1: "))
nota2 = float(input("ingrese la nota 2: "))
nota3 = float(input("ingrese la nota 3: "))

suma_nota = nota1 + nota2 + nota3

promedio = suma_nota / 3

print ("promedio: ", round(promedio,2))

if promedio>=13:
    estado = "aprobado"
elif promedio>=11:
    estado = " desaprobado"
else:
    estado = "reprobado"
print("estado del estudiamte: ", estado)

    