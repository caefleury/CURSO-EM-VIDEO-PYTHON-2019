from time import sleep
print("        ----- TABUADA -----")
while True:
    print("Digite um valor negativo para finalizar")
    n = int(input('Quer ver a tabuada de qual valor? '))
    print("=-" * 19)

    if n > 0:
        for c in range(1, 11):
            print(f'{n} x {c:2} = {n*c}')
        print("=-" * 19)

    else:
        print("      FINALIZANDO PROGRAMA")
        sleep(2)
        print("----- PROGRAMA FINALIZADO -----")
        break
