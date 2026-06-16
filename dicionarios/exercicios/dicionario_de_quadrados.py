
dicionario_de_quadrados = {"Chave" : "Valor"}

for i in range(1, 6):
    dicionario_de_quadrados.setdefault(i, i**2)


for k,v in dicionario_de_quadrados.items():
    print(F"  {k}  ->  {v}")



lista = ["macarrao", "feijao", "arroz", "feijao", "carne", "arroz", "miojo","arroz"]

print("Quantos arrozes", lista.count("feijao"))
