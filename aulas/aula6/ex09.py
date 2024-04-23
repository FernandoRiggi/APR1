#Um anagrama é uma palavra que é feita a partir da transposição dasletras de outra palavra ou frase.
#Por exemplo, “Iracema” é umanagrama para “America”. 
#Escreva um programa que decida se umastring é um anagrama de outra string, ignorando os espaços em branco.
#O programa deve considerar maiúsculas e minúsculas como sendocaracteres iguais, ou seja, “a” = “A”.
string1=input("Digite uma palavra: ")
string2=input("Digite outra palavra: ")
if len(string1)!=len(string2):
    print(f"{string1} não é um anagrama para {string2}")
    anagrama=False
string1 = string1.lower()
string2 = string2.lower()
string1_sorted = sorted(string1)
string2_sorted = sorted(string2)
if string1_sorted == string2_sorted:
    print(f"{string1} é um anagrama para {string2}")
else:
    print(f"{string1} não é um anagrama para {string2}")