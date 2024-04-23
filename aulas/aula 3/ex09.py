#Faça um programa que receba um número N fornecido pelou suário e mostre os N termos da série a seguir.
#Depois, imprima a soma total da série.
n = int(input("Escolha um número: "))
m = n*2 - 1
expoente = 1
base = 1
numeros = 0
print("1/1", end=' ')
while expoente < n:
    print("+", end= ' ')
    nm = expoente/base
    expoente +=1
    base +=2
    numeros = numeros + nm
    print(f"{expoente}/{base}", end=' ')
soma = numeros + n/m
print(f"\nA soma total da série é = {soma:.2f}")