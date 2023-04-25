'''
Calcular imposto de renda real, diminuição de IR por tempo.

Renda até R$ 1.903,98: isento de imposto de renda;
Renda entre R$ 1.903,99 e R$ 2.826,65: alíquota de 7,5%;
Renda entre R$ 2.826,66 e R$ 3.751,05: alíquota de 15%;
Renda entre R$ 3.751,06 e R$ 4.664,68: alíquota de 22,5%;
Renda acima de R$ 4.664,68: alíquota máxima de 27,5%.

https://www.creditas.com/exponencial/tabela-imposto-de-renda/
'''

salario = float(input('Digite seu salário mensal:'))
salarioL = ''
aliquota = ''
imposto = ''
