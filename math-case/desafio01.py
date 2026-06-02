while True:

    letra = input("Digite uma letra ou 0 para sair:")

    match letra.lower():
        case "0":
            break
        case "a"|"e"|"i"|"o"|"u":
            print("VOGAL")
        case _:
            print("CONSOANTE")