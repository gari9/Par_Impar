
# Programa para verificar si un numero es par o impar

# Funcion para verificar si un numero es par o impar

# La funcion recibe un numero y si el dividendo de ese numero entre 2 es 0, entonces es par, de lo contrario es impar

def par_impar(numero):
    if numero % 2 == 0:
        print("El numero es par")
    else:
        print("El numero es impar")

numero = int(input("Ingrese un numero: "))


par_impar(numero)

print("Fin del programa")

