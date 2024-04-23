#Crie um programa que leia inicialmente duas sequências de N elementos cada uma e 
#ao final mostre as duas sequências originais e a sequência resultante da soma de seus elementos. 
valores = int(input("Digite quantos elementos tem a sua sequencia: "))
ListaA = []
ListaB = []
x=0
while x<valores:
    n = int(input("Escolha um número para a lista a: "))
    ListaA.append(n)
    x+=1
x=0
while x<valores:
    n=int(input("Escolha um número para a lista b:"))
    ListaB.append(n)
    x+=1
x=0
somaL=[]
while x<valores:
    soma= ListaA[x] + ListaB[x]
    somaL.append(soma)
    x+=1
print(f"a = {ListaA}")
print(f"b = {ListaB}")
print(f"soma = {somaL}")