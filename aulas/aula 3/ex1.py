#faça um programa que mostre todos os números divisíveis por 7 de 1 até 100
x = 1
while x <= 100:
    if x % 7 == 0:
        print(f"{x} é divisível por 7")
    x +=1