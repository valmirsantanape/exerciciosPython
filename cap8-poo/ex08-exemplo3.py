class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def falar(self, mensagem):
        print(f'{self.nome} diz: {mensagem}')


class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario
    
    def falar(self, mensagem):
        print(f'{self.nome} diz: {mensagem} Estou no trabalho.')


funcionario = Funcionario('Antonio', 30, 50000)
funcionario.falar('Bom dia! ')