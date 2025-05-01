from huesped import Huesped # Importamos la clase Huesped

huespedes=[] # Lista para almacenar los huéspedes registrados

def registrar_huesped(): # Función para registrar un nuevo huésped
    print("\n\t\tREGISTRO DE HUÉSPEDES\n")
    nombre = input("Nombre del Huésped: ")
    while True:
        cedula=input("Cedula: ")
        if cedula.isdigit() and len(cedula)==10:
            break
        else: 
            print("Cédula Inválida. Debe tener 10 dígitos.\n")
    while True:
        correo=input("Correo Electrónico: ")
        if "@" in correo and "." in correo:
            break
        else: 
            print("Correo Inválido. Debe tener '@' y '.'\n")

    huesped=Huesped(nombre,cedula,correo)
    if buscar_huesped(cedula):
        print("Huésped ya registrado.\n")
        return
        
    huespedes.append(huesped)
    print("Huésped registrado con éxito.\n")


def buscar_huesped(cedula): # Función para buscar un huésped por su cédula
    for h in huespedes:
        if h.cedula == cedula:
            return h
    return None

def agregar_reserva_huesped(): # Función para agregar una reserva a un huésped
    tipos_habitacion=["Individual","Doble","Familiar","Suite"]
    cedula = input("Ingrese la cedula: ")
    huesped = buscar_huesped(cedula)
    if huesped:
        if huesped.reservas:
            print("Huésped ya tiene reserva registrada.\n")
            return
        
        print("\n\t\tRESERVA DE HABITACION\n")
        entrada=input("Ingrese la fecha de entrada: ")
        salida=input("Ingrese la fecha de salida: ")
        while True:
            habitacion=input("Ingrese el tipo de habitacion (Individual, Doble, Familiar, Suite): ")
            if habitacion in tipos_habitacion:
                break
            else:
                print("Tipo de habitacion inválido. Debe ser Individual, Doble, Familiar o Suite.\n")
        reserva=(entrada,salida,tipos_habitacion)
        huesped.agregar_reserva(reserva)
        print("Reserva registrada con éxito.\n")
    else:
        print("Huésped no encontrado.\n")

def mostrar_huespedes():   # Función para mostrar los huéspedes registrados
    print("\n\t\tHUÉSPEDES REGISTRADOS\n")
    if not huespedes:
        print("No hay huéspedes registrados.\n")
    for h in huespedes:
        h.mostrar_datos()

def mostrar_reservas(): # Función para mostrar las reservas registradas
    print("\n\t\tRESERVAS REGISTRADAS\n")
    if not huespedes:
        print("No hay reservas registradas.\n")
    for h in huespedes:
        if h.reservas:
            h.mostrar_datos()
        else:
            print("No hay reservas registradas.\n")
