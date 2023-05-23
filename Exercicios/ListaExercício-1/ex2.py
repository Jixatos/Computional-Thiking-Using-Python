#Fazer  um  algoritmo  que  lê  dois  números,  a  base  e  o  expoente,  e  imprime  a  potência  (base  elevada  ao expoente).

import math

base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

print(f"{base} elevado a {expoente} é {math.pow(base, expoente)}")