#Definimos una clase base llamada Persona
class Persona:
    # Constructor de la clase Persona
    # El constructor inicializa los atributos nombre y edad
    def __init__(self, nombre, edad):
        self.nombre = nombre #nombre de la persona
        self.edad = edad #edad de la persona
    # Método para mostrar un saludo 
    # Se usa self para referirse a la instancia actual de la clase
    def saludar(self):
        # Imprime un saludo con el nombre y la edad de la persona
        return f"Hola, soy {self.nombre} y tengo {self.edad} años."

# Creamos un Objeto (una instancia) de la clase Persona
persona1 = Persona("Juan", 30) # Creamos un objeto de la clase Persona
persona2 = Persona("Ana", 25) # Creamos otro objeto de la clase Persona
# Llamamos al método saludar de cada objeto
# Este método tiene acceso a los atributos de la instancia
print(persona1.saludar()) # Llama al método saludar del objeto persona1
print(persona2.saludar()) # Llama al método saludar del objeto persona2


# Definimos una clase hija llamada Estudiante que hereda de Persona
class Estudiante(Persona):
    # Constructor de la clase Estudiante
    def __init__(self, nombre, edad, carrera):
        # Llama al constructor de la clase base (Persona) para inicializar nombre y edad
        super().__init__(nombre, edad)
        self.carrera = carrera

    # Método para mostrar un saludo específico para estudiantes
    def datos_completos(self):
        # Llama al método saludar de la clase base (Persona) y añade la carrera
        return f"{self.saludar()} Estoy estudiando {self.carrera}."
    
# Creamos un Objeto (una instancia) de la clase Estudiante
estudiante1 = Estudiante("Pedro", 20, "Ingeniería") # Creamos un objeto de la clase Estudiante

# Llamamos al método datos_completos del objeto estudiante1
print(estudiante1.datos_completos()) # Llama al método datos_completos del objeto estudiante1