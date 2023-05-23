# Fazer um algoritmo que leia dois números e imprime a divisão do maior pelo menor.

x = float(input("Digite o número 1: "))
y = float(input("Digite o número 2: "))

if x > y:
    print(f"O resultado é {x/y}")
else:
    print(f"O resutlado é {y/x}")