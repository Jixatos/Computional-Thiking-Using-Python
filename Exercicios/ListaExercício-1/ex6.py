# Escreva   um   algoritmo   que   leia   três   números   decimais:   A,   B   e   C.   Em   seguida,   calcule   e   mostre: 
# a) a área do triângulo retângulo que tem A por base e C por altura.
# b)    a    área    do    círculo    de    raio   C.    (π    =    3.14159)
# c) a área do trapézio que tem A e B por bases e C por altura.
# d) a área do quadrado que tem lado B.
# e) a área do retângulo que tem lados A e B
# f) o perímetro do retângulo que tem lados A e B.

a = float(input("Digite o número A:"))
b = float(input("Digite o número B:"))
c = float(input("Digite o número C:"))

enunciadoA = (a*c)/2
enunciadoB = 2*3.14159*c
enunciadoC = (a+b)*c/2
enunciadoD = b*b
enunciadoE = a*b
enunciadoF = a+a+b

print(enunciadoA)
print(enunciadoB)
print(enunciadoC)
print(enunciadoD)
print(enunciadoE)
print(enunciadoF)