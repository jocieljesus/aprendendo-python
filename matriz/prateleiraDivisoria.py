estoque = [

    [12, 5, 8],

    [3, 15, 2],

    [19, 0, 7]
]

prateleira, divisoria = input("Digite a prateleira e a divisoria separadas por vírgula: ").split(",")

print(f"A quantidade de caixas na posição solicitada é: {estoque[int(prateleira)-1][int(divisoria)-1]} ")