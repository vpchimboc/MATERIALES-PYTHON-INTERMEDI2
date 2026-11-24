#Funciones 
#Declarar funciones
def saludar():
    print("Hola, ¿cómo estás?")
#llamar a la función
saludar()


#Funciones con parámetros
def saludar(nombre):
    print(f"Hola {nombre}, ¿cómo estás?")

saludar("Juan")

#Funciones con retorno de valores
def sumar(a, b):
    return a + b

#Llamar a la función y almacenar el resultado
resultado = sumar(5, 3)
print(f"La suma es: {resultado}")

#Funciones con valores predeterminados
def saludar(nombre="amigo"):
    print(f"Hola {nombre}, ¿cómo estás?")

saludar()  # Usando el valor predeterminado
saludar("María")  # Sobrescribiendo el valor predeterminado

#Funciones con argumentos arbitrarios
def sumar_numeros(*numeros):
    return sum(numeros)

#Llamar a la función con diferentes cantidades de argumentos
resultado = sumar_numeros(1, 2, 3, 4, 5)
print(f"La suma de los números es: {resultado}")

#Funciones con argumentos de palabras clave arbitrarias
def mostrar_info(**info):
    for clave, valor in info.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Juan", edad=30, ciudad="Madrid")

#Funciones anónimas (lambda)
#Definir una función lambda para sumar dos números
sumar_lambda = lambda a, b: a + b
#Llamar a la función lambda
resultado_lambda = sumar_lambda(10, 5)
print(f"La suma usando lambda es: {resultado_lambda}")

#Funciones recursivas
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1) 

#Llamar a la función recursiva
resultado_factorial = factorial(5)
print(f"El factorial de 5 es: {resultado_factorial}")
#funciones dentro de funciones
def funcion_externa():
    def funcion_interna():
        print("Hola desde la función interna")
    funcion_interna()
#Llamar a la función externa
funcion_externa()
