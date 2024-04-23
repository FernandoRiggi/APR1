#Faça um programa que permita ao usuário digitar o seu nome e 
#emseguida o mostre de trás para frente utilizando somente letrasmaiúsculas.
nome=input("Digite seu nome: ")
nomeinverso=""
i=len(nome)-1
while i>=0:
    nomeinverso+=nome[i]
    i-=1
print(f"O nome invertido e em maiúsculo é = {nomeinverso.upper()}")