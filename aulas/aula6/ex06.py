#Faça um programa que solicite o nome do usuário e imprima-o navertical e em formato de escada
nome=input("Digite seu nome: ")
formatos=""
for letra in nome:
    formatos+=letra
    print(formatos)