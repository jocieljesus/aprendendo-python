dados_pessoais = {
    "nome" : "Joao",
    "idade" : 21,
    "nascimento" : "20-05-2005",
    "sexo" : "M",
    "altura": 1.70,
    "temCNH" : True
}


dados_pessoais["altura"] = 1.85
dados_pessoais["peso"] = 70
dados_pessoais.pop("idade") #Remove o item

continuar = "s"
while  continuar == "s":
    nova_chave, novo_valor = input("Digite uma nova chave e um novo valor ou realize uma atualizacao de dado: ").split(
        ",")
    dados_pessoais[nova_chave] = novo_valor
    print(dados_pessoais.keys())

    dados = input("Digite o que você quer encontrar: ")

    print(dados_pessoais.get(dados, "Valor não encontrado!"))

    continuar = input("Quer continuar? (s/n): ")[0].lower()

