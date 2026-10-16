La recursión es un concepto fundamental en programación, y tiene especial importancia en Python. Se refiere a la técnica en la que una función se llama a sí misma para resolver un problema, descomponiéndolo en subproblemas más pequeños y manejables. 

Este método permite soluciones elegantes y concisas, sobre todo cuando se trata de problemas que implican tareas repetitivas o estructuras jerárquicas. En Python, la recursividad se utiliza en una gran variedad de aplicaciones, desde la ordenación algoritmos a complejos recorridos de datos. 

Las soluciones recursivas suelen reflejar las definiciones matemáticas de los problemas, lo que las hace intuitivas para quienes están familiarizados con el razonamiento matemático. La belleza de la recursividad reside en su capacidad para expresar algoritmos complejos en unas pocas líneas de código, creando soluciones elegantes y legibles. Sin embargo, dominar la recursividad requiere un cambio de mentalidad respecto a los enfoques iterativos más comunes.

**ejemplos**


Ejemplos en código


1. Factorial de un número

El factorial de un número (n!) es el producto de todos los enteros desde 1 hasta n.
python
def factorial(n):
    # Caso base: el factorial de 0 o 1 es 1
    if n <= 1:
        return 1
    # Caso recursivo: n * factorial del número anterior
    return n * factorial(n - 1)

print(factorial(5))  # Salida: 120


2. Cuenta regresiva

Un ejemplo sencillo sin multiplicaciones, ideal para ver la pila de llamadas:
python
def cuenta_regresiva(n):
    # Caso base
    if n <= 0:
        print("¡Despegue!")
    else:
        print(n)
        # Caso recursivo
        cuenta_regresiva(n - 1)

cuenta_regresiva(5)
# Salida:
# 5
# 4
# 3
# 2
# 1
# ¡Despegue!