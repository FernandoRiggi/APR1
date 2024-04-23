#Crie um programa que dada uma sequência de N elementos fornecidos pelo usuário
# mostre a sequência original e a sequência elevada ao cubo
valores = int(input("Digite a quantidade de elementos da sua sequência: "))
x = 0
lista = []
while x<valores:
    n= int(input("Escolha um número: "))
    lista.append(n)
    x+=1
listacubo = []
x=0
while x<valores:
    cubo = lista[x]**3
    listacubo.append(cubo)
    x+=1
print(f"Lista original = {lista}")
print(f"Lista ao cubo = {listacubo}")