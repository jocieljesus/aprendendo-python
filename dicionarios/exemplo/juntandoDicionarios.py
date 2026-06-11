carro1 = {
    "marca" : "Chevrolet",
    "modelo" : "Chevete",
    "ano" : 1998
}


carro2 = {
    "modelo" : "brasília",
    "cor": "amarelo",
    "placa" : "JPG4021"
}

carro_completo = {**carro1, **carro2} #Cria novo dicionario com os 2 valores

novo_carro = carro1 | carro2

print(f"Novo Carro:{novo_carro}\n")


print(f"Carro completo{carro_completo}\n")


carro1.update(carro2) # Atualiza dicionario
print(f"Carro 1 atualizado com update: {carro1}")


carro1 |= carro2

print(f"Carro 1 atualizado | : {carro1}")
