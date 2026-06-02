"""Crie uma estrutura onde cada elemento da lista principal seja uma sublista contendo o nome de um aluno e suas duas notas.

Exemplo de estrutura: turma = [ ["Ana", 8.0, 9.0], ["Pedro", 5.5, 6.0], ["Carlos", 7.5, 7.0] ]
O programa deve percorrer essa lista composta, calcular a média de cada aluno e imprimir no terminal no formato: "Aluno(a) [Nome] obteve média [Valor da Média]".
"""
quantidade = int(input("Digite quantos alunos tem na sala: "))
turma  = []

for i in range(quantidade):
    nome, nota1, nota2 = input("""
    Iniciando o cadastro das notas: 
    Digite o nome de um aluno(a) e as suas duas ultimas notas separando por vírgula:
    """).split(",")
    alunNota = [nome, float(nota1), float(nota2)]
    turma.append(alunNota)

print(f"Primeira Lista {turma}")
alunoMedia = []

for aluno  in turma:
    media = (aluno[1] + aluno[2])/2
    aluno = [aluno[0],media]
    alunoMedia.append(aluno)

print(f"Segunda Lista {alunoMedia}")
