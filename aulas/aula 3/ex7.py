#faça um programa que mostre os 8 primeiros números de fibonacci
n1 = 0
n2 = 1
print(f"{n1}", end= " ")
print(f"{n2}", end= " ")
while n2 <= 8:
    fibonacci = n1 + n2
    n1 = n2 
    n2 = fibonacci
    print(f"{n2}", end= " ")