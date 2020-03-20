from requests import post

def GerarR():

    print("\033[1;91mATENÇÃO SCRIPT DESENVOLVIDO POR VITX ©\033[m")

    print()

    cpf = int(input("Quantos Rg Deseja Gerar :  "))

    for repetir in range(0,cpf):

        requests = post("https://www.4devs.com.br/ferramentas_online.php",{"acao":"gerar_rg","pontuacao":"S"})

        resposta = requests.text
        print("="*5)
        print()
        print("\033[1;92mRG :\033[m]",resposta)
        print()
        print("="*5)

if(__name__ == "__main__"):
    GerarR()
