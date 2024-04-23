#Escreva um programa que leia um número não determinado de valores inteiros,
#calcula e apresenta: a média aritmética dos valores lidos, a quantidade de valores
#positivos, a quantidade de valores negativos e o percentual de valores negativos e
#positivos. Obs: o programa deverá encerrar a leitura dos números, somente
#quando o usuário desejar. 
negativos = 0
positivos = 0
soma = 0
contador = 0
while True:
    valores = int(input("Escolha um número, se quiser sair digite 0: "))
    if valores > 0:
        positivos +=1
        soma = soma + valores
        contador +=1
    elif valores < 0:
        negativos +=1
        soma = soma + valores
        contador +=1
    elif valores == 0:
        break
saída = valores
média = soma/contador
positivos_p100 = (positivos/contador)*100
negativos_p100 = (negativos/contador)*100
print(f"A média dos valores é = {média:.2f}")
print(f"A quantidade de valores positivos é = {positivos}")
print(f"A quantidade de valores negativos é = {negativos}")
print(f"O percentual de positivos é = {positivos_p100}%")
print(f"O percentual de negativos é = {negativos_p100}%")