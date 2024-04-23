#Crie um programa que leia inicialmente uma sequência de N números inteiros 
#ao seu final mostre a sequência original,
#a soma de seuselementos que forem pares
#multiplicação dos elementos queforem ímpares.
Lista = []
valores = int(input("Escreva quantos números tem sua lista: "))
n = 0
x=0
while x<valores:
    n = int(input("Escolha um número: "))
    Lista.append(n)
    x+=1
print(Lista)
x=0
soma=0
while x<len(Lista):
    if Lista[x]%2 == 0:
        soma = soma+Lista[x]
    x+=1
print(f"A soma dos números pares é = {soma}")
mult = 1
x=0
while x<len(Lista):
    if Lista[x]%2 !=0:
        mult = mult*Lista[x]
    x+=1
print(f"A multiplicação dos números ímpares é = {mult}")