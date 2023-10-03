from math import sqrt

def imc(peso, altura):
    return peso/(altura * altura)
'''
#Calculando IMC
print("*" *30)
peso = float(input("Informe seu peso: \n"))
altura = float(input("Informe sua altura: \n"))
imc = imc(peso, altura)

print(f'O seu imc é: {imc:.2f}')
'''
print("*" * 30)
print('Para obter as raizes da equação do segundo grau, informe os valores que corresponderão respectivamente a A, B e C: \n'
    '"Ax² + Bx + C = 0"')

print("*" * 30)
A = int(input('Informe o valor de "A": '))
B = int(input('Informe o valor de "B": '))
C = int(input('Informe o valor de "C": '))



delt = B**2 - 4 *A*C

rDelt = sqrt(delt)
print(rDelt)

print(B, A)
x1 = (-B + rDelt ) / (2*A)
x2 = (-B - rDelt ) / (2*A)

print('S:{'f'{x1}, {x2}',"}")