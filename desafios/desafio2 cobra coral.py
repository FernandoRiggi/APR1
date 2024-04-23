#crie um programa que msotre uma sequencia de números e indentifique se for v ou f
valor = 4
i=0
lista = []
while i < 4:
    num = int(input("Escolha um número de 1 até 9: "))
    if num>=1 and num<=9:
        lista.append(num)
    elif num<1 and num>9:
        print("O número não corresponde na lista")
    i+=1
i=0
soma = 0
while i<len(lista):
    soma = soma + lista[i]
    i+=1
if not soma%2 ==0:
    print("F")
else:
    print("V")