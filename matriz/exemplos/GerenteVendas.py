"""
### Exercício 5: O Gerente de Vendas
Uma loja registrou o total de vendas de 4 vendedores durante os 4 dias de uma feira de eventos. Cada linha representa um vendedor e cada coluna representa o dia (Dia 1, Dia 2, etc.).
Crie um programa que processe esses dados e exiba:

1. O total vendido por cada vendedor (soma de cada linha).
2. O total vendido pela loja em cada dia da feira (soma de cada coluna).
"""


vendas = [
    [1200, 850, 900, 1500],
    [900, 1100, 1000, 1300],
    [1500, 1600, 1400, 1800],
    [700, 600, 800, 900]
]

vendedoresTotal = []
for i in vendas:
    vendasTotal = 0
    for j in i:
        vendasTotal += j
    vendedoresTotal.append(vendasTotal)

for i in range(len(vendedoresTotal)):
    print(f"O total de vendas do vendedor {i+1} foi de R$ {vendedoresTotal[i]}")

totalVendasPorDia = [0,0,0,0]
for i in range(4):
    for j in range(4):
        totalVendasPorDia[j] += vendas[i][j]

for i in range(len(totalVendasPorDia)):
    print(f"O total de vendas no dia {i+1} foi de R$ {totalVendasPorDia[i]}")


