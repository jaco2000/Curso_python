print("\n Aquí se calculará el rango de calorias recomendado \n")


import calculadora_indice as Rango

peso = float(input("Ingrese el peso de la persona (Kilogramos): "))
altura= float(input("Ingrese altura de la persona (Centimetros): "))
edad= int(input("Ingrese su edad: "))
valor_genero = float(input("Ingrese genero, masculino (5) y femenino (-161): "))

CalActividad = Rango.consumo_calorias_recomendado_para_adelagazar(peso, altura, edad, valor_genero)

print("Para adelgazar es recomendable que consumas entre: ", CalActividad, "calorias al día")