#Ejercicio 1

#MENÚ
#1. Sumar
#2. Restar
#3. Multiplicar
#4. Dividir

opcion = int(input("Elige una opción (1-4): "))
if opcion >= 1 and opcion <=4:
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    if opcion == 1:
        print("La suma es:", num1+num2)
    elif opcion == 2:
        print("La resta es:", num1-num2)
    elif opcion == 3:
        print("La multiplicación es:", num1*num2)
    else:
        if num2 != 0:
            print("La división es:", num1/num2)
        else:
            print("Error: No se puede dividir entre cero.")
else:
    print("Opción no válida. Por favor, elige una opción entre 1 y 4.")
