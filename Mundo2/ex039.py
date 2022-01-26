from datetime import date
ano_de_nasc = int(input('Ano de nascimento: '))
print("Informe o seu sexo:")
sexo = input('Masculino ou Feminino: ').upper()
ano_atual = date.today().year
idade_atual = ano_atual - ano_de_nasc

if idade_atual < 18 and 'MASCULINO' in sexo:
    print('Quem nasceu em {} tem {} anos em 2018'.format(ano_de_nasc, idade_atual))
    faltam = 18 - idade_atual
    em = ano_atual + faltam
    print("Ainda faltam {} anos para o alistamento".format(faltam))
    print("Seu alistamento será em {}".format(em))

elif idade_atual > 18 and 'MASCULINO' in sexo:
    print('Quem nasceu em {} tem {} anos em 2018'.format(ano_de_nasc, idade_atual))
    ha = idade_atual - 18
    em = ano_atual - ha
    print("Você ja deveria ter se alistado há {} anos".format(ha))
    print("Seu alistamento foi em {}".format(em))

elif idade_atual == 18 and 'MASCULINO' in sexo:
    print('Quem nasceu em {} tem {} anos em 2018'.format(ano_de_nasc, idade_atual))
    print('Você deve se alistar IMEDIATAMENTE')

elif 'FEMININO' in sexo:
    print("Mulheres não precisam se alistar")

else:
    print("Sexo não definido")

