#Escreva um programa que solicite ao usuário a entrada de um númerointeiro 
#positivo ou negativo e mostre a quantidade de dígitos dessenúmero.
string=input("Digite um número: ")
i=-1
j=0
k=0
dez=1
dig=0
num="0123456789"
while j < len(string):
    if string[i] == num[k]:
        dig+=1
        k=0
        i+=1
        j+=1
    k+=1
print(f"A quantidade de dígitos desse número é = {dig}")        