#Faça um programa que leia três notas de provas de uma turma de 50 alunos (3
#notas para cada aluno). Para cada aluno, o programa deve calcular a média
#ponderada como segue: Média = (nota1*2 + nota2*4 + nota3*3 ) / 10. Além de
#mostrar a média de cada aluno, o programa deve mostrar uma mensagem
#"Aprovado", caso a média seja maior ou igual a 6,0, e uma mensagem
#"Reprovado", caso contrário. Ao final, o programa deve calcular e apresentar a
#média geral da turma. 
alunos = 0
somamédia = 0
while alunos < 50:
    nota1 = float(input("Digite sua nota 1: "))
    nota2 = float(input("Digite sua nota 2: "))
    nota3 = float(input("Digite sua nota 3: "))
    média = (nota1*2 + nota2*4 + nota3*3) / 10
    if média >= 6:
        print(f"A sua média foi {média} e você foi aprovado")
        alunos +=1
    elif média < 6:
        print(f"A sua média foi {média} e você foi reprovado")
        alunos +=1
    somamédia = somamédia + média
médiag = somamédia/alunos
print(f"A média geral da turma foi de {médiag:.1f}")