listaNumeros = []

for i in range(1,7):
    numero = int(input(f"Digite o {i}° número:"))
    listaNumeros.append(numero)

listaNumeros.sort()
print(listaNumeros)

print(f"A soma é : {sum(listaNumeros)}")
print(f"O maior número é: {max(listaNumeros)}")
print(f"O menor número é: {min(listaNumeros)}")
