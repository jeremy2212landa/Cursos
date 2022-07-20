import random

def run():
    nalea = random.randint(1, 20)
    neleg = int(input("Ingrese un número del 1 al 20: "))
    while neleg != nalea:
        if neleg < nalea:
            print("Ingresa un numero mas grande.")
        else:
            print("Ingresa un numero mas pequeño. ")
        neleg = int(input("elije otro numero: "))
    print("Ganaste!!!")

if __name__ =="__main__":
    run()