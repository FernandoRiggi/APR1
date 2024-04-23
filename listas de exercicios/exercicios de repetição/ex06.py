#Faça um programa que calcule e apresente o mmc entre dois números.
num1 = int(input("Escolha um número inteiro: "))
num2 = int(input("Escolha um número inteiro: "))
i = 2
mmc = 1
while i<=num1 or i<=num2:
     if num1%i == 0 and num2%i == 0:
        print(f"{num1}, {num2} /{i}")
        mmc = mmc * i
        num1 = num1//i
        num2 = num2//i
     elif num1%i == 0:
          print(f"{num1}, {num2} /{i}")
          mmc = mmc*i
          num1 = num1/i
     elif num2%i == 0:
          print(f"{num1}, {num2} /{i}")
          mmc = mmc*i
          num2 = num2/i 
     else:
           i+=1    
print(f"{num1}, {num2}")
print(f"A soma do MMC é = {mmc}")