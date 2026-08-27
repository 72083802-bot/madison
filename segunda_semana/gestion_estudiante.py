print("=== REGISTRO DE ESTUDIANTE ===")

# Solicitar datos
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
carrera = input("Ingrese su carrera: ")
semestre = int(input("Ingrese su semestre: "))

# Estado de matrícula
matriculado = True

#solicitar la primera nota 
nota1 = float(input("ingrese la nota 1: "))
while nota1 < 0 or nota1 > 20:
    print(" la nota debe estar entre 0 y 20.")
    nota1 = float(input("ingrese la nota 1: "))
    
nota2 = float(input("ingrese la nota 2: "))
while nota2 < 0 or nota1 > 20:
    print(" la nota debe estar entre 0 y 20.")
    nota2 = float(input("ingrese la nota 2: "))
    

nota3 = float(input("ingrese la nota 3: "))
while nota3 < 0 or nota1 > 20:
    print(" la nota debe estar entre 0 y 20.")
    nota3 = float(input("ingrese la nota 3: "))
    
    # creemos una lista de notas 
notas = [nota1, nota2, nota3]
    
#acumuladores y contadores 
suma = 0
aprobadas = 0
desaprobadas = 0

#procesos de notas 
for nota in notas:
    #sumando nota 1 + nota 2 + nota 3 
    suma = suma + nota
    if nota >=13:
        aprobadas = aprobadas + 1
    else:
        desaprobadas =  desaprobadas + 1
        
#calcular promedio
promedio = suma / len(notas)

#calificar al estudiante 
if promedio >= 17:
    estado = "puede acceder a la veca en URUSAYHUA"
else:
    estado = "tiene que pagar su matricula completa"
# Cursos
cursos = [
    "Herramientas de Desarrollo de Software",
    "Base de Datos",
    "Redes"
    "tutoria"
]

# Mostrar datos
print("\n=== RESULTADO CADEMICO ===")
print("Nombre:", nombre)
print("Carrera:", carrera)
print("Semestre:", semestre)

print("\nNotas:")

for i in  range(len(notas)):
    print("nota", i+1, ":", notas[i])
    
print("\npromedio:", round(promedio,2))
print("notas aprobadas:", aprobadas)
print("notas desaprovadas:", desaprobadas)
print("estado: ", estado) 
print("\n=== CURSOS ===")

for curso in cursos:
    print("-", curso)