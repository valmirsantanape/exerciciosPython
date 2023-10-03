print('Informe a cor do semaforo: ')
print(" 1 - Vermelhor \n","2 - Amarelo\n","3 - Verde")
semaforo = int(input('Cor do semaforo: '))

match semaforo:
    case 1:
        print("Vermelho: Pare!")
    case 2:
        print("Amarelo: Prepare-se para parar! ")
    case 3:
        print("Verde: Prossiga! ")
    case _ :
        print('Cor inválida! ')