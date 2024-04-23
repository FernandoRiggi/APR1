#Dado o valor da distância D, você deve escrever um programa para calcular o número de pontos do lançamento
d = float(input("insira o distância da pontuação: "))
if d<=800:
    print("O valor da cesta é de 1 ponto")
elif d>800 and d<=1400:
    print("o valor da cesta é de 2 ponto")
else:
    print("o valor da cesta de 3 pontos")
