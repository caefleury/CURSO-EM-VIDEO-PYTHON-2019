n = int(input('Digite um número [999 para parar]: '))
cont = soma = 0
while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite um número[999 para parar]: '))
print("Você digitou {} números e a soma deles foi {}".format(cont,soma))

