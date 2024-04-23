#Faça um programa que crie uma lista com 10 números inteirosfornecidos pelo usuário.
#Após criar a lista, o programa deverá imprimir:
#O maior elemento da lista
#O menor elemento da lista
#A soma de todos os elementos da lista
#Os elementos ímpares
#Os elementos maiores do que 18
numeros = []
x=1
while x <=10:
    n=int(input("Escolha um número inteiro: "))
    numeros.append(n)
    x+=1     
print(numeros)
posição=0
maior=numeros[0]
while posição<len(numeros):
    if maior< numeros[posição]:
        maior = numeros[posição]
    posição+=1 
print(f"Maior elemento da lista é = {maior}")
i = 0
menor=numeros[0]
while i<len(numeros):
    if menor > numeros[i]:
        menor = numeros[i]
    i+=1
print(f"Menor número da lista é = {menor}")
soma = 0
i=0
while i<len(numeros):
    soma = soma+numeros[i]
    i+=1
print(f"A soma dos números da lista é = {soma}")
i=0
print("Os números ímpares são:", end=" ")
while i<len(numeros):
    if numeros[i]%2 !=0:
         print(f"{numeros[i]}", end= " ")
    i+=1
i=0
print("\nOs números maiores que 18 são:", end=" ")
while i<len(numeros):
    if numeros[i]>18:
        print(f"{numeros[i]}", end=" ")
    i+=1