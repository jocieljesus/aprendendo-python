escolha = "s"
while escolha == "s":

    numeroDecimal = int(input("Digite um numero decimal: "))
    binario = ""

    while numeroDecimal > 0:
       binario =str(numeroDecimal%2) + binario
       numeroDecimal //=2


    print("Resultado Binario: ", binario)
    escolha = input("Quer continuar? ")
