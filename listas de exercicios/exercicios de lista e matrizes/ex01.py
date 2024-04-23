#Em geometria analítica, dois vetores podem ser definidos como a=<a1,a2,a3> e
#b=<b1,b2,b3>. Escreva um programa que leia dois vetores a e b (duas listas) de
#três posições cada e efetue o produto escalar entre eles. O produto escalar é obtido
#por axb = a1b1+a2b2+a3b3. De acordo com o exemplo dado abaixo, o calculo a ser
#efetuado será: 1x5+4x2+7x3
A = [] #vetor a
B= [] #vetor b
i = 0 
posições = int(input("Escolha quantas posições terão os vetores: "))
for i in range(posições):
    valora = int(input(f"Escolha o valor de a{i}: "))
    A.append(valora)
for i in range(posições):
    valorb = int(input(f"Escolha o valor de b{i}: "))
    B.append(valorb)
soma = 0
for i in range(posições):
    soma = soma + A[i]*B[i]
print(f"A soma dos vetores é = {soma}") 