valor = float(input("Informe o valor do saque: R$ "))
cedulas = [50, 20, 10, 5, 2]
notas = 0
while valor > 0:

    for n in cedulas:

        notas = valor // n
        
        if n == 5 and (valor == 6  or valor == 8 ):
            continue
        if notas > 0:
            print(f"{notas} cédula(s) de R$ {n}")
            valor %= n

    if valor != 0:
        print(f"Não foi possível sacar o valor restante de R$ {valor}")
        break
        