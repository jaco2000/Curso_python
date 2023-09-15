print("\n Aquí se calculará calorias que quema estando en reposo \n")


import calculadora_indice as CR

peso = float(input("Ingrese el peso de la persona (Kilogramos): "))
altura= float(input("Ingrese altura de la persona (Centimetros): "))
edad= int(input("Ingrese su edad: "))
valor_genero = int(input("Ingrese genero, masculino (5) y femenino (-161): "))

CalReposo = CR.calcular_calorias_en_reposo(peso, altura, edad, valor_genero)

print("Su porcentaje de grasa es:", CalReposo, "Cal")