#Escreva um programa que remove a primeira ocorrência de uma letra deuma string.
#A string e a letra devem ser fornecidas pelo usuário.
string = input("Digite uma frase: ")
letra = input("Escolha a letra a ser removida: ")
str_sem_letra=""
letra_removida=False
for i in string:
    if i==letra and not letra_removida:
        letra_removida=True
    else:
        str_sem_letra+=i
print(str_sem_letra)