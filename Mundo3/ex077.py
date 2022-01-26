word = ('aprender', 'programar', 'linguagem', ' python', 'curso' , 'gratis' )

for palavra in word:
    print(f'\nNa palavra {palavra.upper()} temos as vogais: ',end='')
    for letra in palavra:
        if letra.lower() in 'aáãâéêeiíoôóu':
            print(f'{letra} ',end='')
