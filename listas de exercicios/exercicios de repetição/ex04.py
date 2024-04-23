import random
num = random.randint(0, 100)
x = int(input("Escolha um número de 0 até 100: "))
cont = 0
while x != num:
    if x > num:
        print("Número incorreto, tente um valor menor")
        x = int(input("Escolha um valor menor: "))
        cont +=1
    elif x < num:
        print("Número incorreto, tente um valor maior")
        x =int(input("Escolha um valor maior: "))
        cont +=1
else:
    print(f"Parabéns, você acertou o número escolhido que era {num} em {cont} tentativas")