def funcion(x):
    x.append(5) 

# Programa principal

x = [1,2] 
funcion(x)
print(x)

"""Salida:
[1,2,5]

El programa principal genera la lista [1,2] que se pasa a la funcion.
La funcion agrega el elemento 5 al final de la lista
Como la lista se pasa por referencia, automaticamente aparece con el programa principal en la llamada de la funcion.
Todos los arreglos, de cualquier tipo, y de cualquier dimension, se pasan por referencia""" 