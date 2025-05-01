class Huesped:
    def __init__(self, nombre, cedula, correo): #Constructor de la clase Huesped
        self.nombre = nombre
        self.cedula = cedula
        self.correo = correo
        self.reservas = []

    def agregar_reserva(self,reserva): #Método para agregar reservas
        self.reservas.append(reserva)

    def mostrar_datos(self): #Muestra datos del huésped
        print("\n\t\tDATOS DEL HUÉSPED\n")
        print("Nombre:", self.nombre)
        print("Cedula:",self.cedula)
        print("Correo:",self.correo)
        if self.reservas:
            print("\nReservas\n")
            for r in self.reservas:
                print("Fecha de entrada: ", r[0])
                print("Fecha de salida: ", r[1])
                print("Tipo de Habitación: ", r[2])
        else:
            print("No hay reservas registradas.")
        print("\n")