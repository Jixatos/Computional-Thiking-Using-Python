# Leia 3 números decimais A, B e C e efetue o cálculo das raízes da equação de Bhaskara.
# Se não for possível calcular as raízes, ou seja, caso haja uma divisão por 0 ou raiz de número negativo, mostre a mensagem correspondente “Impossível calcular”.

import math

a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

delta = (b*b)-4*a*c
if delta > 0:
    raiz = math.sqrt(delta)
    x1 = (-(b)+raiz)/2*a
    x2 = (-(b)-raiz)/2*a

    if x1 == 0 or x2 == 0:
        print("Impossível calcular")
    else:
        print(f" x'={x1} e x''={x2} ")
else:
    print("Impossível calcular")
