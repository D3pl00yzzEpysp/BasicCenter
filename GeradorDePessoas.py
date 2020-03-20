from requests import post
import json
from time import sleep

def GerarP():
    print("\033[1;91mEsse Script Foi Feito Por Viitx(Ninja), Deixe Todos Os Creditos A Ele")
    print()
    print("\033[1;91m Aviso: Esse Script Irá Motrar Os Dados Nesse Formato\033[m")
    print()
    print("\033[1;33mNome : ** ","idade : **\033[m")
    print()
    escolha = int(input('''
        1- Sim
        2- Não
Deseja Gerar Os Dados >>> '''))
    sleep(1)
    print()
    if escolha == 1:
        requests = post("https://www.4devs.com.br/ferramentas_online.php",{"acao":"gerar_pessoa","sexo":"I","pontuacao":"S","idade":"0","cep_estado":" ","txt_qtde":"1","cep_cidade":" "})
        resposta = requests.json()
        print("Dados",": ",resposta)
