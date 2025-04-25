class Paciente:
    def __init__(self,cedula, nombre, edad, tipo_sangre):
        #Datos del paciente
        self.cedula=cedula
        self.nombre=nombre
        self.edad=edad
        self.tipo_sangre=tipo_sangre

        #Las consultas son una lista de objetos de la clase Consulta
        self.consultas=[]

    def agregar_consulta(self, fecha, diagnostico, tratamiento):
        consulta=[fecha, diagnostico, tratamiento]
        self.consultas.append(consulta)

    def mostrar_historial(self):
        print(f"Historial de consultas de {self.nombre}:")
        for consulta in self.consultas:
            print(f"Fecha: {consulta[0]}, Diagnóstico: {consulta[1]}, Tratamiento: {consulta[2]}")

