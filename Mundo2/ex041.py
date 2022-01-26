from datetime import date
print("\033[36m---CLASSIFICAÇÃO DE ATLETAS---\033[m")

ano_nasc = int(input("Ano de Nascimento do Atleta: "))
atual = date.today().year
idade = atual - ano_nasc

if idade <= 9:
    c = 'MIRIM'
elif 9 < idade <= 14:
    c = 'INFANTIL'
elif 14 < idade <= 19:
    c = 'JUNIOR'
elif 19 < idade <= 20:
    c = 'SÊNIOR'
else:
    c = 'MASTER'

print("O atleta tem {} anos".format(idade))
print('Classificação:',c)


