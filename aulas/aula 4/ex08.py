#Crie um programa que leia inicialmente uma sequência de N elementosinteiros positivos fornecidos pelo usuário 
#e substitua seus elementos devalor ímpar por -1 e os pares por +1. 
#o final imprima a sequênciaoriginal e a sequência alterada
valores = int(input("Digite a quantidade de elementos da sua sequência: "))
lista = []
x=0
while x<valores:
    n = int(input("Escolha um numero inteiro positivo: "))
    if n>0:
        lista.append(n)
        x+=1
    else:
        print("O número não é positivo")
x=0
alternada=[]
while x<valores:
    if lista[x]%2 == 0:
        alternada.append(+1)
        x+=1
    else:
        alternada.append(-1)
        x+=1
print(f"A lista original é = {lista}")
print(f"A sequência alternada é = {alternada}")