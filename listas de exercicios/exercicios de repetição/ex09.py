#Escreva um programa que apresente os 5 primeiros números perfeitos. Um
#número perfeito é aquele que é igual a soma dos seus divisores (por exemplo, 6 =
#1+2+3 e 28= 1+2+4+7+14).
num=2
i=1
soma = 0
while i <= num:
    if num%i == 0:
        soma = 0 + i
        i+=1
        num+=1
    elif num%i !=0:
        num+=1
    print(f"{soma}")