'''
listas []
dicionarios[] chave:valor
conjuntos{}
tuplas()

'''


nome = str(input("Nome do funcionario: "))
salario = float(input(f"Salário bruto de {nome}: "))
percentualTaxa = float(input(f"Imposto cobrado sobre o salario de R${salario:.2f}: "))

taxa = percentualTaxa / 100
salarioLiquido = salario - (salario * taxa)
print(f'{nome} tem um salário de R${salarioLiquido:.2f} ')