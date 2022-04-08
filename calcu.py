import os
os.system("clear")

print("Caluladora \n")


def Suma(a, b):
    return a+b


def Resta(a, b):
    return a-b


def Multiplicacion(a, b):
    return a*b


def Division(a, b):
    return a/b


while True:
    opciones = int(input("""--Menu--
    1.Sumar
    2.Restar
    3.Multiplicar
    4.Dividir
    5.Salir
    Elija su opcion: """))
    N1 = int(input("Coloque el primer numero "))
    N2 = int(input("Coloque el segundo numero "))

    if opciones == 1:
        print("EL resultados es ", Suma(N1, N2))

    if opciones == 2:
        print("EL resultados es ", Resta(N1, N2))

    if opciones == 3:
        print("EL resultados es ", Multiplicacion(N1, N2))

    if opciones == 4:
        print("EL resultados es ", Division(N1, N2))

    if opciones == 5:
        print("Gracias por usar la calculadora")
        break
