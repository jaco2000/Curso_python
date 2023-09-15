# Calcular indice de masa corporal  
def calcular_IMC (peso: float, altura: float)->float:
    return round(peso/(altura**2), 2)

# Calcular porcentaje de grasa de una persona
def calcular_porcentaje_grasa (peso: float, altura: float, edad: int, valor_genero: float)->float:
    IMC = calcular_IMC (peso, altura)
    gc = (1.2*IMC)+(0.23*edad)-5.4-(valor_genero)
    return round (gc , 2)

#Calcular cantidad de calorias que una persona quema en reposo 
def calcular_calorias_en_reposo (peso: float, altura: float, edad: int,valor_genero: int)-> float:
    TMB = (10*peso)+(6.25*altura)-(5*edad)+valor_genero
    return round (TMB, 2)

#Calorias al realizar actividad física 
def calcular_calorias_en_actividad (peso: float, altura: float, edad: int, valor_genero: float, valor_actividad: float)->float:
    return round(calcular_calorias_en_reposo(peso, altura, edad, valor_genero)*valor_actividad, 2)

#Calculo rango calorias recomendado
def consumo_calorias_recomendado_para_adelagazar (peso: float, altura: float, edad: int, valor_genero: float)-> str: 
    ccer = calcular_calorias_en_reposo (peso, altura, edad, valor_genero)
    cal_1= str (round((ccer * 0.80),2))
    cal_2= str (round((ccer* 0.85),2))
    return str(cal_1 +" y "+ cal_2)
