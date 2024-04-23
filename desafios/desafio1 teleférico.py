#Criar um programa que mostre a quantidade mínima de viagens necessárias
C = int(input("Digite a capacidade máxima de pessoas na cabine: "))
A = int(input("Digite a quantidade de alunos da turma: "))
viagem = A / (C-1)
if A%(C-1) != 0 and C<A:
    viagem +=1
print(f"A quantidade mínima de viagens que deve ser feita é {viagem:.0f}")