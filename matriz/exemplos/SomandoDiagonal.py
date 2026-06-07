"""
Exercício 2: Somando a Diagonal
Em matemática, a diagonal principal de uma matriz quadrada é aquela que vai do canto superior esquerdo ao canto inferior direito (onde o índice da linha é igual ao índice da coluna). Escreva um programa que calcule e mostre a soma de todos os elementos da diagonal principal da matriz abaixo:
"""

matrizQuadrada = [
    [5, 2, 9],
    [1, 8, 3],
    [4, 7, 6]
]

somaDiagonal = 0
for i in range(len(matrizQuadrada)):
    somaDiagonal += matrizQuadrada[i][i]


print(f"A soma dos elementos da diagonal principal é {somaDiagonal}")