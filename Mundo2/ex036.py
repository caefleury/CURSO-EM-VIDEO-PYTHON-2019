casa = float(input("Qual o valor da casa: R$"))
sal = float(input("Salario mensal: R$"))
anos = int(input("Em quantos anos a casa será paga: "))

meses = anos * 12
prest_mensal = casa / meses
limite = sal * 30/100
cores = {'amarelo' : '\033[33m',
         'verde' : '\033[32m',
         'vermelho' : '\033[31m',
         'limpa' : '\033[m'}

print("Para pagar uma casa de R${:.2f} em {}{} anos{}, o valor a ser pego por mês é de R${:.2f}".format(casa,cores['amarelo'],anos,cores['limpa'],prest_mensal))

if prest_mensal <= limite:
    print("Empréstimo \033[32mAPROVADO\033[m")
else:
    print("Empréstimo \033[31mNEGADO\033[m")
