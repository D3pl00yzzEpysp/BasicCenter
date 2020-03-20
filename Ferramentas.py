# -*- coding: utf-8 -*-

import GeradorBanco
import GeradorDePessoas
import cpf
import GeradorRG
import a
import Wish
import ConsultaCpf
from time import sleep
from termcolor import colored



print("-"*40)
print("-"*40)
print()

print(colored('''_________   _____    _____             _____   ______   _   _   _______   ______   _____  
 |  _ \      /\      / ____| |_   _|  / ____|           / ____| |  ____| | \ | | |__   __| |  ____| |  __ \ 
 | |_) |    /  \    | (___     | |   | |       ______  | |      | |__    |  \| |    | |    | |__    | |__) |
 |  _ <    / /\ \    \___ \    | |   | |      |______| | |      |  __|   | . ` |    | |    |  __|   |  _  / 
 | |_) |  / ____ \   ____) |  _| |_  | |____           | |____  | |____  | |\  |    | |    | |____  | | \ \ 
 0|____/  /_/    \_\ |_____/  |_____|  \_____|           \_____| |______| |_| \_|    |_|    |______| |_|  \_\ ''',"green"))
print("-"*40)
sleep(2)
print()
print(colored("OBS : CASO QUEIRA POSTAR EM ALGUM LUGAR , DEIXE OS CREDITOS A MIM",'red'))
sleep(1)
print()
print('''       CONTATO

        TELEGRAM - @NinjaOFC''')
print()
sleep(1)
print("\033[;1m   1 - Gerador De Conta Bancaria\033[m")
print("\033[1;32m 2 - Gerador De CPF\033[m")
print("\033[1;33m 3 - Gerador De Pessoas (Dados)\033[m")
print("\033[1;92m 4 - Gerador De RG (Funcional)\033[m]")
print(colored("   5 - Checker Tufos",'green'))
print(colored("   6 - Checker Wish",'cyan'))
print(colored("   7 - Consulta CPF Basica",'blue'))
sleep(2)
print()

ver = int(input('Qual Gerador Deseja Usar >> '))

if ver == 1:
    print("•" *9)
    print()
    print("Abrindo Gerador De Conta Bancaria")
    print()
    print("•" *9)
    GeradorBanco.gerarB()
elif ver == 3:
    print("=" *10)
    print()
    print("Abrindo Gerador De Pessoas")
    print()
    print("=" *10)
    GeradorDePessoas.GerarP()
elif ver == 2:
    print("*" *8)
    print()
    print("Abrindo Gerador De CPF")
    print()
    print("*" *9)
    cpf.GerarC()
elif ver == 4:
    print("* "*8)
    print()
    print("ABRINDO GERADOR DE RG")
    print()
    print("*"*8)
    GeradorRG.GerarR()

elif ver == 5:

    print("*"*8)
    print()
    print(colored("ABRINDO CHECKER TUFOS",'red'))
    print()
    print("*"*8)
    a.ata()

elif ver == 6:
    print("*"*8)
    print()
    print(colored("ABRINDO CHECKER WISH",'red'))
    print()
    print("*"*8)
    sleep(3)
    Wish.wish()

elif ver == 7:
    sleep(2)
    print("*"*8)
    print()
    print(colored("ABRINDO CPF BASICA",'cyan'))
    print()
    print("*"*8)
    sleep(3)
    ConsultaCpf.cpf()
