# funciones en phyton
las funciones nos permite ordenar mejor el codigo y reutilizarlo cuando sea necesario.
```python
# ejemplo deseamos crear un programa en python que nos permite sumar dos numeros 
numero_uno:int=45
numero_dos:int=70
numero_tres:int=78
numero_cuatro:int=20
suma:int=numero_uno+numero_dos
suma_dos:int=numero_tres+numero_cuatro
print(suma)
print(suma_dos)
```
como hacemos reutilizable el ejercicio antereior y mas lejible.
para eso utilizaremos funciones.

la caracteristica es la siguiente :
1. debe comenzr con la palabra reservada
   'def'

2. debe tener un nombre que de a entender que realiza la funcion.
 
3. debera tener parametros y estos estaran encerrados en parentesis '()'
no todas las funciones resibiran parametros aun asi debera tener '()'

4. las funciones deberan retornar datos a traves de la palabra 'return'

```python

# crear un un programa que  me permita sumar dos numeros
def sumar (a,b):
    return a+b

 print(sumar(78,56))
 print(sumar(45,5))    
 ```  