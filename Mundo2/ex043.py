print("---Calulcadora de IMC---")
peso = float(input("Peso(kg): "))
altura= float(input("Altura(m): "))
IMC = peso / ( altura**2 )
print("O IMC dessa pessoa é {:.1f}".format(IMC))

if IMC <= 18.5:
    print("Essa pessoa está ABAIXO DO PESO")
elif 18.5 < IMC <= 25:
    print("Essa pessoa está NO PESO IDEAL")
elif 25 < IMC <= 30:
    print("Essa pessoa está em SOBREPESO")
elif 30 < IMC <= 40:
    print("Essa pessoa está com OBESIDADE")
elif IMC > 40:
    print("Essa pessoa está com OBESIDADE MÓRBIDA")
