#faça um programa que receba 5 números e informe o maior entre eles
n1 = int(input("Escolha um número:"))
n2 = int(input("Escolha outro número:"))
n3 = int(input("Escolha outro número:"))
n4 = int(input("Escolha outro número:"))
n5 = int(input("Escolha outro número:"))
if n1>n2 and n1>n3 and n1>n4 and n1>n5:
    print(f"{n1} é o maior")
elif n2>n1 and n2>n3 and n2>n4 and n2>n5:
    print(f"{n2} é o maior")
elif n3>n1 and n3>n2 and n3>n4 and n3>n5:
    print(f"{n3} é o maior")
elif n4>n1 and n4>n2 and n4>n3 and n4>n5:
    print(f"{n4} é o maior")
else:
    print(f"{n5} é o maior")