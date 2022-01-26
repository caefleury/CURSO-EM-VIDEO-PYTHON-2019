frase = input("Digite uma frase: ").upper().strip().replace(' ','')
inverso = frase[::-1]
print("O inverso de {} é {}".format(frase,inverso))

if frase == frase[::-1]:
    print("Temos um políndromo!!!")
else:
    print('Frase não é um políndromo')
