#Ctrl+K+C para comentar una línea de código
# Ctrl+K+U para descomentar una línea de código
# Funciones en Python


# def verificar_par(numero):
#     """
#     Verifica si un número es par o impar.
    
#     :param numero: Número a verificar.
#     :return: True si es par, False si es impar.
#     """
#     if numero % 2 == 0:
#         return "Par"
#     else:
#         return "Impar"
    
# print(verificar_par(10))  # Salida: Par

# def nombre():
#     nombre=input("¿Cuál es tu nombre? ")
#     return nombre
# print(nombre())  # Salida: Nombre ingresado por el usuario

# Argumentos Posicionales: En el mismo orden que aparecen en la definición de la función.
# Argumentos Nominales: Se pasan como pares clave-valor, independientemente del orden.
# Argumentos por defecto: Se asigna un valor por defecto a un parámetro en la definición de la función.

# def datos(nombre, apellidos):
#     print("Estamos estudiando Python",nombre, apellidos)
# datos("Juan", "Pérez")  # Argumentos posicionales
# datos(apellidos="Pérez", nombre="Juan")  # Argumentos nominales

# def welcome(nombre, apellidos="Pérez"): #Argumento por defecto
#     print("Bienvenido", nombre, apellidos)
# welcome("Juan")  # Salida: Bienvenido Juan Pérez

# print("Pasar un número indetermiado de argumentos a una función")
# def menu(*platos): # El asterisco (*) permite pasar un número indeterminado de argumentos
#     print("Los platos del día son:")
#     for plato in platos:
#         print(plato, end=", ")
# menu("Pizza", "Pasta", "Ensalada", "Sopa")  # Salida: Pizza, Pasta, Ensalada, Sopa,
# print("\n")

# #**parametros: Se utiliza para pasar un número indeterminado de argumentos como pares clave-valor.
# def contacto(**datos):
#     print("Los datos de contacto son:")
#     for clave, valor in datos.items():
#         print(clave, ":", valor)	
# contacto(nombre="Juan", apellidos="Pérez", telefono="123456789")  # Salida: nombre : Juan, apellidos : Pérez, telefono : 123456789
# print("\n")

print("***Funciones Recursivas***")
def cuenta_regresiva(numero):
    """
    Realiza una cuenta regresiva desde un número dado hasta 0.
    
    :param numero: Número desde el cual iniciar la cuenta regresiva.
    """
    numero-=1
    if numero>0:
        print(numero)
        cuenta_regresiva(numero)
    else:
        print("BOOOOOM!")
cuenta_regresiva(5)  # Salida: 4, 3, 2, 1, BOOOOOM!

#Dependiendo de la cantidad de datos dependerá el uso del IF(O(1)), FOR-WHILE (O(n)), FOR ANIDADO (O(n^2))

# # #BIG-O Complejidades Computacionales# # #
#O(1) Complejidad Constante - Funcion Par-Impar
#O(n) Complejidad Lineal - Funcion For While Recursiva
#O(n^2) Complejidad Cuadratica - Funcion For Anidado
#O(log n) Complejidad Logaritmica - Funcion Binaria
#O(n!) Complejidad Factorial - Funcion Recursiva
#O(2^n) Complejidad Exponencial - Funcion Fibonacci
#O(n^k) Complejidad Polinomial - Funcion Recursiva
#O(n^3) Complejidad Cubica - Funcion Recursiva