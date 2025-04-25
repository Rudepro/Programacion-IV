from funciones import *

# Definición de la función principal
def menu():
    while True:
        print("\n\t\tMENU PRINCIPAL")
        print("1. Registrar nuevo paciente")
        print("2. Registrar consulta")
        print("3. Mostrar datos del paciente")
        print("4. Mostrar Pacientes Registrados")
        print("5. Salir")

        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            registrar_paciente()
        elif opcion == 2:
            registrar_consulta()
        elif opcion == 3:
            mostrar_paciente()
        elif opcion == 4:
            mostrar_todos()
        elif opcion == 5:
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    menu()