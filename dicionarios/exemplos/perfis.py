perfil_pessoal = {
    "nome" :  "Jociel",
    "idade" : 29,
    "hobbie" : "Voleibol"
}

perfil_profissional = {
    "nome":  "Jociel Jesus",
    "profissao1" : "analista de sistemas",
    "profissao2" :  "professor de ti",
    "formacao" : "BSI"
}

perfil_completo = perfil_pessoal | perfil_profissional

perfil_completo2 = {**perfil_pessoal, **perfil_profissional}

perfil_pessoal |= perfil_profissional

perfil_profissional.update(perfil_pessoal)

print(perfil_completo)
print(perfil_completo2)
print(perfil_pessoal)
print(perfil_pessoal)