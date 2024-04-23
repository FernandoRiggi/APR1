#Faça um programa que recebe uma frase e retorna o número de palavrasque a frase contém.
string=input("Digite uma frase: ")
palavras = string.split()
print(f"{len(palavras)}")