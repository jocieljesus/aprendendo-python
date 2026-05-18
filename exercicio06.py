## Atividade de Desconto blackfriday

valorTotalCompras = float(input("Digite o total das compras: "))

if valorTotalCompras <= 100:
    print(f"Você não teve desconto. O valor total da sua compra é de {valorTotalCompras}")
elif valorTotalCompras > 100 and valorTotalCompras <= 300:
    valorDesconto = valorTotalCompras * 0.05
    valorComDesconto = valorTotalCompras - valorDesconto
    print(f"Voce teve o desconto de 5% no valor de {valorDesconto}. Sua compra ficou um total de: {valorComDesconto}")

elif valorTotalCompras > 300 and valorTotalCompras < 500:
    print(f"Voce teve o desconto de 10% no valor de {valorTotalCompras*0.1}. Sua compra ficou um total de: {valorTotalCompras*0.9}")

else :

    print(
        f"Voce teve o desconto de 15% no valor de {valorTotalCompras * 0.15}. Sua compra ficou um total de: {valorTotalCompras * 0.85}")

