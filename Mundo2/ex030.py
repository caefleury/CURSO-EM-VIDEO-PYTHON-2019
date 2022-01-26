print("Qual a distancia da sua viagem?")
d = float(input("Distancia em km: "))
cores = {'limpa' : '\033[m',
         'verde' : '\033[32m',
         'amarelo' : '\033[33m'}
print("Você está prestes a começar uma viagem de {}{}{}km".format(cores['amarelo'],d,cores['limpa']))

if d <= 200:
    preço = 0.50 * d
    print("O preço da sua passagem será de {}{:.2f}{}R$".format(cores['verde'],preço,cores['limpa']))
else:
    preço = 0.45 * d
    print("O preço da sua passagem será de {}{:.2f}{}R$".format(cores['verde'],preço,cores['limpa']))
