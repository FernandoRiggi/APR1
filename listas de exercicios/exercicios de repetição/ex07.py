#Faça um programa que calcule e apresente o mdc entre dois números. 
num1 = int(input("Escolha um número: "))
num2 = int(input("Escolha um número: "))
i = 2
mdc = 1
while i<=num1 and i<=num2:
    if num1%i == 0 and num2%i == 0:
        print(f"{num1}, {num2} / {i}")
        mdc = mdc * i
        num1 = num1/i
        num2 = num2/i
    i+=1
print(f"{num1}, {num2}")
print(f"A soma do MDC é = {mdc}")