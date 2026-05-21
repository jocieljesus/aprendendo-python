# Atividade de média

frequencia = int(input("Informe quantos dias o aluno compareceu as aulas: "))

if frequencia > 0 :
    nota1 = float(input("Digite a primeira nota: ").replace("," , "."))
    nota2 = float(input("Digite a segunda nota: ").replace("," , "."))
    
    media = (nota1 + nota2) / 2

    if media >= 7 :
        print("APROVADO")
    elif media>=5: 
        print("RECUPERAÇÃO")
    else :
        print("REPROVADO")
else: 
    print("Aluno não foi as aulas")
