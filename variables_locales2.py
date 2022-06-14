from re import X 
"""Se omite el parametro x en el llamado de la funcion ya que la variable es global"""
def f():
    global x
    x = x + 1 
    print("Valor de x dentro de f(x) =", x) 
    return X


# Algoritmo principal 
x = 3
print("Valor inicial de x = ", x)
z = f(x) 
print("Valor de x despues de llamar a f(x) =" , x)

""" 
SALIDA:
Valor inicial de x = 3
Valor de x dentro de f(x) = 4
Valor de x despues de llamar a f(x) = 4""" 