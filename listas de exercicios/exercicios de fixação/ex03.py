c = int(input("Digite o número de competidores: "))
p = int(input("Digite o número de folhas especiais compradas: "))
f = int(input("Digite o número de folhas especiais que cada participante deve receber: "))
if p >= (c*f):
    print("S")
else:
    print("N")