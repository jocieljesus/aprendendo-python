"""
Exercício 1: O Localizador (Fácil)
Dada a matriz abaixo, que representa o estoque de caixas em um armário de 3 prateleiras (linhas) e 3 divisórias (colunas), crie um programa que peça para o usuário digitar o número da prateleira e o número da divisória e exiba a quantidade de caixas naquele local.
"""

estoque = [
    [12, 5, 8],
    [3, 15, 2],
    [19, 0, 7]
]

print("----------------------------------")
print("     BEM VINDO AO SEU ESTOQUE     ")
print("----------------------------------")
for i in estoque:
    print(i)
prateleira = int(input("Digite o número da prateleira que você quer acessar: "))-1
divisoria = int(input("Digite o número da divisória que você quer acessar:"))-1

print(f"Na prateleira e divisoria informada foram encontradas '{estoque[prateleira][divisoria]}' caixas.")
