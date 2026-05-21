peso = float(input("Informe seu peso: "))
altura = float(input("Informe sua alura: "))
imc  =  peso/(altura**2)

if  imc < 18.5:
    print(f"Abaixo do peso{imc}")
elif imc >= 18.5 and imc <= 24.9:
    print(f"Peso {imc} normal")
elif imc >= 25 and imc <=29.9:
    print(f"Peso {imc} normal")
else:
    print(f"Obesidade {imc}")

