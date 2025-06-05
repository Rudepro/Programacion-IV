# Definimos la clase base "Animal"
class Animal:
    #Método que puede ser sobreescrito por las clases hijas
    def hablar(self):
        return "Hace un sonido." #Comportamiento por defecto

# Definimos la clase "Perro", que hereda de "Animal"
class Perro(Animal):
    #Sobreescribimos el método "hablar" para que sea específico de los perros
    def hablar(self):
        return "Ladra"
    
# Definimos la clase "Gato", que hereda de "Animal"
class Gato(Animal):
    #Sobreescribimos el método "hablar" para que sea específico de los gatos
    def hablar(self):
        return "Maulla"
    
#Creamos una lista que contiene un objeto de cada clase
animales =[Perro(), Gato(), Animal()]

#Recorremos la lista y llamamos al método "hablar" de cada objeto
for animal in animales:
    print(animal.hablar()) #Se ejecuta el método correspondiente a cada objeto