class Paciente:
    def __init__(self, cedula, nombre, edad, tipo_sangre):
        # Almacena los datos personales del paciente
        self.cedula = cedula
        self.nombre = nombre
        self.edad = edad
        self.tipo_sangre = tipo_sangre

        # Lista para guardar las consultas médicas del paciente
        self.consultas = []

    # Método para agregar una nueva consulta al historial del paciente
    def agregar_consulta(self, fecha, diagnostico, tratamiento):
        consulta = [fecha, diagnostico, tratamiento]  # Se guarda como lista
        self.consultas.append(consulta)  # Se añade la consulta a la lista de historial

    # Método para mostrar todas las consultas registradas del paciente
    def mostrar_historial(self):
        print(f"Historial de consultas de {self.nombre}:")
        for consulta in self.consultas:
            print(f"Fecha: {consulta[0]}, Diagnóstico: {consulta[1]}, Tratamiento: {consulta[2]}")
