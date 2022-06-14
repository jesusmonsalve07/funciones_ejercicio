# FUNCIONES 

## VARIABLE LOCALES Y GLOBALES 

### Variables locales 
Variables que se definen dentro de una funcion.
Son validas unicamente dentro de la funcion.
Las variables correspondientes a la funcion solamente son accesibles por la funcion, es decir, se pueden usar solamente por ella. Al usarlas fuera de la funcion marcara error.
Una variable del algoritmo principal que se pasa a una funcion donde se modifica y es variable local, cambia su valor en la funcion pero NO en el algoritmo principal.

### Variables globales 
- Son aquellas que no importa donde se usen o modifiquen siempre conservan los valores asignados, ya sea en el algoritmo principal o en las funciones.
- Para hacer que una variable sea global hay que definirlacomo tal por medio de la instruccion `global nombre_variable` 

## LLAMADO POR VALOR Y LLAMADO POR REFERENCIA 

### Paso por valor 
- Cuando se pasa una variable a una funcion creando una nueva localidad de memoria, donde se copian los valores de los parametros de la funcion.
- La memoria ocupada aumenta de tamaño 
- Aunque en Python no se aumenta la memoria, el paso de la variable es equivalente a paso por valor.

### Paso por referencia 
- La variable se puede modificar en la funcion y el cambio siempre se realiza usando la referencia a la localidad de memoria donde se almacena la variable. Ej. variables tipo lista.

## FUNCIONES LAMBDA

- Declaracion de una funcion en un solo renglon
`f = lambda parametros: expresion de la funcion f` 