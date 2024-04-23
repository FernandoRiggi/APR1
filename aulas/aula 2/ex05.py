#crie um algoritmo para resolver equações de segundo grau
a = float(input("Escolha um núemro diferente de zero:"))
b = float(input("Escolha um número:"))
c = float(input("Escolha um número:"))
delta = b**2 - 4*a*c 
x = (-b)/(2*a)
x1 = (-b + delta**0.5)/(2*a)
x2 = (-b - delta**0.5)/(2*a)
equação = a*x**2 + b*x + c 
if delta < 0:
    print("não existe raiz real")
elif delta == 0:
    print(f"existe uma raiz real x1={x1}")
else:
    print(f"existe duas raizes reais x1={x1} e x2={x2}")