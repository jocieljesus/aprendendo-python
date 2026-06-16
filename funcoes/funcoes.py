def PI():
    return 3.14

def somar( n1, n2):
    soma = n1 + n2
    return soma

def subtrair(n1, n2):
    return  n1 - n2

estoque = {"Teclado": 15, "Mouse": 22, "Monitor": 8}

mercado = {"Farinha" : 9.90, "Arroz" : 7.50, "Macarrao": 3.50, "Frango" : 18.00}

ferramentas = {"Alicate" : 15.00, "Martelo" : 12.00, "Furadeira": 150, "Serrote" : 35.00}


def imprimir_dic(dic, descricao):
    print(f"Imprimindo coisas de {descricao}:")
    for k, v in dic.items():
        print(f"{k}:{v}")

imprimir_dic(estoque, "Informática")
print()

imprimir_dic(mercado, "Mercado")
print()

imprimir_dic(ferramentas, "Ferramentas")






