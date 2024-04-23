#programa par ou impar
P = int(input("Escolha 0 ou 1: "))
D1 = int(input("Escolha um número de 0 a 5: "))
D2 = int(input("Escolha um número de 0 a 5: "))
if P == 0 and (D1+D2) % 2 == 0:
    print(0)
else:
    print(1)