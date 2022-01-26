import random
from time import sleep
op = ['PEDRA' , 'PAPEL' , 'TESOURA']
computador = random.choice(op).lower().title()
print("""Suas opções:
[ PEDRA ]
[ PAPEL ] 
[ TESOURA ] """)
jogada = input("Qual a sua jogada? ").upper()

print("\033[31mJO\033[m")
sleep(1)
print("\033[31mKEN\033[m")
sleep(1)
print("\033[31mPO!!!\033[m")

if jogada == 'PEDRA':
    jogada = jogada.lower().title()
    print("-=" * 12)
    print("Computador jogou",computador)
    print("Jogador jogou",jogada)
    print("-=" * 12)
    if computador == 'Pedra':
        print("EMPATE")
    elif computador == 'Papel':
        print("\033[32mCOMPUTADOR VENCE\033[m")
    elif computador == 'Tesoura':
        print("\033[32mJOGADOR VENCE\033[m")

elif jogada == 'PAPEL':
    jogada = jogada.lower().title()
    print("-=" * 12)
    print("Computador jogou",computador)
    print("Jogador jogou",jogada)
    print("-=" * 12)
    if computador == 'Pedra':
        print("\033[32mJOGADOR VENCE\033[m")
    elif computador == 'Papel':
        print("EMPATE")
    elif computador == 'Tesoura':
        print("\033[32mCOMPUTADOR VENCE\033[m")

elif jogada == 'TESOURA':
    jogada = jogada.lower().title()
    print("-=" * 12)
    print("Computador jogou",computador)
    print("Jogador jogou",jogada)
    print("-=" * 12)
    if computador == 'Pedra':
        print("\033[32mCOMPUTADOR VENCE\033[m")
    elif computador == 'Papel':
        print("\033[32mJOGADOR VENCE\033[m")
    elif computador == 'Tesoura':
        print("EMPATE")




