'''Calculo imposto de renda'''

salario = float(input('Qual o salário? '))
aliquota = float()

if salario < 1257.12:
    aliquota = (0)
elif salario >= 1257.12 and salario <= 2510:
    aliquota = (0.17)
else:
    aliquota = (0.28)

imposto = float(salario * aliquota)
salarioL = float(salario - imposto)

match aliquota:
    case (0):
        print('Salário bruto: ', salario)
        print('Salário Liquido:', salarioL)
        print('Aliquota: ', aliquota)
        print('Imposto: ', round(imposto), 2)
    case (0.17):
        print('Salário bruto: ', salario)
        print('Salário Liquido:', salarioL)
        print('Aliquota: ', aliquota)
        print('Imposto: ', round(imposto), 2)
    case (0.28):
        print('Salário bruto: ', salario)
        print('Salário Liquido:', salarioL)
        print('Aliquota: ', aliquota)
        print('Imposto: ', round(imposto), 2)
    





