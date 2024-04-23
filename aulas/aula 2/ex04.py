#faça um algoritmo que receba 3 valores e mostre se é um triangulo e se for indentificar o tipo
a = int(input("Escolha um número:"))
b = int(input("escolha um número:"))
c = int(input("escolha um número:"))
if a < (b+c) and b < (a+c) and c < (a+b) and a==b and a==c and b==c:
    print("é um triângulo equilátero")
elif a < (b+c) and b < (a+c) and c < (a+b) and a==b or a==c or b==c:
    print("é um triângulo isoceles") 
elif a < (b+c) and b < (a+c) and c < (a+b) and a!=b and a!=c and b!=c:
    print("é um triângulo escaleno")
else:
    print("não é um triângulo")