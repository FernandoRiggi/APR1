#Escreva um programa que remove todas as ocorrências de uma letra deuma string.
#A string e a letra devem ser fornecidas pelo usuário.
string=input("Digite uma frase: ")
letra_removida=input("Digite a letra que será removida: ")
str_sem_letra=""
for letra in string:
    if letra != letra_removida:
        str_sem_letra+=letra
print(str_sem_letra)