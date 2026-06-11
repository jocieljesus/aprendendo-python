vendas = [
    [1200, 850, 900, 1500],     # vendedor 1
    [900, 1100, 1000, 1300],    # vendedor 2
    [1500, 1600, 1400, 1800],   # vendedor 3
    [700, 600, 800, 900]        # vendedor 4
]

vendas_vendedores = [ sum(vendedor) for vendedor in vendas]

vendas_dia  = [ sum(dia) for dia in zip(*vendas)]

print("Total de vendas por vendedor: \n")

for i, valor in enumerate(vendas_vendedores, 1):
    print(f"O vendedor {i} vendeu R$ {valor}")

print("\nTotal de vendas por dia: \n")

for i, valor in enumerate(vendas_dia, 1):
    print(f"No dia {i} vendeu R$ {valor}")