numeroBinario = input("Digite um numero binario: ")
decimal = 0

for i, digito in enumerate(reversed(numeroBinario)):
    if digito == '1':
        decimal += 2 ** i
print("Resultado Decimal: ", decimal)

