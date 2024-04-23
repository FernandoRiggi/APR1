#Crie um programa que leia inicialmente uma sequencia de N númerosinteiros.
#Depois, o programa deve gerar e mostrar 2 novas listas apartir da primeira: uma sem repetição de elementos e 
#outra com oselementos que se repetem na lista original.
Lista = []
valores = int(input("Escreva quantos elementos tem sua lista: "))
x=0
while x<valores:
    n = int(input("Escolha um número: "))
    Lista.append(n)
    x+=1
print(f"A lista original é: {Lista}")
noreps = []
x=0
while x<len(Lista):
    if Lista[x] not in noreps :
        noreps.append(Lista[x])
    x+=1
print(f"A lista sem repetição de elementos: {noreps}")
reps = []
y=0
while y<len(Lista):
    x=0
    while x<len(Lista):
        if Lista[x]==Lista[y] and x!=y:
            reps.append(Lista[y])
            break
        x+=1
    y+=1
print(f"A lista com apenas os elementos que se repetem é: {reps}")