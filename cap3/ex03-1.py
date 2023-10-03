for c in range(1, 101):
    print(c, '', end='')

print("=-" * 30)
for c in range(0, 101, 2):
    print(c, '', end='')

print("=-" * 30)
for c in range(1, 101, 2):
    print(c, '', end='')

soma = 0
print("=-" * 30)
for c in range(0, 101, 2):
    soma = soma + c
    print(c, '', end='')
print("\nSoma de todos os pares de 0 a 100", soma)
