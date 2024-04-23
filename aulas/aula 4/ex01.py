#Gere uma lista de contendo os múltiplos de 3 entre 1 e 150.
Lista = []
x=1
while x<=150:
    if x%3 == 0:
        Lista.append(x)
    x+=1
print(Lista)