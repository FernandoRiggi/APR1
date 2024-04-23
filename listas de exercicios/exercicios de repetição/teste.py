x = 1
z = x
impar = x%2 != 0
while x <= 500:
    if x == impar and x%3 == 0:
        z = z + x
        print(f"{z}")
    x +=1