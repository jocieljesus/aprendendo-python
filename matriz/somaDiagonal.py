matriz_quadrada = [
    [5, 2, 9, 12],
    [1, 8, 3, 7],
    [4, 7, 6, 8],
    [4, 7, 6, 12]
]

numeros = []
for i in range(len(matriz_quadrada)):
    numeros.append(matriz_quadrada[i][i])

print(f"A soma da diagonal da matriz quadrada de {"+".join(map(str, numeros))} =  {sum(numeros)}")