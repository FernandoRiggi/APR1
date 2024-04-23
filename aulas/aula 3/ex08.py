#Faça um programa que leia um número inteiro >= 0 e calcule o seu fatorial.
n1 = int(input("Escolha um número inteiro >=0: "))
n2 = n1-1
fatorial = n1
if n1>=0:
    if n1 ==0:
        print("Fatorial de zero é igual a 1")
    else:
        while n2 > 1:
            fatorial = fatorial*n2
            n2 -=1
        print(f"O fatorial de {n1} é = {fatorial}")
else:
    print("O valor deve ser positivo")