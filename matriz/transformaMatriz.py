matriz_valores = [
    [15, 42, 7],
    [23, 91, 12],
    [34, 8, 55]
]

matriz_unificada = [n for conjunto in matriz_valores for n in conjunto]

maior = max(matriz_unificada)
menor = min(matriz_unificada)


