#uma frase informada pelo usuário (incluindoespaços em branco),
#conte a quantidade de espaços em branco e aquantidade de vezes que aparecem as vogais a, e, i, o, u.
string=input("Digite uma frase: ")
vogais="aeiouAEIOU"
contadorvogais=0
for letra in string:
    if letra in vogais:
        contadorvogais+=1
print(f"O número de vogais que aparecem é = {contadorvogais}")
contspace=string.count(" ")
print(f"O número de espaçoes em branco que aparecem é = {contspace}")