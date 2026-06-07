"""
### Exercício 4: Multiplicador de Matriz por Escalar

Escreva um programa que pegue uma matriz de números inteiros qualquer e multiplique todos os seus elementos por um número digitado pelo usuário (fator de escala). No final, exiba a nova matriz formatada linha por linha.
"""

matrizBase = [ [1,2], [3,4]]

fator = int(input("Digite um fator para escalarmos a matriz base: "))

matrizFatorada = []

for i in matrizBase:
    vetorFator = []
    for j in i:
        vetorFator.append(j*fator)
    matrizFatorada.append(vetorFator)


print(f"Matriz Base = {matrizBase}")
print(f"Matriz Fatorada = {matrizFatorada}")