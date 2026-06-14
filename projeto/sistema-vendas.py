# --- BANCO DE DADOS SIMULADO ---
# Utilizando dicionário para o estoque (Chave: ID do produto)
estoque = {
    1: {"nome": "Teclado Mecânico", "preco": 180.00, "quantidade": 15},
    2: {"nome": "Mouse Wireless", "preco": 120.00, "quantidade": 20},
    3: {"nome": "Monitor 24' Full HD", "preco": 850.00, "quantidade": 5},
}

carrinho = []  # Lista de dicionários para as compras atuais


# --- FUNÇÕES AUXILIARES ---
def exibir_estoque():
    print("\n--- PRODUTOS DISPONÍVEIS ---")
    print(f"{'ID':<5} | {'Nome':<25} | {'Preço':<10} | {'Estoque':<10}")
    print("-" * 55)
    for id_prod, info in estoque.items():
        print(f"{id_prod:<5} | {info['nome']:<25} | R$ {info['preco']:>7.2f} | {info['quantidade']:<10}")


def adicionar_ao_carrinho():
    exibir_estoque()
    try:
        id_escolhido = int(input("\nDigite o ID do produto que deseja comprar: "))

        if id_escolhido in estoque:
            qtd = int(input(f"Quantas unidades de '{estoque[id_escolhido]['nome']}' deseja? "))

            # Validação de estoque
            if qtd <= 0:
                print("❌ Quantidade inválida.")
            elif qtd <= estoque[id_escolhido]["quantidade"]:
                # Adiciona ao carrinho (lista de dicionários)
                item = {
                    "id": id_escolhido,
                    "nome": estoque[id_escolhido]["nome"],
                    "preco_unitario": estoque[id_escolhido]["preco"],
                    "quantidade": qtd
                }
                carrinho.append(item)
                # Atualiza o estoque temporariamente
                estoque[id_escolhido]["quantidade"] -= qtd
                print(f"✅ {qtd}x '{estoque[id_escolhido]['nome']}' adicionado ao carrinho!")
            else:
                print(f"❌ Estoque insuficiente! Temos apenas {estoque[id_escolhido]['quantidade']} unidades.")
        else:
            print("❌ Produto não encontrado.")
    except ValueError:
        print("❌ Por favor, digite apenas números inteiros para ID e Quantidade.")


def ver_carrinho():
    if not carrinho:
        print("\n🛒 Seu carrinho está vazio.")
        return 0

    print("\n--- SEU CARRINHO ---")
    subtotal = 0
    for item in carrinho:
        total_item = item["preco_unitario"] * item["quantidade"]
        subtotal += total_item
        print(f"• {item['quantidade']}x {item['nome']} (R$ {item['preco_unitario']:.2f} cada) = R$ {total_item:.2f}")

    print(f"\nSubtotal atual: R$ {subtotal:.2f}")
    return subtotal


def finalizar_compra():
    subtotal = ver_carrinho()
    if subtotal == 0:
        return

    # Regra de negócio real: Cupom de desconto
    cupom = input("\nPossui cupom de desconto? (Digite o cupom ou aperte ENTER para pular): ").upper()

    desconto = 0
    if cupom == "DESCONTO10":
        desconto = subtotal * 0.10
        print("🎉 Cupom DESCONTO10 aplicado! 10% de desconto garantido.")
    elif cupom == "DEV20" and subtotal > 500:
        desconto = subtotal * 0.20
        print("🎉 Cupom DEV20 aplicado! 20% de desconto garantido.")
    elif cupom != "":
        print("⚠️ Cupom inválido ou não atende aos requisitos. Prosseguindo sem desconto.")

    total_final = subtotal - desconto

    print("\n=================================")
    print("        RESUMO DA COMPRA         ")
    print("=================================")
    print(f"Subtotal:       R$ {subtotal:.2f}")
    print(f"Desconto:       R$ {desconto:.2f}")
    print(f"Total a Pagar:  R$ {total_final:.2f}")
    print("=================================")

    confirmar = input("Confirmar pagamento? (S/N): ").upper()
    if confirmar == 'S':
        print("\n✨ Compra realizada com sucesso! Obrigado por comprar conosco.")
        carrinho.clear()  # Limpa o carrinho para a próxima compra
    else:
        # Se cancelar, devolve os itens ao estoque
        print("\n🛒 Compra cancelada. Os itens voltaram para o estoque.")
        for item in carrinho:
            estoque[item["id"]]["quantidade"] += item["quantidade"]
        carrinho.clear()


# --- MENU PRINCIPAL (LOOP) ---
def menu():
    while True:
        print("\n=================================")
        print("    MERCADO LIVRE - TERMINAL     ")
        print("=================================")
        print("[1] Visualizar Estoque")
        print("[2] Adicionar Item ao Carrinho")
        print("[3] Visualizar Carrinho")
        print("[4] Finalizar Compra")
        print("[0] Sair do Sistema")
        print("=================================")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            exibir_estoque()
        elif opcao == "2":
            adicionar_ao_carrinho()
        elif opcao == "3":
            ver_carrinho()
        elif opcao == "4":
            finalizar_compra()
        elif opcao == "0":
            print("\nSistema encerrado. Até logo!")
            break
        else:
            print("❌ Opção inválida! Tente novamente.")


# Inicializa o programa
menu()