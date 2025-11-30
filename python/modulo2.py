# FUNCIONES

# Definición y llamada de funciones
def saludo():
    print ("Hola Mundo")
    
    
# Parámetros y argumentos

#Las funciones pueden aceptar parámetros, que son valores que se pasan a la función cuando se la llama. Los parámetros se especifican dentro de los paréntesis en la definición de la función.

def saludo(nombre):
    print(f"Hola, {nombre}")
saludo ("Mariano")
saludo ("jorge")




# Valores de retorno

#Las funciones pueden devolver valores utilizando la palabra clave return. El valor de retorno puede ser utilizado por el código que llama a la función. 
 
def suma(a, b):
    return a + b

resultado = suma(3, 4)
print(resultado)




# Funciones anónimas (lambda)

# Python permite crear funciones anónimas o funciones lambda, que son funciones sin nombre definidas en una sola línea. Se utilizan comúnmente para funciones pequeñas y concisas.

cuadrado = lambda x: x ** 2
print(cuadrado(5))  # Imprime 25




# Alcance de las variables (local vs. global)

#Las variables definidas dentro de una función tienen un alcance local, lo que significa que solo son accesibles dentro de la función. Por otro lado, las variables definidas fuera de cualquier función tienen un alcance global y pueden ser accedidas desde cualquier parte del programa.

def funcion():
    variable_local = 10
    print(variable_local)  # Accesible dentro de la función
    
    
    
variable_global = 20

def funcion2():
    print(variable_global)  # Accesible desde cualquier lugar
    
    
funcion()  # Imprime 10
funcion2()  # Imprime 20
print(variable_global)  # Imprime 20
# print(variable_local)  # Genera un error, la variable no está definida en este alcance.   




# Funciones definidas por el usuario 


def calcular_media(*numeros):
    suma = sum(numeros)
    cantidad = len(numeros)
    media = suma / cantidad
    return media

print("Media:", calcular_media(10, 20, 30, 40))


def sumar_3(x):
    return x + 3

sumar = lambda x: x + 3

print("Sumarle 3 a un numero", sumar (5))


#Documentación de funciones (docstrings)

#Es una buena práctica documentar nuestras funciones utilizando docstrings. Los docstrings son cadenas de texto que describen el propósito, los parámetros y el valor de retorno de una función. Se colocan inmediatamente después de la definición de la función y se encierran entre triples comillas dobles.

def area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.


    Args:
        base (float): La base del rectángulo.
        altura (float): La altura del rectángulo.


    Returns:
        float: El área del rectángulo.
    """
    return base * altura


# Funciones con número variable de argumentos
#Python permite definir funciones que acepten un número variable de argumentos. Esto se logra utilizando el operador * antes del nombre del parámetro.

def suma_variable(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total


print(suma_variable(1, 2, 3))  # Imprime 6
print(suma_variable(4, 5, 6, 7))  # Imprime 22


# Manejo excepciones

#Try
#El bloque try contiene el código que puede generar una excepción. Si ocurre una excepción dentro del bloque try, el flujo de ejecución se transfiere al bloque except correspondiente.

try:
    # Código que puede generar una excepción
    resultado = 10 / 0  # División por cero
    print(resultado)
except ZeroDivisionError:
    print("Error: División por cero")
    
    
#Except
#El bloque except especifica el tipo de excepción que se desea capturar y manejar. Puedes tener múltiples bloques except para manejar diferentes tipos de excepciones.

try:
    # Código que puede generar una excepción
    resultado = 10 / 0  # División por cero
    print(resultado)
except ZeroDivisionError:
    print("Error: División por cero")
except ValueError:
    print("Error: Valor inválido")
    
    
#Finally
# El bloque finally es opcional y se ejecuta siempre, independientemente de si ocurrió una excepción o no. Se utiliza comúnmente para realizar tareas de limpieza o liberación de recursos.}

try:
    # Código que puede generar una excepción
    archivo = open("archivo.txt", "r")
    # Realizar operaciones con el archivo
except FileNotFoundError:
    print("Error: Archivo no encontrado")
finally:
    archivo.close()  # Cerrar el archivo siempre, incluso si ocurre una excepción
 
 

# Entradas / Salidas 

# Entrada de datos del usuario


nombre = input ("Ingresa tu nombre")
edad = input ("Ingresa tu edad")

print("Hola," + nombre + edad)

print("Tenes" + edad + "Años.")


edad = int(input("Ingresa tu edad: "))


if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
    
    
# Salida de datos

# Para mostrar información en la pantalla, utilizamos la función print(). Esta función toma uno o más argumentos y los muestra en la consola.
#Podemos utilizar la f-string (formateo de cadenas) para incrustar variables directamente dentro de una cadena de texto.

nombre = "Juan"
edad = 25


print(f"Hola, mi nombre es {nombre} y tengo {edad} años.")


# Lectura de archivos

# Para leer el contenido de un archivo, primero debemos abrirlo utilizando la función open() en modo de lectura ("r"). Luego, podemos leer el contenido del archivo utilizando métodos como read() o readlines().

archivo = open("datos.txt", "r")
contenido = archivo.read()
print(contenido)
archivo.close()

# En este ejemplo, se abre el archivo "datos.txt" en modo de lectura utilizando open(). Luego, se lee todo el contenido del archivo utilizando el método read() y se almacena en la variable contenido. Finalmente, se muestra el contenido en la pantalla y se cierra el archivo utilizando el método close().



# Escritura de archivos

# Para escribir datos en un archivo, lo abrimos en modo de escritura ("w") utilizando la función open(). Si el archivo no existe, se creará automáticamente. Si el archivo ya existe, su contenido se sobrescribirá.


archivo = open("datos.txt", "w")
archivo.write("Hola, mundo!")
archivo.close()


# En este ejemplo, se abre el archivo "datos.txt" en modo de escritura utilizando open(). Luego, se escribe la cadena "¡Hola, mundo!" en el archivo utilizando el método write(). Finalmente, se cierra el archivo utilizando el método close().




#  Importación y creación de módulos

# En Python, un módulo es un archivo que contiene definiciones de funciones, clases y variables que se pueden utilizar en otros programas. La importación de módulos nos permite acceder a la funcionalidad definida en otros archivos y reutilizar código de manera eficiente. Además, podemos crear nuestros propios módulos para organizar y modularizar nuestro código.

# Importar módulos

# import math

 # Para utilizar un módulo en nuestro programa, debemos importarlo utilizando la declaración import. Podemos importar un módulo completo o funciones específicas de un módulo.
resultado = math.sqrt(25)
print(resultado)  # Imprime 5.0

import math


resultado = math.sqrt(25)
print(resultado)  # Imprime 5.0


from math import sqrt


resultado = sqrt(25)
print(resultado)  # Imprime 5.0



# Funciones yu clases de modulos estandar

import random
import datetime


numero_aleatorio = random.randint(1, 10)
print(numero_aleatorio)  # Imprime un número entero aleatorio entre 1 y 10


fecha_actual = datetime.datetime.now()
print(fecha_actual)  # Imprime la fecha y hora actual


# Creacion de moedulos propios

# Además de utilizar los módulos estándar de Python, también podemos crear nuestros propios módulos para organizar y reutilizar nuestro código.

#Crear y utilizar módulos personalizados
#Para crear un módulo personalizado, simplemente creamos un nuevo archivo Python con el nombre deseado y definimos las funciones, clases y variables que queremos incluir en el módulo. Por ejemplo, creamos un archivo (en el mismo directorio donde estamos ejecutando Python) llamado mi_modulo.py con el siguiente contenido:


#mi_modulo.py
def saludar(nombre):
    print(f"Hola, {nombre}!")


def calcular_suma(a, b):
    return a + b


# Luego, podemos importar y utilizar las funciones definidas en mi_modulo.py en otro archivo Python.
 
import mi_modulo


mi_modulo.saludar("Juan")  # Imprime "Hola, Juan!"
resultado = mi_modulo.calcular_suma(5, 3)
print(resultado)  # Imprime 8


# Organización del código en módulos


# operaciones.py
def sumar(a, b):
    return a + b


def restar(a, b):
    return a - b


# utilidades.py
def imprimir_mensaje(mensaje):
    print(mensaje)


def obtener_nombre_usuario():
    return input("Ingresa tu nombre: ")



#import operaciones
#import utilidades


#resultado = operaciones.sumar(5, 3)
#utilidades.imprimir_mensaje(f"El resultado de la suma es: {resultado}")


#nombre = utilidades.obtener_nombre_usuario()
#utilidades.imprimir_mensaje(f"Hola, {nombre}!")


#  Paquetes 

# Crear y utilizar paquetes
#Para crear un paquete, creamos un directorio con el nombre deseado y agregamos un archivo especial llamado __init__.py dentro del directorio. Este archivo puede estar vacío o contener código de inicialización del paquete.

#Por ejemplo, creamos un directorio llamado mi_paquete con la siguiente estructura:

""""mi_paquete/
    __init__.py
    modulo1.py
    modulo2.py
    
    
    from mi_paquete import modulo1, modulo2


modulo1.funcion1()
modulo2.funcion2()"""


