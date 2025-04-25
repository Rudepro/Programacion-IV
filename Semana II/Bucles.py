"""
numero=int(input("Ingrese un valor entero: "))
for i in range(numero+1):
    print(i)
print("Fin del programa")
# El programa solicita un número entero al usuario y luego imprime todos los números desde 0 hasta el número ingresado, inclusive.

for i in range(5,10,2):
    print(i)
# El programa imprime los números del 5 al 9, incrementando de 2 en 2.
# El resultado es 5, 7 y 9.


for i in [1,2,3,4,5]:
    print(i)
# El programa imprime los números de la lista [1, 2, 3, 4, 5].
# El resultado es 1, 2, 3, 4 y 5.

for i in range(0,6):
    print("tabla del ",i)
    for j in range(0,6):
        print(i,"*",j,"=",i*j)
# El programa imprime la tabla de multiplicar del 0 al 5.

for i in range(0,2):
    print("Ciclo de i ",i)
    for j in range(0,2):
        print("Ciclo de j ",j)
        for k in range(0,2):
            print("Ciclo de k ",k)
# El programa imprime los ciclos anidados de i, j y k, cada uno variando de 0 a 1.  
"""
"""
a=5
while a>0:
    print(a)
    a-=1
# El programa imprime los números del 5 al 1, decrementando de 1 en 1.

a=-10
while a<=10:
    if a%2==0:
        print("El número ", a, " es par")
    else:
        print("El número ", a, " es impar")

    a+=1
"""
