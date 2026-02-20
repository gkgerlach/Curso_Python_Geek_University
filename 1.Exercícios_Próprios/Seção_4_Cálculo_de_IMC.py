peso: float = float(input("Qual o seu peso: "))
altura: float = float(input("Qual a sua altura: "))
imc: float = round(peso / (altura**2), 2)

if imc < 18.5:
    print(f"Seu é IMC é {imc} e você está 'Abaixo do Peso'")
elif imc < 25:
    print(f"Seu é IMC é {imc} e você está 'No peso Ideal'")
elif imc < 30:
    print(f"Seu é IMC é {imc} e você está 'Acima do Peso'")
else:
    print(f"Seu é IMC é {imc} e você está 'Com Obesidade'")
