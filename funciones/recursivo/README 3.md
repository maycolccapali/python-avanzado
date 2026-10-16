La recursión es un concepto fundamental en programación, y tiene especial importancia en Python. Se refiere a la técnica en la que una función se llama a sí misma para resolver un problema, descomponiéndolo en subproblemas más pequeños y manejables. 

Este método permite soluciones elegantes y concisas, sobre todo cuando se trata de problemas que implican tareas repetitivas o estructuras jerárquicas. En Python, la recursividad se utiliza en una gran variedad de aplicaciones, desde la ordenación algoritmos a complejos recorridos de datos. 

Las soluciones recursivas suelen reflejar las definiciones matemáticas de los problemas, lo que las hace intuitivas para quienes están familiarizados con el razonamiento matemático. La belleza de la recursividad reside en su capacidad para expresar algoritmos complejos en unas pocas líneas de código, creando soluciones elegantes y legibles. Sin embargo, dominar la recursividad requiere un cambio de mentalidad respecto a los enfoques iterativos más comunes.

**ejemplos**


Ejemplos en código


1. Factorial de un número

```python
def cuenta_regresiva(n):
    if n == 0:  # Caso base
        print("¡Despegue!")
    else:
        print(n)
        cuenta_regresiva(n - 1)  # Caso recursivo

cuenta_regresiva(5)
```


2. Cuenta regresiva
   
   ```python
   def factorial(n):
    if n == 0 or n == 1:  # Caso base
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))
print(factorial(4))
print(factorial(3))```



cuenta_regresiva(5)
# Salida:
# 5
# 4
# 3
# 2
# 1
# ¡Despegue!
