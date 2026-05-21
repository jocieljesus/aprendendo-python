import math
temperatura="frio"
print(temperatura)
sala = ["monitor", "cadeira", 9, True, 18.5, "TV"]
print(sala[1].upper()) #Transforma tudo em maiúscula
print(sala[-1].lower()) # Minuscula
sala.pop() #Remove o último
sala.remove("cadeira")
"""
if temperatura == "FRIO" :
    sala.append("AR")
    sala.append("Casaco")
else:
    sala.append("Caipirinha")
    sala.append(29.90)
"""

print(sala)

notas = [4.5, 2.8, 7.3, 8.5, 9.0]
media = sum(notas)/len(notas) # Sum, soma tudo, e len conta tudo.
print(f"A media é = {media}")
print(math.pow(2, 0)) # Potencia