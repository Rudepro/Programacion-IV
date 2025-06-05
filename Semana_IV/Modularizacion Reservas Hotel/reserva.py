from huesped import Huesped

class Reserva:
    def __init__(self,entrada,salida,tipo_habitacion):
        self.entrada=entrada
        self.salida=salida
        self.tipo_habitacion=tipo_habitacion
        self.reservas=[]

    def mostrar_reservas(self):
        print