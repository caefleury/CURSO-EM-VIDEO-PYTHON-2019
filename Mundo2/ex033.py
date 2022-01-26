print("\033[4;31mQual o salário do funcionário?\033[m")
sal = float(input("\033[1;34mSalário:\033[m "))
cores = {'ciano' : '\033[36m',
         'limpo' : '\033[m',
         'vermelho' : '\033[31m'}
if sal <= 1250:
    aumento = sal * 1.15
else:
    aumento = sal * 1.10

print("O funcionário que ganhava {}R${:.2f}{} passa a ganhar {}R${:.2f}".format(cores['vermelho'],sal,cores['limpo'],cores['ciano'], aumento))