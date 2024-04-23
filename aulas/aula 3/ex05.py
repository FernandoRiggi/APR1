x = int(input("escolha a base: "))
y = int(input("escolha o expoente: "))
i = 0
z = 1
while i < y:
    z = z * x
    i +=1
print(f"{x}^{y} = {z}")