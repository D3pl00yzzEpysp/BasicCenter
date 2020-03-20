# -*- coding: utf-8 -*-

# Imports

from time import sleep
from termcolor import colored
import requests
import json


def cpf():

    print("-"*40)
    print(colored("^ Consulta Cpf Basica ^",'yellow'))
    print("-"*40)

    sleep(2)

    opcao = 1

    while opcao == 1:

        print()

        cpf2 = input(colored("DIGITE O CPF 》  ",'green'))

        print()

        req = requests.post(f"http://namso-cc.com/cpf2.php?cpf={cpf2}")

        data = req.text

        print()

        print(data)

        print()

        pergunta = input(colored('DESEJA CONSULTAR OUTRO 》 [y/n]  ','red'))

        print()

        if pergunta == 'y'.lower():

            opcao = 1

        else:

            opcao = 2

            print()

            print("OBRIGADO POR USAR :) @NinjaOFC  ")
            break


if __name__ == "__main__":

    cpf()
