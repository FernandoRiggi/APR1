#faça um programa para mostrar as tabuadas de todos os números de 1 até 10
x = 1 
while x <= 10:
        cont = 1
        while cont <= 10:
               print(f"{x} x {cont} = {x*cont}")
               cont +=1 
        x+=1