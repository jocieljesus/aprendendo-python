notasAlunos = {
    "Jessica": [9.8, 8.7, 9.5],
    "Kennedy" : [8.9, 9.2, 9.9],
    "Jefferson": [8.5, 8.9, 9.7]
}

mediaAlunos ={}

for nome, notas in notasAlunos.items():
    media = round(sum(notas)/len(notas), 2)
    mediaAlunos[nome] = media

print(mediaAlunos)