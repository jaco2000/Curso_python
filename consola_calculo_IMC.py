print("\n Aquí se calculará el índice de masa corporal \n")

import calculadora_indice as IMC

peso = float(input("Ingrese el peso de la persona (Kilogramos): "))
altura= float(input("Ingrese altura de la persona (Metros): "))

resultado = IMC.calcular_IMC(peso, altura)

print("Su índice de masa corporal es:", resultado)