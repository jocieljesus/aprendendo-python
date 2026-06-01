from unittest import result

while True:
    print("Operações")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Sair")

    opcao = int(input("Escolha uma opção: "))
    if opcao == 5:
        print("Saindo...")
        break
    num1 = float(input("Digite o primeiro numero :"))
    num2 = float(input("Digite o Segundo numero :"))

    result = 0
    if opcao == 1:
        result = num1 + num2
    elif opcao == 2:
        result = num1 - num2
    elif opcao == 3:
        result = num1 * num2
    elif opcao == 4:
        result = num1 / num2
    else:
        print("Opção Inválida")
    print("O resultado é: ", result)
