print('Informe um numero para verificar se ele é primo.')
num = int(input('Numero: '))

if num > 3:
    for c in range(2, num):
        if num % c == 0:
            print(f'{num} não é um numero primo.')
            break
        else:     
            print(f'{num} é um numero é primo.')
            break
else:
    print(f'{num} é um numero é primo.')