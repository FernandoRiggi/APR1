#faça um programa que mostre todos os números divisíveis por 7 e 3 de 1 até 100
x = 1
while x <= 100:
    if x % 7 == 0 and x % 3 == 0:
        print(f"{x} é divisível por 3 e 7")
    x +=1