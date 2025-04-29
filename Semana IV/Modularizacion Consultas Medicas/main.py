from funciones import *  # Importa todas las funciones definidas en el archivo funciones.py

# Definición de la función principal que muestra el menú y ejecuta acciones según la opción seleccionada
def menu():
    while True:  # Bucle que permite mostrar el menú repetidamente hasta que el usuario decida salir
        print("\n\t\tMENU PRINCIPAL")
        print("1. Registrar nuevo paciente")            # Opción para ingresar los datos de un nuevo paciente
        print("2. Registrar consulta")                  # Opción para añadir una consulta a un paciente existente
        print("3. Mostrar datos del paciente")          # Opción para ver el historial de un paciente específico
        print("4. Mostrar Pacientes Registrados")       # Opción para ver la lista de todos los pacientes registrados
        print("5. Salir")                               # Opción para salir del programa

        opcion = int(input("Seleccione una opción: "))  # Solicita al usuario que seleccione una opción
        
        if opcion == 1:
            registrar_paciente()    # Llama a la función que registra un nuevo paciente
        elif opcion == 2:
            registrar_consulta()    # Llama a la función que registra una nueva consulta
        elif opcion == 3:
            mostrar_paciente()      # Llama a la función que muestra los datos de un paciente específico
        elif opcion == 4:
            mostrar_todos()         # Llama a la función que muestra todos los pacientes registrados
        elif opcion == 5:
            print("Saliendo del programa...")  # Mensaje de salida
            break                    # Sale del bucle y finaliza el programa
        else:
            print("Opción inválida. Intente nuevamente.")  # Mensaje de error para opciones no válidas

# Punto de entrada principal del programa
if __name__ == "__main__":
    menu()  # Llama a la función principal para iniciar el programa
