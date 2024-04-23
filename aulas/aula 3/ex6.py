notas = float(input("Digite sua nota: "))
contador = 0
contador2 = 0
contador3 = 0
contadorg = 0
media = 0
while notas>=0 and notas<=10: 
    if notas >= 6:
        contador +=1
    elif notas >=4 and notas < 6:
        contador2 +=1
    else:
        contador3 +=1
    media = media + notas
    contadorg +=1
    notas = float(input("Digite sua nota: "))
mediag = media/contadorg 
print(f"o número de notas maiores ou iguais que 6 são: {contador}")
print(f"o número de notas maiores ou iguais a 4 e menores que 6 são: {contador2}")
print(f"o número de notas menores que 4 são: {contador3}")
print(f"a média das notas é {mediag:.2f}")