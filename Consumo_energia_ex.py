#Calculo do consumo de Energia

kwh = int(input('Quantos kWh você já consumiu? '))
valorMin = 11.9


if kwh < 150:
    totalPg = kwh * 0.2
elif kwh >= 150 and kwh < 500:
    totalPg = kwh * 0.25
else:
    totalPg = kwh * 0.30
    
if totalPg > valorMin:
    print('Você irá pagar um valor de ', totalPg)
else:
    print('Você irá pagar um valor de ', valorMin)
    
print('Fim!')