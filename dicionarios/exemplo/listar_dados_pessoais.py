dados_pessoais = {
    "nome" : "Joao",
    "idade" : 17,
    "nascimento" : "20-05-2005",
    "sexo" : "M",
    "altura": 170,
    "temCNH" : True
}

for chave,valor in dados_pessoais.items():
   print(f"{chave}:{valor}")

print("------------------------------------------")

#Remove e retornar o valor removido ou o valor padrão
print( dados_pessoais.pop("peso", "Chave nao existe!" ) )
print( dados_pessoais.pop("nascimento", "Chave nao existe!" ) )
print( dados_pessoais.popitem()  )

print("------------------------------------------")
#Como imprimir somente os valores
print( dados_pessoais.values() )

print("------------------------------------------")
print("Setando valor: ")
#Seta um valor novo ou retorna um existente
print(
dados_pessoais.setdefault("peso", 80),
dados_pessoais.setdefault("telefone", "6199999775"),
dados_pessoais.setdefault("idade", 25)
)

print(dados_pessoais.clear())
print(dados_pessoais)
