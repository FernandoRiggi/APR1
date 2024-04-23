#faça um progama que receba a idade e informe o tipo de voto
idade = int(input("Digite sua idade:"))
if idade < 16:
    print("Você ainda não pode votar!")
elif idade >= 16 and idade <= 17:
    print("Você possui voto facultativo!")
elif idade >= 18 and idade <= 65:
    print("Você é obrigado a votar!")
else:
    print("Você está dispensado de votar!")