notasAlunos = [
                ["João", 8.7, 9.0],
                ["Maria", 7.3, 9.0],
                ["José", 8.3, 5.2]
              ]
mediaAlunos = []
for i in notasAlunos:
    media = (i[1]+i[2])/2
    lista = [i[0],media]
    mediaAlunos.append(lista)

print(f"Lista de Notas de alunos: {notasAlunos}")
print(f"Lista de Médias de alunos: {mediaAlunos}")


