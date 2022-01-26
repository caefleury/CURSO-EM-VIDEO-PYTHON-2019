import random
vit = 0
while True:
    comp_num = random.randint(0, 10)

    choice = str(input('Escolha [PAR ou ÍMPAR]: ')).upper().strip()
    while choice not in 'IMPAR' and choice not in 'ÍMPAR':
        print('')
        print('=-' * 18)
        print('Resposta invalida.Escolha SOMENTE entre PAR e ÍMPAR')
        print('=-' * 18)
        print('')
        choice = input('Escolha [PAR ou ÍMPAR]: ').upper().strip()

    n = int(input('Escolha um número entre 0 e 10: '))
    soma = n + comp_num
    if 0 <= n <= 10:
        print(f"Você jogou {n} e o computador {comp_num}. Total de {soma}")

        if choice == 'PAR':
            if soma % 2 == 0:
                vit += 1
                print('A soma foi PAR, o jogador venceu!')
            else:
                print('A soma foi ÍMPAR, o jogador perdeu')
                print('----- GAME OVER -----')
                break
        elif choice == 'IMPAR' or choice == 'ÍMPAR':
            if soma % 2 != 0:
                vit += 1
                print('A soma foi ÍMPAR, o jogador venceu!')
            else:
                print('A soma foi PAR, o jogador perdeu')
                print('----- GAME OVER -----')
                break
        print("Vamos jogar novamente...")

    else:
        print('')
        print('=-' * 18)
        print('Número invalido.Tente novamente')
        print('=-' * 18)
        print('')

print(f"Você venceu {vit} vezes!!")