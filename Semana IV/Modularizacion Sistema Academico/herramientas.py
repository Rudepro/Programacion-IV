#Importar funciones de otros módulos
from estudiante import Estudiante

estudiantes=[] #Lista para guardar estudiantes

def registrar_estudiante(): #Funcion para agregar estudiante
    print("\n\t\tREGISTRO DE ESTUDIANTES\n")
    nombre=input("Ingrese el nombre del estudiante:")
    while True:
        matricula=input("Ingrese la matricula del estudiante:")
        if len(matricula)==10 and matricula.isdigit():
            break
        else:
            print("Matricula inválida. Debe tener 10 dígitos.\n")
    carrera=input("Ingrese la carrera del estudiante:")
    estudiante=Estudiante(nombre, matricula, carrera)
    estudiantes.append(estudiante)
    print("Estudiante registrado con éxito.\n")

def buscar_estudiante(estudiantes, matricula): #Funcion para buscar estudiante
    for e in estudiantes:
        if e.matricula == matricula:
            return e
    return None

def asignar_calificacion(): #Funcion para asignar calificacion
    print("\n\t\tASIGNAR CALIFICACION\n")
    matricula=input("Ingrese la matricula del estudiante:")
    estudiante=buscar_estudiante(estudiantes,matricula)
    if estudiante:
        materia=input("Ingrese la materia: ")
        while True:
            nota=float(input("Ingrese la nota:"))
            if 0<=nota<=10:
                break
            else:
                print("Nota inválida. Debe estar entre 0 y 10.\n")
        estudiante.agregar_calificaciones(materia,nota)

    else:
        print("Estudiante no encontrado.\n")

def mostrar_datos(): #Funcion para mostrar los datos de un estudiante
    print("\n\t\tINFORMACIÓN DEL ESTUDIANTE\n")
    matricula=input("Ingrese la matricula del estudiante:")
    estudiante=buscar_estudiante(estudiantes,matricula)
    if estudiante:
        estudiante.mostrar_datos()
    else:
        print("Estudiante no encontrado.\n")

def mostrar_todos(): #Funcion para mostrar los estudiantes
    print("\n\t\tLISTA DE ESTUDIANTES\n")
    if not estudiantes:
        print("No hay estudiantes registrados.\n")
    for e in estudiantes:
        e.mostrar_datos()
