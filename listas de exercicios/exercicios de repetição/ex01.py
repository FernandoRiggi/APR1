#Elabore um programa que efetue a soma de todos os números ímpares que são
#múltiplos de 3 e que se encontram no intervalo de 1 a 500
x = 3
z = 0
while x <= 500:
    impar = x%2 != 0
    if x%3 == 0 and impar == True:
        z = z + x
    x +=1
print(f"A soma de todos os números ímpares e múltiplos de 3 no intervalo de 1 até 500 é = {z}")