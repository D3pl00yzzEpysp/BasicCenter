from requests import post

def GerarC():

    print("\033[1;91m Esse Script Foi Desenvolvido Por Viitx(Ninja), Deixe Todos Os Creditos A Ele\033[?")
    print()

    num = int(input("Quantos Cpf Deseja Gerar >> "))

    for repetir in range(0,num):

        requesitos = post("https://www.4devs.com.br/ferramentas_online.php",{"cpf_estado":"AL","pontuacao:":"S","acao":"gerar_cpf"})
        resposta = requesitos.text
        print("CPF", repetir,": ",resposta)

if(__name__ == "__main__"):
    GerarC()
