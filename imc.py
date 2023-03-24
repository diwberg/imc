altura = float(input("Digite a sua altura em metros: "))
peso = float(input("Digite o seu peso em quilogramas: "))
imc = peso / altura ** 2
print("Seu IMC é:", round(imc, 2))
