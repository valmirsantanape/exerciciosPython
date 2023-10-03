class Pessoa:
    def __init__(self, nome, idade,):
        self.nome = nome
        self.idade = idade
    
    def falar(self, mensagem):
        print(f'{self.nome} diz: {mensagem}')

class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario
    
    def falar(self, mensagem):
        print(f'{self.nome} diz: {mensagem} Estou no trabalho!')


funcionaro1 = Funcionario('André', 30, 3800)
print(funcionaro1.nome, funcionaro1.idade, funcionaro1.salario)

funcionaro1.falar('Bom dia! ')