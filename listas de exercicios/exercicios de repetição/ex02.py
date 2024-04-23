#Faça um programa que imprima os 20 primeiros números primos.
x = 2
print("2", end=" ")
while x < 72:
    i = 2
    primo = x%i != 0
    while i<x and primo == True:
        if x%i == 0:
            primo = False
        i+=1
    if primo == True:
        print(f"{x}", end=" ")
    x+=1