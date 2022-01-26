from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
option = 0
print("----- INICIANDO PROGRAMA -----")
sleep(1)


while option != 5:
    print("""[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior termo 
[ 4 ] novos números
[ 5 ] finalizar programa""")
    option = int(input(">>>>> Qual a sua opção?"))
    if option == 1:
        soma = n1 + n2
        print('  {} + {} = {}'.format(n1,n2,soma))
        print('=-=' * 8)
        sleep(1)
    elif option == 2:
        produto = n1 * n2
        print('  {} x {} = {}'.format(n1, n2, produto))
        print('=-=' * 8)
        sleep(1)
    elif option == 3:
        if n1 > n2:
            print("Entre {} e {} o maior valor é {}".format(n1,n2,n1))
            print('=-=' * 8)
            sleep(1)
        elif n1 < n2:
            print("Entre {} e {} o maior valor é {}".format(n1,n2,n2))
            print('=-=' * 8)
            sleep(1)
        else:
            print("Os termos são iguais")
            print('=-=' * 8)
            sleep(1)
    elif option == 4:
        print("Informe os números novamente:")
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
        print('=-=' * 8)
        sleep(1)
    else:
        print('Opção inválida, tente novamente:')
        print('=-=' * 8)
        sleep(1)
if option == 5:
    print("----- FINALIZANDO PROGRAMA -----")
    sleep(1)
    print("----- PROGRAMA FINALIZADO -----")
