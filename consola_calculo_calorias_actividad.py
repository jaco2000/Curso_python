print("\n Aquí se calculará calorias que quema actividad fisica \n")


import calculadora_indice as CA

peso = float(input("Ingrese el peso de la persona (Kilogramos): "))
altura= float(input("Ingrese altura de la persona (Centimetros): "))
edad= int(input("Ingrese su edad: "))
valor_genero = float(input("Ingrese genero, masculino (5) y femenino (-161): "))
valor_actividad = float(input("Actividad fisica semanal: "))

CalActividad = CA.calcular_calorias_en_actividad(peso, altura, edad, valor_genero, valor_actividad)

print("Su porcentaje de grasa es:", CalActividad, "Cal")