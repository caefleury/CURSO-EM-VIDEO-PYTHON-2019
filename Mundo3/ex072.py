n = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
     'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input("Número entre 0 - 20: "))

    if 0 <= num <= 20:
        find = n[num]
        print(f'Você digitou o número {find}')
        break
        
    print("Número inválido. Tente novamente:")

