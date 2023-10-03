def maior_menor(numeros):
    maior = max(numeros)
    menor = min(numeros)

    return maior, menor

print(maior_menor([4, 3, 5, 6, 1, 9, 7]))

#Funçao com paramentros e retorno tipificado

def cumprimentar(nome: str) -> str:
    return 'Ola, ' + nome

print(cumprimentar('Valmir'))

from typing import List

def media(numeros: List[int]) -> float:
    return sum(numeros) / len(numeros)
print("Média")    
print(media([4, 3, 5, 6, 1, 9, 7]))

