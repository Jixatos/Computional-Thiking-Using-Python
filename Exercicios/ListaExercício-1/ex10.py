# Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, calcular e imprimir o total a receber no final do mês.

nome = input("Digite o nome: ")
salario = float(input("Digite seu salário fixo: "))
totalV = float(input("Digite o total de vendas *EM DINHEIRO*: "))

print(f"{nome} tem uma comissão de 15% de seu salário. \nSalário sem a comissão: {salario} \nSalário com comissão: {salario*1.15}")