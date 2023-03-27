nome = str(input('Qual o nome do vendedor? '))
salario = float(input('Qual o salário fixo? '))
totalV = float(input('Qual o valor total das vendas que foram feitas no mes? '))

comissao =  (totalV * 0.15)
salarioC = salario + comissao

print('A comissão é de:', comissao)
print('O salário é de: ', salario)
print('O salaio mais a comissão é de:', salarioC)