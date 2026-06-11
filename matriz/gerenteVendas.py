vendas = [
    [1200, 850, 900, 1500],     # vendedor 1
    [900, 1100, 1000, 1300],    # vendedor 2
    [1500, 1600, 1400, 1800],   # vendedor 3
    [700, 600, 800, 900]        # vendedor 4
]
vendas_vendedores = []
for vendedor in vendas:
    total_vendas = 0
    for valor_dia in vendedor:
        total_vendas += valor_dia
    vendas_vendedores.append(total_vendas)
vendas_dia = [0, 0, 0, 0]
for vendedor in range(len(vendas)):
    for dia in range(len(vendas[0])):
        vendas_dia[dia] += vendas[vendedor][dia]
print(" Total de vendas por vendedor foi:  ")
for i in range(len(vendas)):
    print(f" Vendedor {i+1} = R$ {vendas_vendedores[i]:.2f} " )
print(" ")
print(" Total de vendas por dia foi:  ")
for i in range(len(vendas)):
    print(f" Dia {i+1} =  R$ {vendas_dia[i]:.2f} " )








