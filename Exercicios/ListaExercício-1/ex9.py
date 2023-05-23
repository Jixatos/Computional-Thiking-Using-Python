# Escreva um programa que leia o número de cadastro de um funcionário, seu número de horas trabalhadas, o valor que recebe por hora e calcula o salário desse funcionário. A seguir, mostre na tela o número e o salário do funcionário.

id = input("Número de cadastro: ")
hs = int(input("Número de horas trabalhadas: "))
mh = float(input("Quanto recebe por hora: "))

print(f"O funcionário com o registro {id} tem o salário de {mh * hs}")