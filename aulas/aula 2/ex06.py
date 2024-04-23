#Faça um programa que leia o quanto o cliente gastou e escreva o valor da conta já com os descontos.
valor = int(input("Digite o valor bruto da compra:"))
desconto1 = valor*5/100
desconto2 = valor*10/100
desconto3 = valor*20/100
if valor <= 100:
    print(f"você ganhou 5% de desconto, o valor da conta será de R${valor-desconto1:.2f}")
elif valor > 100 and valor < 200:
    print(f"você ganhpu 10% de desconto, o valor da conta será de R${valor-desconto2:.2f}")
else:
    print(f"você ganhou 20% de desconto, o valor da conta será de R${valor-desconto3:.2f}")   