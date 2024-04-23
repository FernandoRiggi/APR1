#crie um programa que faça a tabuada dos números
x = float(input("insira um número : "))
cont = 1
while cont <= 10:
    print(f"{x} * {cont} = {x*cont}")
    cont+=1 # cont = cont +1