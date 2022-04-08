

def opt1():
    i = 0
    while i < 51:
        print(i)
        i += 1
def pot2():
    i = 0
    while i < 21:
        print(i**2)
        i += 1
def salir():
    print("Gracias por participar")
    exit()

menu = int(input("""--Menu--
1- Imprimiendo numeros del 0 al 50
2- Imprimiendo numeros del 1 al 20
3- Salir

Elija su opcion: """))

if menu == 1:
    opt1()
if menu == 2:
    pot2()
if menu == 3:
    salir()
