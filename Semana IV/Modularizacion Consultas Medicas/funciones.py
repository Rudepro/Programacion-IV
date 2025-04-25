from paciente import Paciente

#Lista para almacenar los pacientes
lista_pacientes = []

def buscar_paciente(cedula):
    for paciente in lista_pacientes:
        if paciente.cedula == cedula:
            return paciente
    return None

def registrar_paciente():
    print("\n\t\tREGISTRAR NUEVO PACIENTE")
    cedula = input("Ingrese la cédula del paciente: ")
    while len(cedula) != 10 or not cedula.isdigit():
        print("Cédula inválida. Debe tener 10 dígitos.")
        cedula = input("Ingrese la cédula del paciente: ")

    if buscar_paciente(cedula):
        print("El paciente ya está registrado.")
        return
    
    nombre = input("Ingrese el nombre del paciente: ")
    edad = input("Ingrese la edad del paciente: ")
    while not edad.isdigit() or int(edad)<=0:
        print("Edad inválida. Debe ser un número positivo.")
        edad = input("Ingrese la edad del paciente: ")

    tipo_sangre = input("Ingrese el tipo de sangre del paciente: ")
    while tipo_sangre not in ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]:
        print("Tipo de sangre inválido. Debe ser uno de los siguientes: A+, A-, B+, B-, AB+, AB-, O+, O-.")
        tipo_sangre = input("Ingrese el tipo de sangre del paciente: ")

    nuevo_paciente = Paciente(cedula, nombre, edad, tipo_sangre)
    lista_pacientes.append(nuevo_paciente)
    print(f"Paciente {nombre} registrado exitosamente.")

def registrar_consulta():
    print("\n\t\tREGISTRAR CONSULTA")
    cedula = input("Ingrese la cédula del paciente: ")
    while len(cedula) != 10 or not cedula.isdigit():
        print("Cédula inválida. Debe tener 10 dígitos.")
        cedula = input("Ingrese la cédula del paciente: ")
    paciente = buscar_paciente(cedula)
    
    if not paciente:
        print("Paciente no encontrado.")
        return
    
    fecha = input("Ingrese la fecha de la consulta (DD/MM/AAAA): ")
    diagnostico = input("Ingrese el diagnóstico: ")
    tratamiento = input("Ingrese el tratamiento: ")

    paciente.agregar_consulta(fecha, diagnostico, tratamiento)
    print(f"Consulta registrada para {paciente.nombre}.")

def mostrar_paciente():
    print("\n\t\tDATOS DEL PACIENTE")
    cedula = input("Ingrese la cédula del paciente: ")
    while len(cedula) != 10 or not cedula.isdigit():
        print("Cédula inválida. Debe tener 10 dígitos.")
        cedula = input("Ingrese la cédula del paciente: ")
    paciente = buscar_paciente(cedula)
    
    if not paciente:
        print("Paciente no encontrado.")
        return
    
    print(f"Nombre: {paciente.nombre}, Edad: {paciente.edad}, Tipo de Sangre: {paciente.tipo_sangre}")
    paciente.mostrar_historial()

def mostrar_todos():
    print("\n\t\tPACIENTES REGISTRADOS")
    if not lista_pacientes:
        print("No hay pacientes registrados.")
        return
    
    for paciente in lista_pacientes:
        print(f"Cédula: {paciente.cedula}, Nombre: {paciente.nombre}, Edad: {paciente.edad}, Tipo de Sangre: {paciente.tipo_sangre}")
        paciente.mostrar_historial()