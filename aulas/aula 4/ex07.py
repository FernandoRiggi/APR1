#Crie um programa que leia inicialmente uma sequência de N númerosinteiros fornecidos pelo usuário
#e mostre ao final da leitura a sequênciaoriginal e a sequência invertida.
valor = int(input("Digite a quantidade de elementos de sua sequencia: "))
x= 0
lista = []
while x<valor:
    n=int(input("Escolha um número: "))
    lista.append(n)
    x+=1
invertida = []
x=valor-1
while x>=0:
    invertida.append(lista[x])
    x-=1
print(f"A lista original é = {lista}")
print(f"A lista invertida é = {invertida}")