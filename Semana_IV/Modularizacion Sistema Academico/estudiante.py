from calificacion import Calificacion

class Estudiante:
    def __init__(self, nombre, matricula, carrera):
        self.nombre = nombre
        self.matricula = matricula
        self.carrera = carrera
        self.calificaciones=[]

    def agregar_calificaciones(self,materia, nota):
        for c in self.calificaciones:
            if c.materia.lower() == materia.lower():
                c.nota=nota
                print("Nota actualizada con éxito.")
                return
        
        self.calificaciones.append(Calificacion(materia,nota))
        print("Calificación agregada con éxito.")
        
    def mostrar_datos(self):
        print("Nombre: ",self.nombre)
        print("Matricula: ",self.matricula)
        print("Carrera: ",self.carrera)
        print("\n\tCalificaciones ")
        if not self.calificaciones:
            print("No hay calificaciones registradas.")
        
        for c in self.calificaciones:
            print("Materia: ",c.materia)
            print("Nota: ",c.nota)
            print("")


