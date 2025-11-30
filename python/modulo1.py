print ("Hola Mundo")

# Mi primer "Hola Mundo" en Python

nombre_completo = "Douggie Bear Castellanos" 
edad = "25"                                         # Asignación de variables
tonto = True  

a = b = c = d = 10 # Se pueden asignar múltiples variables en una sola línea

# Arimetica básica

a = 10
b = 3


suma = a + b   # 13
resta = a - b    # 7
multiplicacion = a * b    # 30
division = a / b   # 3.333333333
división_entera = a // b   # 3
modulo = a % b   # 1
exponenciacion = a ** b   # 1000

# De comparacion 

a = 10
b = 3


igual = a == b   # False
diferente = a != b   # True
#mayor que = a > b   # True
#menor que = a < b   # False
#mayor o igual = a >= b   # True
#menor o igual = a <= b   # False


#Logicos

a = 10
b = 3


resultado_and = (a > 5) and (b < 5)   # True
resultado_or = (a > 15) or (b < 5)   # True
resultado_not = not (a > 5)   # False#


# Estructuras de control 

# if condicion:     # Bloque de código si la condición es verdadera 



nombre = "Douggie"

if nombre == "Douggie":
    print("Hola Douggie!") # Bloque de código si la condición es verdadera
 
 
 
edad = 20

if edad < 18:
    print ("Sos menor de edad.")
    

elif edad > 18 and edad < 60:
    print ("Sos mayor de edad.")
    

elif edad > 15:
    print("Sos mayor de 15.")
    

elif edad == 60:
    print("Felicidades, cumpliste 60 años.")
    

else: 
    print("Felicidades, sos adulto mayor.")
    
    
# For

frutas = ["manzana, frutilla, mango, naranja"]


for frutas in frutas:
    print(frutas)



# While

contador = 3


while contador != 0:
    contador = contador -1
print ("El contenido del contador es", contador)

# break = La instrucción break se utiliza para salir prematuramente de un bucle, independientemente de la condición.

for numero in range(10):
    if numero == 10:
       break
    continue
print(numero) 



for nombre in ("Javier", "Pablo", "Douglas", "Pepe"):
    if nombre == "Douglas":
        continue
print(nombre)    

intentos = 3    
while intentos > 0:
    if input(">>> Escriba la contraseña") == "ansel":
        print("Contraseña correcta.")
        break
    else:
        print("Contraseña incorrecta.")
    intentos = intentos - 1
    
#Estructura de datos

#append(elemento): agrega un elemento al final de la lista.
#insert(indice, elemento): inserta un elemento en una posición específica de la lista.
#remove(elemento): elimina la primera aparición de un elemento en la lista.
#pop(indice): elimina y devuelve el elemento en una posición específica de la lista.
#sort(): ordena los elementos de la lista en orden ascendente.
#reverse(): invierte el orden de los elementos en la lista.

frutas1 = ["manza, banana, caca"]

frutas1.append("pis")
print(frutas1)

frutas1.insert(1, "uva")
print(frutas1)

frutas1.remove("uva")
print(frutas1)

frutas1.sort
print(frutas1)

frutas1.reverse ()
print(frutas1)


numeros = [1, 2, 3, 4, 5]
cuadrados = [x ** 2 for x in numeros if x % 2 == 0]
print(cuadrados)  # Imprime [4, 16]

#Tuplas

#count(elemento): devuelve el número de veces que aparece un elemento en la tupla. 
#index(elemento): devuelve el índice de la primera aparición de un elemento en la tupla. Opcionalmente, se puede especificar el inicio y fin de la búsqueda. 
#len(tupla): aunque no es un método de tupla propiamente dicho, esta función incorporada devuelve la longitud de la tupla.


mi_tupla = (1, 2, 3, 2, 4, 2)


print (mi_tupla.index(2))   # Salida: 1

print (mi_tupla.index(2, 2))   #Salida: 3

print (mi_tupla.index(2, 2, 4))   #Salida: 3

#Diccionarios

#Los diccionarios en Python tienen varios métodos incorporados para manipular y acceder a los elementos. Algunos métodos comunes son:

#keys(): devuelve una vista de todas las claves del diccionario.
#values(): devuelve una vista de todos los valores del diccionario.
#items(): devuelve una vista de todos los pares clave-valor del diccionario.
#update(otro_diccionario): actualiza el diccionario con los pares clave-valor de otro diccionario.

persona = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}


print(persona.keys())    # Imprime dict_keys(["nombre", "edad", "ciudad"])
print(persona.values())  # Imprime dict_values(["Juan", 25, "Madrid"])
print(persona.items())   # Imprime dict_items([("nombre", "Juan"), ("edad", 25), ("ciudad", "Madrid")])


persona.update({"profesion": "Ingeniero"})
print(persona)  # Imprime {"nombre": "Juan", "edad": 25, "ciudad": "Madrid", "profesion": "Ingeniero"}

#conjuntos

#Para crear un conjunto, utiliza llaves o la función set():

# frutas = {"manzana", "banana", "naranja"}
# numeros = set([1, 2, 3, 4, 5])

frutas2 = {"naranja, pepino, arandano"}
numeros = set([1, 2, 3, 4, 5])
print(frutas2)

#conjunto1 = {1, 2, 3}
#conjunto2 = {3, 4, 5}


#union = conjunto1 | conjunto2
#print(union)  # Imprime {1, 2, 3, 4, 5}


#interseccion = conjunto1 & conjunto2
#print(interseccion)  # Imprime {3}


#diferencia = conjunto1 - conjunto2
#print(diferencia)  # Imprime {1, 2}


#diferencia_simetrica = conjunto1 ^ conjunto2
#print(diferencia_simetrica)  # Imprime {1, 2, 4, 5}




#metodos de conjunto


#Los conjuntos en Python tienen varios métodos incorporados para manipular y acceder a los elementos. Algunos métodos comunes son:

#add(elemento): agrega un elemento al conjunto.
#remove(elemento): elimina un elemento del conjunto. Si el elemento no existe, genera un error.
#discard(elemento): elimina un elemento del conjunto si está presente. Si el elemento no existe, no hace nada.
#clear(): elimina todos los elementos del conjunto.

frutas3 = {"caca", "pedo", "pipi"}

frutas3.add ("socotroco")
print(frutas3)

frutas3.remove("caca")
print(frutas3)

frutas3.discard("pipi")
print("pipi")

frutas3.clear()
print(frutas3)