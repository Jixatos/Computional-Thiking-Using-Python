# Fazer um algoritmo que leia os dois lados Ae Bde um triângulo retângulo e calcula a hipotenusa do triângulo. Para  esse  caso,  considere  que ℎ𝑖𝑝𝑜𝑡𝑒𝑛𝑢𝑠𝑎=√𝐴2+𝐵2.  

import math

a = float(input("Digite o Lado A do triângulo: "))
b = float(input("Digite o lado B do triângulo"))

print(f"A hipotenusa do triangulo com lado {a} e lado {b} é de {math.sqrt((a*a)+(b*b))}")