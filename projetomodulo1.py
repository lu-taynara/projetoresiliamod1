import time

def inicio():

    jogar = True    
    while jogar:

        resposta_errada = True

        while resposta_errada:
            jogar = input('Você deseja jogar? s/n\n').lower()
            if jogar == 'n':
                print('Você saiu do jogo')
                resposta_errada = False
                jogar = False
            elif jogar == 's':
                jogadores()
                resposta_errada = False
                jogar = False
            else:
                print('Opção invalida\n')
                print('Escolha Sim ou Não')
                resposta_errada = True
            
def jogadores():
    print('Escolha um jogador:\n')
    time.sleep(2)
    print('Cuidado com a sua escolha, ela pode te levar a morte!!!')
    jogador = input('1 - Maldito' '\n2 - Sombra' '\n3 - Bocó\n')
    if jogador == '1':
        jogador = 'Maldito'
        fase1Maldito(jogador)
    elif jogador == '2':
        jogador = 'Sombra'
        fase1Sombra(jogador)
    elif jogador == '3':
        jogador = 'Bocó'
        fase1Boco(jogador)
    else:
        print('Opção invalida, tente novamente:\n')
        jogadores()


def fase1Maldito(jogador=''):

    resposta_errada = True
    while resposta_errada:
        continuar = ()
        print('\nOlá ' + jogador + ',\n Seja bem vindo CARCERE. No retorno de uma balada, você e seus amigos foram abordados por'
              ' um grupo de homens armados e foram forçados a entrar num carro estranho. Sim, vocês foram'
              ' vítimas de um sequestro. Já no cativeiro, fica claro que foi um crime encomendado. Porém,'
              ' o bandido não está disposto a liberá-los com vida, mesmo após o pagamento do resgate. Vocês'
              ' precisarão de inteligência e sangue frio para ajuda- los a escapar!')
        time.sleep(2)

        print('\nEnquanto os bandidos saíram para buscar água você tem uma chance de escapar! ')
        time.sleep(2)

        fase1 = input('Escolha uma opção'
                      '\n1 - Quebrar a janela'
                      '\n2 - Atacar o bandido em grupo\n')

        if fase1 == '1':
            print('Muito bem, você passou para a próxima fase!!!!!')
            fase1MalditoI()
            resposta_errada = False
            time.sleep(2)

        elif fase1 == '2':
            continuar_pergunta = True
            while continuar_pergunta:

                print('\nVocê falhou, o bandido atirou =(\n')
                continuar = input('Deseja tentar novamente? s/n\n')

                if continuar == 's':
                    fase1Maldito(jogador)
                    continuar_pergunta = False

                elif continuar == 'n':
                    print('Você saiu do jogo')
                    continuar_pergunta = False
                    resposta_errada = False

                else:
                    print("Você digitou opção errada!")
                    continuar_pergunta = True

        else:
            print('Você digitou errado')
            resposta_errada = True


def fase1MalditoI():
    continuar2 = ()
    print('\nMuito bem, você conseguiu sair do cativeiro! Agora você pode:')
    fase2 = input('\n1 - Pedir socorro'
                  '\n2 - Correr\n')
    if fase2 == '2':
        fase1MalditoII()
    elif fase2 != '2':
        print('\nPoxa vida, o sequestrador te ouviu, você perdeu =( !\n')
        continuar2 = input('Deseja tentar novamente? s/n\n')

        if continuar2 == 's':
            time.sleep(2)
            fase1MalditoI()

        elif continuar2 == 'n':
            print('Você saiu do jogo')
    else:
        print('Fim de jogo')

        fase1MalditoI()


def fase1MalditoII():
    continuar3 = ()
    print('\nAgora falta pouco!!!!!!!! \nVocê percebeu que estava próximo(a) à uma avenida, então você decide: ')
    fase3 = input('\n1 - Tenta pedir uma carona'
                  '\n2 - Procura o comércio mais próximo\n')
    if fase3 == '2':
        print('\nUAU, VOCÊ CONSEGUIU, PARABENS!!!!!\n')

    elif fase3 == '1':
        print(
            '\nQue azar, o carro que parou era do sequestrador! Você MORREU =(!!!!\n')
        continuar3 = input('Deseja tentar novamente? s/n\n')
        if continuar3 == 's':
            time.sleep(2)
            fase1MalditoII()
        elif continuar3 == 'n':
            print('Você saiu do jogo')
    else:
        print('Fim de jogo')
        fase1MalditoII()

def fase1Sombra(jogador=''):

    resposta_errada = True
    while resposta_errada:
        continuar = ()
        print('\nOlá ' + jogador + ',\n Seja bem vindo CARCERE. No retorno de uma balada, você e seus amigos foram abordados por'
              ' um grupo de homens armados e foram forçados a entrar num carro estranho. Sim, vocês foram'
              ' vítimas de um sequestro. Já no cativeiro, fica claro que foi um crime encomendado. Porém,'
              ' o bandido não está disposto a liberá-los com vida, mesmo após o pagamento do resgate. Vocês'
              ' precisarão de inteligência e sangue frio para ajuda- los a escapar!')
        time.sleep(2)

        print('\nVocê é o mais forte entre seus amigos, mas vá com calma!\nO canalha está de costas, o que fazer: ')
        time.sleep(2)

        fase1 = input('Escolha uma opção'
                      '\n1 - Acertar o bandido com uma cadeira'
                      '\n2 - Tentar segura-lo para que os outros possam correr\n')

        if fase1 == '1':
            print('Muito bem, você passou para a próxima fase!!!!!')
            fase1SombraI()
            resposta_errada = False
            time.sleep(2)

        elif fase1 == '2':
            continuar_pergunta = True
            while continuar_pergunta:

                print('\nGame over, você foi baleado =(\n')
                continuar = input('Deseja tentar novamente? s/n\n')

                if continuar == 's':
                    fase1Sombra(jogador)
                    continuar_pergunta = False

                elif continuar == 'n':
                    print('Você saiu do jogo')
                    continuar_pergunta = False
                    resposta_errada = False

                else:
                    print("Você digitou opção errada!")
                    continuar_pergunta = True

        else:
            print('Você digitou errado')
            resposta_errada = True


def fase1SombraI():
    continuar2 = ()
    print('\nMuito bem, você escapou do cativeiro! Mas ainda não acabou, agora você pode:')
    fase2 = input('\n1 - Correr até a avenida'
                  '\n2 - Roubar um carro do estacionamento\n')

    if fase2 == '2':
        fase1SombraII()
    elif fase2 != '2':
        print('\nPoxa vida, você foi atropelado por uma carreta. Perdeu!!!! =( !\n')
        continuar2 = input('Deseja tentar novamente? s/n\n')

        if continuar2 == 's':
            time.sleep(2)
            fase1SombraI()

        elif continuar2 == 'n':
            print('Você saiu do jogo')
    else:
        print('Fim de jogo')

        fase1SombraI()


def fase1SombraII():
    continuar3 = ()
    print('\nAgora falta pouco!!!!!!!! \nVocê percebeu que estava próximo(a) à uma viatura de policia, então você decide: ')
    fase3 = input('\n1 - Pede ajuda para a policia'
                  '\n2 - Passa direto e vai até um bar próximo\n')
    if fase3 == '2':
        print('\nUAU, VOCÊ CONSEGUIU, PARABENS!!!!!\n')

    elif fase3 == '1':
        print(
            '\nQue azar, eles te deram 80 tiros por enganos. Você MORREU =(!!!!\n')
        continuar3 = input('Deseja tentar novamente? s/n\n')
        if continuar3 == 's':
            time.sleep(2)
            fase1SombraII()
        elif continuar3 == 'n':
            print('Você saiu do jogo')
    else:
        print('Fim de jogo')
        fase1SombraII()

def fase1Boco(jogador=''):

    resposta_errada = True
    while resposta_errada:
        continuar = ()
        print('\nOlá ' + jogador + ',\n Seja bem vindo CARCERE. No retorno de uma balada, você e seus amigos foram abordados por'
              ' um grupo de homens armados e foram forçados a entrar num carro estranho. Sim, vocês foram'
              ' vítimas de um sequestro. Já no cativeiro, fica claro que foi um crime encomendado. Porém,'
              ' o bandido não está disposto a liberá-los com vida, mesmo após o pagamento do resgate. Vocês'
              ' precisarão de inteligência e sangue frio para ajuda- los a escapar!')
        time.sleep(2)

        print('\nVocê é o mais lerdo entre seus amigos, fique atento! ')
        time.sleep(2)

        fase1 = input('Escolha uma opção'
                      '\n1 - Ajuda seu amigo a quebrar a janela'
                      '\n2 - Tentar correr quando seus amigos agarram o bandido\n')

        if fase1 == '1':
            print('Muito bem, você passou para a próxima fase!!!!!')
            fase1BocoI()
            resposta_errada = False
            time.sleep(2)

        elif fase1 == '2':
            continuar_pergunta = True
            while continuar_pergunta:

                print('\nDessa vez você perdeu, foi atingido nas costas enquanto tentava fugir =(\n')
                continuar = input('Deseja tentar novamente? s/n\n')

                if continuar == 's':
                    fase1Boco(jogador)
                    continuar_pergunta = False

                elif continuar == 'n':
                    print('Você saiu do jogo')
                    continuar_pergunta = False
                    resposta_errada = False

                else:
                    print("Você digitou opção errada!")
                    continuar_pergunta = True

        else:
            print('Você digitou errado')
            resposta_errada = True


def fase1BocoI():
    continuar2 = ()
    print('\nMuito bem, até qui você foi bem! está quase lá, agora você pode:')
    fase2 = input('\n1 - Se esconder em uma casa abandonada'
                  '\n2 - Correr em direção à uma avenida\n')
    if fase2 == '2':
        fase1BocoII()
    elif fase2 != '2':
        print('\nAaah que pena, você foi caiu e bateu a cabeça. Morreu, Bocó!!!! =( !\n')
        continuar2 = input('Deseja tentar novamente? s/n\n')

        if continuar2 == 's':
            time.sleep(2)
            fase1BocoI()

        elif continuar2 == 'n':
            print('Você saiu do jogo')
    else:
        print('Fim de jogo')

        fase1BocoI()


def fase1BocoII():
    continuar3 = ()
    print('\nAgora falta pouco!!!!!!!! \nAgora ja anoiteceu,  o que vc pretende fazer? ')
    fase3 = input('\n1 - Passa a noite no esconderijo '
                  '\n2 - Anda com cuidado até o estacionamento\n')
    if fase3 == '2':
        print('\nUAU, VOCÊ CONSEGUIU, PARABENS!!!!!\n')

    elif fase3 == '1':
        print(
            '\nPoxa vida, a policia te confundiu com o Lázaro. Você MORREU =(!!!!\n')
        continuar3 = input('Deseja tentar novamente? s/n\n')
        if continuar3 == 's':
            time.sleep(2)
            fase1BocoII()
        elif continuar3 == 'n':
            print('Você saiu do jogo')
    else:
        print('Fim de jogo')
        fase1BocoII()




inicio()
