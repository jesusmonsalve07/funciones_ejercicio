print("---------------------------------------") 
print("--------- CONVERSOR MONEDAS -----------") 
print("---------------------------------------")

# funcion para hacer la conversion

def convertir(tipo_pesos, valor_dolar): 
    pesos = input("¿Cuantos pesos " + tipo_pesos + "tienes?") 
    pesos = float(pesos) 
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2) 
    dolares = str(dolares)
    print("Tienes $ " + dolares + " dolares") 

    # funcion principal del programa 
    def funcion_principal():
        menu = """
        Bienvenidos al conversor de monedas 
        1 - Pesos colombianos
        2 - Pesos Argentinos
        3 - Pesos mexicanos
        
        Elige la opcion: """ 

        opcion = int(input(menu)) 
        if opcion == 1:
            convertir("Colombianos", 3966)
        elif opcion == 2:
            convertir("Argentinos", 122.52) 
        elif opcion == 3:
            convertir("Mexicanos", 20.62) 
        else:
            print("Ingrese una opcion correcta")

        # Inicializar el programa
        if __name__ == "__main__": 
            funcion_principal() 