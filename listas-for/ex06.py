emails = ["joao@gmail.com", "maria@senac.df", "pedro@outlook.com", "ana@senac.df"]

emailsSenac = []

for i in emails :
    if(i.endswith("senac.df")):
        emailsSenac.append(i)

print(*emailsSenac)