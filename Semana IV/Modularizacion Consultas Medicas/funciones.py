from paciente import Paciente  # Importa la clase Paciente desde el archivo paciente.py

# Lista global donde se almacenan todos los pacientes registrados
lista_pacientes = []

# Busca un paciente en la lista usando su cédula
def buscar_paciente(cedula):
    for paciente in lista_pacientes:
        if paciente.cedula == cedula:
            return paciente  # Devuelve el paciente si se encuentra
    return None  # Si no se encuentra, devuelve None

# Registra un nuevo paciente si no existe ya
def registrar_paciente():
    print("\n\t\tREGISTRAR NUEVO PACIENTE")
    cedula = input("Ingrese la cédula del paciente: ")
    
    # Validación de cédula: debe tener 10 dígitos numéricos
    while len(cedula) != 10 or not cedula.isdigit():
        print("Cédula inválida. Debe tener 10 dígitos.")
        cedula = input("Ingrese la cédula del paciente: ")

    # Verifica si el paciente ya está registrado
    if buscar_paciente(cedula):
        print("El paciente ya está registrado.")
        return
    
    # Solicita los demás datos del paciente
    nombre = input("Ingrese el nombre del paciente: ")
    
    edad = input("Ingrese la edad del paciente: ")
    while not edad.isdigit() or int(edad) <= 0:
        print("Edad inválida. Debe ser un número positivo.")
        edad = input("Ingrese la edad del paciente: ")

    # Verifica que el tipo de sangre ingresado sea válido
    tipo_sangre = input("Ingrese el tipo de sangre del paciente: ")
    while tipo_sangre not in ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]:
        print("Tipo de sangre inválido. Debe ser uno de los siguientes: A+, A-, B+, B-, AB+, AB-, O+, O-.")
        tipo_sangre = input("Ingrese el tipo de sangre del paciente: ")

    # Crea el objeto Paciente y lo agrega a la lista
    nuevo_paciente = Paciente(cedula, nombre, edad, tipo_sangre)
    lista_pacientes.append(nuevo_paciente)
    print(f"Paciente {nombre} registrado exitosamente.")

# Registra una consulta médica para un paciente existente
def registrar_consulta():
    print("\n\t\tREGISTRAR CONSULTA")
    cedula = input("Ingrese la cédula del paciente: ")
    
    # Validación de cédula
    while len(cedula) != 10 or not cedula.isdigit():
        print("Cédula inválida. Debe tener 10 dígitos.")
        cedula = input("Ingrese la cédula del paciente: ")

    paciente = buscar_paciente(cedula)
    
    if not paciente:
        print("Paciente no encontrado.")
        return

    # Recolección de datos de la consulta
    fecha = input("Ingrese la fecha de la consulta (DD/MM/AAAA): ")
    diagnostico = input("Ingrese el diagnóstico: ")
    tratamiento = input("Ingrese el tratamiento: ")

    # Agrega la consulta al historial del paciente
    paciente.agregar_consulta(fecha, diagnostico, tratamiento)
    print(f"Consulta registrada para {paciente.nombre}.")

# Muestra los datos de un paciente específico y su historial
def mostrar_paciente():
    print("\n\t\tDATOS DEL PACIENTE")
    cedula = input("Ingrese la cédula del paciente: ")
    
    # Validación de cédula
    while len(cedula) != 10 or not cedula.isdigit():
        print("Cédula inválida. Debe tener 10 dígitos.")
        cedula = input("Ingrese la cédula del paciente: ")

    paciente = buscar_paciente(cedula)
    
    if not paciente:
        print("Paciente no encontrado.")
        return

    # Muestra los datos personales y el historial de consultas
    print(f"Nombre: {paciente.nombre}, Edad: {paciente.edad}, Tipo de Sangre: {paciente.tipo_sangre}")
    paciente.mostrar_historial()

# Muestra todos los pacientes registrados y sus historiales
def mostrar_todos():
    print("\n\t\tPACIENTES REGISTRADOS")
    
    if not lista_pacientes:
        print("No hay pacientes registrados.")
        return

    # Recorre la lista y muestra los datos e historial de cada paciente
    for paciente in lista_pacientes:
        print(f"Cédula: {paciente.cedula}, Nombre: {paciente.nombre}, Edad: {paciente.edad}, Tipo de Sangre: {paciente.tipo_sangre}")
        paciente.mostrar_historial()
