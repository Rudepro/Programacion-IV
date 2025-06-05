#Importar funciones de otros módulos
from utilidades import registrar_huesped, buscar_huesped, agregar_reserva_huesped, mostrar_huespedes, mostrar_reservas

# Funcion MENU
def menu():
    while True:
        print("\n\t\tSISTEMA DE GESTIÓN DE RESERVAS DE HOTEL\n")
        print("1. Registrar nuevo huésped")
        print("2. Agregar reserva a huésped")
        print("3. Mostrar huéspedes registrados")
        print("4. Mostrar reservas registradas")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        #Validar opcion
        if opcion == "1":
            registrar_huesped()
        elif opcion == "2":
            agregar_reserva_huesped()
        elif opcion == "3":
            mostrar_huespedes()
        elif opcion == "4":
            mostrar_reservas()
        elif opcion == "5":
            print("Gracias por usar el sistema. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intente de nuevo.\n")

# Ejecutar menú
if __name__ == "__main__":
    menu()