print("Qual a velocidade atual do carro?")
v = int(input("\033[1mVelocidade em km: \033[m")) #velocidade do carro
permitida = 80 #velocidade permitida
multa = (v - permitida) * 7

if v > permitida:
    print("\033[31mMULTADO!\033[m Você exedeu o limite permitido que é de \033[35m{}\033[mkm!".format(permitida))
    print("Você deve pagar uma multa de \033[32m{}R$\033[m".format(multa))
    print("\033[33mTenha um bom dia, diriga com segurança\033[m")
else:
    print("Parabens,você estava abaixo do limite permitido")