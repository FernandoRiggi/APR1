#faça um programa que mostre se um número inteiro>1 é primo ou não
x = int(input("Escolha um número inteiro maior que 1: "))
if x > 1:
    primo = True
    i = 2
    while i<x and primo == True:
        if x%i == 0:
            primo = False
        i += 1
    if primo == True:
        print(f"{x} é primo!")
    else:
        print(f"{x} não é primo!")