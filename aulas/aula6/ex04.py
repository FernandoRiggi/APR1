#Escreva um programa que reconhece se uma string é um palíndromo.Exemplo: arara, ovo, reter.
string=input("Digite uma palavra: ")
count=0
start=0
end=len(string)-1
palíndromo=True
while start<end and palíndromo==True:
    if string[start]!=string[end]:
        print(f"A palavra {string} não é um palíndromo")
        palíndromo=False
    start+=1
    end-=1
if palíndromo==True:
    print(f"A palavra {string} é um palíndromo")