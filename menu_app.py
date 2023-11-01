import os
def agregar_compra(compras_realizadas):

    compra = int(input("Ingrese el monto de la compra: "))
    compras_realizadas.append(compra)
    print("La compra se ha realizado con exito.")
    print("========================================================================")
    input("Presiona enter para continuar.")
    os.system('cls')


def mostrar_compras(compras_realizadas):
    if not compras_realizadas:
        print("No hay compras agregadas.")
    else:
        for numero, precio in enumerate(compras_realizadas, 1):
            print(f"Compra {numero}: ${precio:,}")
    print("========================================================================")
    input("Presiona enter para continuar.")
    os.system('cls')

def mostrar_total(compras_realizadas):
    total = sum(compras_realizadas)
    print(f"El total de la compra es ${total:,}")
    print("========================================================================")
    input("Presiona enter para continuar.")
    os.system('cls')

def main():
    compras = []
    
    while True:
        print("========================================================================")
        print("1) Agregar compra")
        print("2) Mostrar compras")
        print("3) Mostrar total gastado")
        print("4) Salir")
        print("========================================================================")

        opcion = int(input("Por favor ingrese una opción: "))
        if opcion == 1:
            os.system('cls')
            print("Usted ha elegido 'Agregar compra'.")
            print("|=======|====================================|=======|")
            agregar_compra(compras)
            
        elif opcion == 2:
            os.system('cls')
            print("Usted ha elegido 'Mostrar compras'.")
            print("|=======|====================================|=======|")
            mostrar_compras(compras)
            
        elif opcion == 3:
            os.system('cls')
            print("Usted ha elegido 'Mostrar total gastado.'")
            print("|=======|====================================|=======|")
            mostrar_total(compras)
            
        elif opcion == 4:
            os.system('cls')
            print("Hasta luego!")
            break
        else:
            print("Opción no valida. Por favor ingrese una opción valida")


main()