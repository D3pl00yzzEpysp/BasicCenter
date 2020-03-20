from requests import post
import json 
from time import sleep

def gerarB():
    print('''\033[1;91m OBS : OS DADOS SERÃO MOSTRADO EM FORMA DE CODIGO HTML 
        MOTIVO: PREGUIÇA DE AJEITAR\033[m''')
    sleep(1)
    print()

    cont = int(input("Quantas Contas Bancarias Deseja Gerar >>> "))

    for repetir in range(0,cont):
        requests = post("https://www.4devs.com.br/ferramentas_online.php",{"acao":"gerar_conta_bancaria","estado":"","banco":""})
        resposta = requests.text
        print()

        conta = resposta.split('<div id="conta_corrente" onclick="fourdevs.selectText(this)" class="output-txt output-txt-active">',2)
        conta = conta[1].split('<span class="clipboard-copy">',2)
        conta = conta[0]

        argencia = resposta.split('<div id="agencia" onclick="fourdevs.selectText(this)" class="output-txt output-txt-active">',2)
        argencia = argencia[1].split('<span class="clipboard-copy">',2)
        argencia = argencia[0]

        banco = resposta.split('<div id="banco" onclick="fourdevs.selectText(this)" class="output-txt output-txt-active">',2)
        banco = banco[1].split('<span class="clipboard-copy">',2)
        banco = banco[0]

        cidade = resposta.split('<div id="cidade" onclick="fourdevs.selectText(this)" class="output-txt output-txt-active">',2)
        cidade = cidade[1].split('<span class="clipboard-copy">',2)
        cidade = cidade[0]


        estado = resposta.split('<div id="estado" onclick="fourdevs.selectText(this)" class="output-txt output-txt-active">',2)
        estado = estado[1].split('<span class="clipboard-copy">',2)
        estado = estado[0]


        print("\n")
        print("Conta: ",conta)
        print("Argencia: ",argencia)
        print("Banco: ",banco)
        print("Cidade: ",cidade)
        print("Estado: ",estado)



if(__name__ == "__main__"):
    GerarB()
