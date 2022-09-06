from math import sqrt


n1 = int(input("Informe o primeiro número:"))
n2 = int(input("Informe o segundo número: "))
n3 = int(input("Informe o terceiro número: "))

if  n1 >= 0:
    raiz = sqrt(n1)
    print(f"A raiz quadrada de {n1} é {raiz}")

else:
    n1q = n1 * n1
    print(f"O seu quadrado é {n1q}")
    
if n2 >10 <100:
    print('NÚMERO ESTÁ ENTRE 10 E 100 - INTERVALO PERMITIDO')

if n3 < n2:
    print(f'A diferença entre {n3} e {n2} é de {n3 - n2}')

else:
    print(f"A soma entre {n2} e {n3} é de {n2 + n3}")