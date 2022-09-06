n1 = int(input('Informe o primeiro número '))
n2 = int(input('Informe o segundo número '))
n3 = int(input('Informe o terceiro número '))

maior = n1

if n2 > maior:
    maior = n2
if n3 > maior:
    maior = n3

print (f'Maior:{maior}')