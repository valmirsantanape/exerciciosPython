class Pessoa:
    def  __init__(self, nome, idade):
        self.nome =  nome
        self.idade = idade

        print(f'{self.nome} foi criado.')
    
    def __del__(self):
        print(f'{self.nome} foi deletado. ')
    

    def falar(self, mensagem):
        print(f'{self.nome} diz: {mensagem}')


pessoa1 = Pessoa('Antonio', 35)
pessoa2 = Pessoa('Maria', 29)
pessoa3 = Pessoa('Marcos', 27)

mensagem1 = pessoa1.falar("Olá, como estão vocês? ")
print(mensagem1)


class Cliente:
    def __init__(self, nome, idade, limite):
        self.nome = nome
        self.idade = idade
        self.__limite = limite

    def comprar(self, valor):
        if valor > self.__limite:
            print('Compra não autorização ')
        else: 
            print('Compra autorizada')

cliente1 = Cliente('Marta', 36, 3500)
compra1 = cliente1.comprar(4000)
compra2 = cliente1.comprar(3000)

print(compra1)
print(compra2)
