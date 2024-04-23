#Crie um programa que leia inicialmente uma sequência de N notas de alunos fornecidas pelo usuário
#final mostre a sequência e sua média aritmética.
#Defina um critério de parada para a entrada denotas pelo usuário
notas=[]
nota = 0
print("Quando acabar as notas digite um número negativo")
while nota>=0:
    nota = float(input("Digite a nota do aluno: "))
    if nota>=0 and nota<11:
        notas.append(nota)
    elif nota>10:
        print("Escolha um número menor que 10")
soma = 0
x=0
while x<len(notas):
    soma = (soma + notas[x])
    x+=1
média = soma/(len(notas))
print(f"A média dos alunos é = {média:.2f}")