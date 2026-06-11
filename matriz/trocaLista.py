
matriz_A = [
    [1, 2, 3],
    [4, 5, 6]
]

matriz_T = [list(coluna) for coluna in zip(*matriz_A)]


for i in matriz_T:
    print(i)