#Importacion de modulos
from herramientas import registrar_estudiante, asignar_calificacion, mostrar_datos, mostrar_todos

# Funcion MENU
def menu():
    while True:
        print("\n\t\tSISTEMA DE REGISTRO ACADÉMICO\n")
        print("1. Registrar nuevo estudiante")
        print("2. Agregar calificación a estudiante")
        print("3. Mostrar información de estudiantes")
        print("4. Mostrar todos los estudiantes")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        #Validar opcion
        if opcion == "1":
            registrar_estudiante()
        elif opcion == "2":
            asignar_calificacion()
        elif opcion == "3":
            mostrar_datos()
        elif opcion == "4":
            mostrar_todos()
        elif opcion == "5":
            print("Gracias por usar el sistema. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente de nuevo.\n")

# Ejecutar menú
if __name__ == "__main__":
    menu()