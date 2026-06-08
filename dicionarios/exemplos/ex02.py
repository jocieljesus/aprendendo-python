frase = input("Digite uma frase qualquer e que possa conter palavras repetidas: ")

palavras = frase.split()

contador  = {}


for p in palavras:
    p = p.lower()

    if p in contador:
        contador[p] += 1
    else:
        contador[p] = 1

print("Contagem de palavras: ")
print(contador)