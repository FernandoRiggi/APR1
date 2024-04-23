#Faça um programa que simule um jogo da loto. O computador deve gerar 5
#números aleatoriamente entre 50 possíveis (0 a 49), armazenando as dezenas
#sorteadas em um vetor (dez_sort) de 5 posições. Em seguida, o usuário deverá ler
#uma lista com 10 posições, representando a aposta (conforme o exemplo abaixo).
#O programa deve, então, verificar e imprimir uma mensagem mostrando quantos
#números o usuário acertou.
import random
dez_sort = []
i = 0
while i <5:
    num = random.randint(0, 49)
    dez_sort.append(num)
    i+=1
n_escolhidos = []
valor = 9
acertos = 0
n_acertados = []
for i in range(valor):
    aposta = int(input("Escolha um número para a sua aposta: "))
    n_escolhidos.append(aposta)
print(f"Os números sorteados foram {dez_sort}")
for i in range(valor):
    for j in range(len(dez_sort)):
        if n_escolhidos[i] == dez_sort[j]:
           acertos +=1
           print(f"Acertou o número {n_escolhidos[i]}")
           n_acertados.append(n_escolhidos[i])
print(f"A quantidade de acertos é = {acertos}") 