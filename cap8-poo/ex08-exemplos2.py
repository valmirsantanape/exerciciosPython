class Cliente:
    def __init__(self, nome, idade, limite):
        self.nome = nome
        self.idade = idade
        self.__limite = limite
    
    def compra(self, valor):
        if valor > self.__limite:
            print('Compra não autorizada ')
        else:
            print('Compra autorizada. ')

cliente = Cliente('Antonio', 18, 800)

#cliente._Cliente__limite = 2000

cliente.compra(1500)