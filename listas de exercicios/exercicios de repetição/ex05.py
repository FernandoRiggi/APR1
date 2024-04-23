#Escreva um programa que leia um número n (número de termos de uma
#progressão aritmética), a1 (o primeiro termo da progressão) e r (a razão daprogressão) 
#apresenta os n termos desta progressão, bem como a soma de todos elementos
n = int(input("Escolha a quantidade de termos da P.A.: "))
a1 = int(input("Escolha o primeiro termor da P.A.: "))
r = int(input("Escolha a razão da P.A.: "))
x = 0
soma = 0
print("Os termos da P.A. são:", end =" ")
while x < n:
    print(f"{a1}", end =" ")
    soma = soma +a1
    a1 = a1 +r
    x+=1
print( f"\nA soma dos termos da P.A. = {soma}")