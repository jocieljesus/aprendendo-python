estoque = {
    "Teclado": 15,
    "Mouse": 22,
    "Monitor": 0
}

while True:
    retornoCliente = input("Digite qual produto e a quantidade que voce deseja, separado por vigula: ").split(",")

    produto = retornoCliente[0]
    quantidade = int(retornoCliente[1])
    if estoque[produto] >= quantidade:
        estoque[produto] -= quantidade
        print(f"Estoque Atualizado: {estoque}")
    elif estoque[produto] > 0:
        print("Quantidade do produto solicitado Insuficiente")
    else:
        print("Produto Esgotado!")
    continuar = input("Quer realizar novo pedido ? s/n: ").lower()
    if( continuar == "n"):
        break
