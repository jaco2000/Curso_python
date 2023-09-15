print("\n Aquí se calculará el porcenaje de grasa \n")


import calculadora_indice as PG

peso = float(input("Ingrese el peso de la persona (Kilogramos): "))
altura= float(input("Ingrese altura de la persona (Metros): "))
edad= int(input("Ingrese su edad: "))
valor_genero = float(input("Ingrese genero, masculino (10.8) y femenino (0): "))

PorG = PG.calcular_porcentaje_grasa(peso, altura, edad, valor_genero)

print("Su porcentaje de grasa es:", PorG, "%")