while True:
    print("*******************")
    print("1 - Somar")
    print("2 -Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Sair")
    print("*******************")
    opcao = int(input("Qual operação você deseja fazer: "))
    print("*******************")
    match opcao:
        case 1:
            print("Somando valores")
        case 2:
            print("Subtraindo valores")
        case 3:
            print("Multiplicando valores")
        case 4:
            print("Dividindo valores")
        case 5:
            print("Saindo...")
            break








