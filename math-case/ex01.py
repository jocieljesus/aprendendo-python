dia = 1
while dia != 0:
    dia = int(input("Informe um numero, ou 0 para sair: "))

    match dia:
        case 1:
            print("Domingo")
        case 2:
            print("Segunda-Feira")
        case 3:
            print("Terça-Feira")
        case 4:
            print("Quarta-Feira")
        case 5:
            print("Quinta-Feira")
        case 6:
            print("Sexta-Feira")
        case 7:
            print("Sábado-Feira")
        case _:
            print("Digite um dia válido!")