from time import sleep
h = 0
while h == 0:
    print("\033[34mDigite um número para calcular seu fatorial: \033[m")
    n = input("\033[34mNúmero: \033[m")
    #if n != int(n):
        #print("Números inteiros apenas!")
    c = int(n)
    fac = 1
    if c < 0:
        print("\033[31mNúmeros positivos apenas!\033[m")
    else:
        print('\033[33mCalculando {}! = '.format(n), end='')
        while c > 0:
            print('{}'.format(c),end='')
            # if c > 1:
            # print(' x ')
            # else:
            # print(' x ')
            print(' x ' if c > 1 else ' = ',end='')
            fac *= c
            c -= 1
        print(fac)
        print("\033[33mO fatorial de {} é {}\033[m".format(n,fac))
        sleep(1)

