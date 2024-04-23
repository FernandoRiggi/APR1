#Escreva um programa que verifique se duas strings fornecidas pelousuário são iguais
#e mostre o total de caracteres de cada uma delas.
#Diferencie letras maiúsculas das minúsculas.
string1=input("Digite uma frase: ")
string2=input("Digite uma frase: ")
if string1==string2:
    print("As duas strings são iguais")
else:
    print("As strings não são iguais")
print(f"O total de caracteres da string 1 é = {len(string1)}")
print(f"O total de caracteres da string 2 é = {len(string2)}")