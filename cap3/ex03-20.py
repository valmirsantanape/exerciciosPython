
print("Sequencia de fotoriais")
print("Descubra o fatorial de todos os numeros até o numero indicado: ")

numero = int(input('Numero: '))
print('=-' * 30)
for i in range(1, numero + 1):
    num = i
    fatorial = num

    for c in range(num - 1, 0, -1):
        fatorial = fatorial * c
    
    print(f'O fatorial de {num} é: {fatorial}')
    
print('=-' * 30)