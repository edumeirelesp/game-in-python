from time import sleep   # JOGO: O BRUXO DA MOTANHA DE FOGO
import emoji
#  funções
def separa():
    print(" ")
    print(40* emoji.emojize(":wavy_dash:",use_aliases=True))
    print(" ")


def gameover():
    print(f"{emoji.emojize(':skull:',use_aliases=True):>20} \33[31mGAME OVER\33[m {emoji.emojize(':skull:',use_aliases=True)}")


                         # INTRODUÇÃO , PROGRAMA PRINCIPAL.
print()
print(f"\33[31m{'INICIANDO O JOGO':>35}\33[m", end=" ")
for a in range(0, 1):
    sleep(2)
    print(emoji.emojize(":thought_balloon:", use_aliases=True), end=" ")
    for b in range(0, 1):
        sleep(2)
        print(emoji.emojize(":thought_balloon:", use_aliases=True), end=" ")
        for c in range(0, 1):
            sleep(2)
            print(emoji.emojize(":thought_balloon:", use_aliases=True))
sleep(2)
separa()
sleep(1)
print(f"\33[33mA aventura começa á caminho da montanha de fogo\33[m {emoji.emojize(':volcano:',use_aliases=True)}\33[33m localizada no continente Lascard.\33[m")
sleep(2)
print(
    "\33[33mO jovem guerreiro chamado Zargo na busca de encontrar sua amada Azilia que foi sequestrada pelo bruxo Zaos.\33[m")
sleep(2)
print("\33[33mAté la desafio e misterios lhe aguarda.\33[m")
sleep(2)
separa()
sleep(1)
print("""\33[34mVamos começar. Escolha qual caminho deseja tomar...\33[m

1 Para seguir pelo pantano.
2 Para seguir pela floresta desconhecida.""")
sleep(1)
separa()
sleep(1)
op = int(input("\33[34mQual caminho deseja seguir? [1 ou 2]:\33[m "))
separa()
if op < 1 or op > 2:  # VERIFICANDO E VALIDANDO A VAR OP
    while True:
        op = int(input("\33[34mDigite novamente, 1 ou 2:\33[m "))
        if op == 1 or op == 2:
            break
if op == 1:  # OP 1 PANTANO  ( 1° DESAFIO )
    sleep(1)
    print("\n\33[33mVocê estar em um terreno pantanoso, ver algo estranho se movendo.\33[m")
    print("\33[33mPercebe uma grande calda. Oque será?...\33[m")
    sleep(1)
    print(f"\33[33mEm seguida é revelado um grande crocodilo\33[m {emoji.emojize(':crocodile:',use_aliases=True)} \33[33mDESEJA ENFRENTALO ? [S/N]\33[m")
    separa()
    op1 = " "
    while op1 not in "SN":  # VERIFICANDO E VALIDANDO A VAR OP1
        sleep(1)
        op1 = str(input("\33[34mOque você deseja? [SIM] para enfrentalo ou [NÂO] para fugir:\33[m ")).strip().upper()[0]
        if op1 == "SN":
            break
    separa()
    if op1 == "S": # SIM, ENFRENTAR O CROCODILO
        sleep(1)
        print("\33[33mVocê tem um arco e está com apenas 6 flexas, tem uma adaga e uma espada longa...\33[m")
        sleep(1)
        separa()
        print("""\33[34mCom oque deseja enfrentar a criatura:\33[m 
        
        1 Arco
        2 Adaga
        3 Espada longa""")
        sleep(1)
        separa()
        escolha = int(input("\33[34mDigita qual sua escolha ? [1 , 2 , 3 ]:\33[m "))
        if escolha < 1 or escolha > 3:
            while True:
                escolha = int(input("\33[34mEscolha incorreta digite novamente [1 , 2 ou 3]:\33[m "))
                if escolha >= 1 and escolha <= 3:
                    break
        if escolha == 1:                                 # ARCO
            sleep(1)
            print("\33[33mVocê escolheu o arco. Você tem que larga sua espada longa, porque ela pesa muito....\33[m")
            sleep(1)
            print("\33[33mAssim você ganha mais destreza.\33[m")
            sleep(1)
            print("\33[33mA fera lhe atacou e você esquivou sem nenhum dano. Oque você faz em seguida?...\33[m")
            sleep(1)
            separa()
            print("""          \33[34mLEMBRANDO QUE VOCÊ SÓ TEM 6 FLEXAS NO ARCO\33[m     
            
            1 Atira flexa no olho da criatura.
            2 Procura algum ponto mas alto para se posicionar.
            3 Espera proxima reação da criatura.""")
            separa()
            op = int(input("\33[34mQual sua ação? [1, 2 ou 3 ]:\33[m" ))
            if op < 1 or op > 3:
                while True:
                    op = int(input("\33[34mOpção errada, Digite novamente [1, 2 ou 3]:\33[m "))
                    if op >= 1 and op <= 3:
                        break
            separa()
            if op == 1:                 # ARCO: ATACA O OLHO
                sleep(1)
                print("\33[33mDepois de duas tentativas, você acerta no olho do crocodilo, com isso consiguiu atordoa-lo...\33[m")
                sleep(1)
                print("\33[33mO crocodilo virou-se para tentar tirar a flexa, ficando com sua parte inferior exposta...\33[m")
                sleep(1)
                print("\33[33mVocê puxou adaga e rasgou o pescoço do crocodilo, e assim conseguindo mata-lo.\33[m")
                sleep(1)
                print("\33[33mVocê continuar o caminho, seguindo pelo pantano apôs sua vitoria...\33[m")
                sleep(1)
                print("\33[33mE ver a saida a frente a alguns metros e continua ate ver a frente a montanha de fogo...\33[m")
                sleep(1)
                separa()
                print("""\33[34m                        ESTAMOS QUASE LA ...\33[m
                
                1 Continua a jornada ate a montanha.
                2 Da uma parada e repor as energias.""")
                separa()
                escolha=int(input("\33[34mQual sua escolha ? [ 1 ou 2 ]:\33[m "))
                if escolha < 1 or escolha > 2:
                    while True:
                        escolha=int(input("\33[34mDigite novamente [ 1 ou 2 ]:\33[m "))
                        if escolha >= 1 and escolha <= 2:
                            break
                separa()
                if escolha == 1:                # ARCO: CAMINHO MONTANHA DE FOGO
                    sleep(1)
                    print("\33[33mVocê continua sua caminhada, chegando a entrada da montanha de fogo...\33[m")
                    sleep(1)
                    print("""                           \33[34mEncontrando dois caminhos\33[m   
                
                1 Atravesar Uma ponta que em baixo passa um rio de lava.
                2 Um caminho estreito e muito escuro, não se ver o fim.""")

                    sleep(1)
                    op=int(input("\33[34mQual sua escolha ? [ 1 ou 2 ]:\33[m "))
                    if op < 1 or op > 2:
                        while True:
                            op=int(input("\33[34mEscolha incorreta digite novamente [ 1 ou 2 ]:\33[m "))
                            if  op >= 1 and op <= 2:
                                break
                    separa()
                    if op == 1:                                 # ARCO: PONTE DE LAVA
                        sleep(1)
                        print("\33[33mVocê atravessa a ponte com dificuldades...\33[m")
                        sleep(1)
                        print("\33[33mDepois de atravessar a ponte se depara com uma passagem, você ebtra beka e não acredita no que ver adiante...\33[m")
                        sleep(1)
                        print("\33[33mEncontra finalmente sua amada Azilia...\33[m")
                        sleep(1)
                        print("\33[33mQuando você tenta se aproximar dela para livra-la das amarras que a prendia...\33[m")
                        sleep(1)
                        print("\33[33mZAOS APARECE...\33[m")
                        sleep(1)
                        print("\33[33mO GRANDE CONFRONTO CHEGOU!!\33[m")
                        sleep(1)
                        separa()
                        print("""           \33[34mCom qual arma você pretende usar nesse combate?\33[m
                        
                        1 Adaga e arco
                        2 Espada longa""")
                        sleep(1)
                        escolha=int(input("\33[34mQua sua escolha? [ 1 ou 2 ]:\33[m "))
                        if escolha < 1 or escolha > 2:
                            while True:
                                escolha=int(input("\33[34mEscolha incorreta. Digite novamente [ 1 ou 2 ]:\33[m "))
                                if escolha >= 1 and escolha <= 2:
                                    break
                        separa()
                        if escolha == 1:        # ARCO: ADAGA E ARCO NA PONTE DE LAVA , FIM DE JOGO
                            sleep(1)
                            print("\33[33mVocê está bastante agil pois está de arco e adaga...\33[m")
                            sleep(1)
                            print("\33[33mLargou sua espada longa, decide da uma envestida brutal em Zaos...\33[m")
                            sleep(1)
                            print("\33[33mZaos com sua magia tenta se defender...\33[m")
                            sleep(1)
                            print("\33[33mZaos se cansa e baixa a guarda...\33[m")
                            sleep(1)
                            print("\33[33mAs suas flexas acabaram...\33[m")
                            sleep(1)
                            print("\33[33mVocê avança para cima de Zaos com sua adaga e o acaba ferindo fatalmente...\33[m")
                            sleep(1)
                            print("\33[33mEnfim você conseguiu derrota Zaos e libertou sua amada Azilia.\33[m")
                            sleep(1)
                            print("\33[33mPARABÉNS VOCÊ CONSEGUIU VENCER ZAOS!!\33[m")
                            sleep(1)
                            print()
                            print(f"{emoji.emojize(':couple:',use_aliases=True)} \33[33mFim de jogo!!\33[m {emoji.emojize(':couplekiss:',use_aliases=True)}")
                        else:                     # ARCO: ESPADA LONGA NA PONTE DE LAVA, FIM DE JOGO MAS ELABORADO
                            sleep(1)
                            print("\33[33mVocê corre para cima de Zaos arrastando a espada no chãos flamejando faiscas...\33[m")
                            sleep(1)
                            print("\33[33mZaos contrataca lança uma magia para tentar se defender...\33[m")
                            sleep(1)
                            print("\33[33mFica um empasse e os dois se chocam com você levando a pior, seu braço esquerdo quebreou...\33[m")
                            sleep(1)
                            separa()
                            print("""                     \33[34mVocê contrataca ou aguarda a reação de Zaos ?\33[m
                            
                            1 Investe em um novo ataque.
                            2 Aguarda reação de Zaos.""")
                            sleep(1)
                            op=int(input("\33[34mQual sua escolha? [1 ou 2]:\33[m "))
                            if op < 1 or op > 2:
                                while True:
                                    op=int(input("\33[34mOpção incorreta, digite novamente [1 ou 2]:\33[m "))
                                    if op >= 1 and op <= 2:
                                        break
                            separa()
                            if op == 1:    # ARCO: ULTIMA ESCOLHA DA PONTE DE LAVA, INVESTIDA ATAQUE
                                sleep(1)
                                print("\33[33mVocê mais uma vez, com apenas uma das mãos apunhala a espada...\33[m")
                                sleep(1)
                                print("\33[33mE ataca ferozmente Zaos...\33[m")
                                sleep(1)
                                print("\33[33mA magia de Zaos não obteve o mesmo resultado ele foi fatalmente ferido...\33[m")
                                sleep(1)
                                print("\33[33mPARABÉNS VOCÊ CONSEGUIU VENCER ZAOS.\33[m")
                                sleep(1)
                                print("\33[33mSalvou sua amada Azilia...\33[m")
                                sleep(1)
                                print()
                                print(f"{emoji.emojize(':couple:',use_aliases=True)} \33[33mFim de jogo!!\33[m {emoji.emojize(':couplekiss:',use_aliases=True)}")
                            else:               # ARCO: AGUARDA A REAÇÃO
                                sleep(1)
                                print("\33[33mZaos não teve piedade e lhe ataca ferozmente, com sua magia e o derrota...\33[m")
                                sleep(1)
                                print("\33[33mSua amada para sempre será prisioneira de Zaos...\33[m")
                                sleep(1)
                                print("\33[37mVOCÊ MORREU!!\33[m")
                                sleep(1)
                                print()
                                gameover()
                    else:                           # ARCO: MURO ESTREITO , MORTE
                        sleep(1)
                        print("\33[33mVocê entra no caminho sem conseguir enchergar um palmo a frente...\33[m")
                        sleep(1)
                        print("\33[33mAtrás de você cairam umas pedras, você não tem mas como voltar...\33[m")
                        sleep(1)
                        print("\33[33mVocê continua o caminho e cai em um abismo...\33[m")
                        sleep(1)
                        print("\33[37mVOCÊ MORREU!!\33[m")
                        sleep(1)
                        print()
                        gameover()
                else:                             # ARCO: ESCOLHEU DESCANSO
                    sleep(1)
                    print("\33[33mVocê adormeceu...\33[m")
                    sleep(1)
                    print("\33[33mO bruxo Zaos soube que você conseguiu vencer a criatura...\33[m")
                    sleep(1)
                    print("\33[33mZaos foi ao seu encontro, viu você adormecido e lhe invenenou.\33[m")
                    sleep(1)
                    print("\33[37mVOCê MORREU!!\33[m")
                    sleep(1)
                    print()
                    gameover()
            elif op == 2:                          # ARCO: POSIÇÃO ALTA PARA ATACA
                sleep(1)
                print("\33[33mVocê estar em um pantano, so tem lama e arvores podres.\33[m")
                sleep(1)
                print("\33[33mO crocodilo lhe alcança e te ataca brutalmente, te derrubando e te da outro ataque...\33[m")
                sleep(1)
                print("\33[37mVOCÊ MORREU!!\33[m")
                sleep(1)
                print()
                gameover()
            elif op == 3:                          # ARCO: AGUARDA CRIATURA
                sleep(1)
                print("\33[33mO crocodilo lhe atacou brutalmente e você não conseguiu se esquiva, e foi derrubado...\33[m")
                sleep(1)
                print("\33[33mVocê recebeu outro ataque...\33[m  \33[37mVOCÊ ESTÁ MORTO!!\33[m")
                sleep(1)
                print()
                gameover()
        elif escolha == 2:                             #ADAGA
            separa()
            sleep(1)
            print("\33[33mVocê escolheu adaga, e assim decidiu jogar as outras armas...\33[m")
            sleep(1)
            print("\33[33mA criatura lhe atacou e você conseguiu desviar do ataque...\33[m")
            sleep(1)
            print("\33[33mUma vantagem de estar com adaga é a destreza que você ganha...\33[m")
            sleep(1)
            separa()
            print("""\33[34mE assim ficou mais facil desviar dos ataques da fera.\33[m \33[34mOque você quer fazer agora?\33[m
            
            1 Pula em cima da criatura.
            2 Tenta fugir da criatura.""")
            separa()
            sleep(1)
            op=int(input("\33[34mDigite sua escolha [ 1 ou 2 ]:\33[m "))
            if op < 1 or op > 2:
                while True:
                    op=int(input("\33[34mDigitou errado, Digite novamente [ 1 ou 2 ]:\33[m "))
                    if op == 1 or op == 2:
                        break
            separa()
            if op == 1:                 # ADAGA: PULA EM CIMA DA CRIATURA
                sleep(1)
                print("\33[33mO crocodilo se vira com você em cima dele e você acaba sendo esmagado...\33[m")
                sleep(1)
                print("\33[37mVOCÊ MORREU...\33[m")
                sleep(1)
                print()
                gameover()
            elif op == 2:                # ADAGA: TENTAR FUGIR
                sleep(1)
                print("\33[33mVocê está num pantano, só tem lama e arvores podres...\33[m")
                sleep(1)
                print("\33[33mO crocodilo te alcança e te ataca brutalmente, e te da outro ataque mortal...\33[m")
                sleep(1)
                print("\33[37mVOCÊ MORREU...\33[m")
                sleep(1)
                print()
                gameover()
        elif escolha == 3:                             # ESPADA LONGA: PARTE 2 DO PANTANO
            separa()
            sleep(1)
            print(
                "\33[33mUsando a espada longa você fica muito lento, tem que ter um ataque preciso ou será seu fim.\33[m")
            sleep(1)
            print("""\33[33mVocê se livra do arco, ele poderia lhe atrapalhar no combate.\33[m \33[34m
            
            Você tem as seguintes opções...\33[m
            
            1 Esperar o ataque da criatura.
            2 Atacar a cabeça da criatura.""")
            separa()
            sleep(1)
            op=int(input("\33[34mDigite sua escolha? [1 ou 2]:\33[m "))
            if op < 1 or op > 2 :
                while True:
                    op=int(input("\33[34mOpção não existente, Digite novamente [1 ou 2]:\33[m "))
                    if op == 1 or op == 2:
                        break
            separa()
            if op == 1:                      # ESPADA LONGA: ESPERA O ATAQUE
                sleep(1)
                print("\33[33mO crocodilo lhe ataca, e com a boca aberta fica funeravel e você enfia a espara longa...\33[m")
                sleep(1)
                print("\33[33mDentro da cabeça do crocodilo... e assim chegando ao cérebro.\33[m")
                sleep(1)
                print("\33[33mEnfim consegue derrotar o crocodilo... Você ainda tem um longo caminho, se levanta e continua...\33[m")
                sleep(1)
                print("\33[33mContinua o caminho e consegui sair do pantano, a frente consegue ver a montanha de fogo...\33[m")
                sleep(1)
                separa()
                print("""                   \33[34mEstamos quase la...\33[m
                 
                 1 Seguir para montanha.
                 2 Parar e descansar.""")
                separa()
                sleep(1)
                escolha=int(input("\33[34mQual sua escolha? [1 ou 2]:\33[m "))
                if escolha < 1 or escolha > 2:
                    while True:
                        escolha=int(input("\33[34mEscolha encorreta, digite novamente [1 ou 2]:\33[m "))
                        if escolha == 1 or escolha == 2:
                            break
                if escolha == 1:              # ESPADA LONGA: SEGUINDO PARA MOTANHA DE FOGO
                    separa()
                    sleep(1)
                    print("\33[33mVocê segui o caminho para montanha de fogo...\33[m")
                    sleep(1)
                    print("\33[33mChegou na montanha de fogo, entrando nela logo observa...\33[m")
                    sleep(1)
                    print("\33[33mUma ponta que por baixo passa um rio de lava...\33[m")
                    sleep(1)
                    separa()
                    print("""\33[34m                        Oque você faz?\33[m
                    
                    1 Atravesa a ponte.
                    2 Procura outra entrada.""")
                    sleep(1)
                    separa()
                    op=int(input("\33[34mQual sua oção? [1 ou 2]:\33[m "))   # ESCOLHA: PASSA PONTE OU PROCURA ENTRADAS
                    if op < 1 or op > 2:
                        while True:
                            op=int(input("\33[34mDigite novamente entre [1 ou 2]:\33[m "))
                            if op == 1 or op == 2:
                                break
                    separa()
                    if op == 1:                    # ESPADA LONGA: ATRAVESSAR A PONTE, ENCONTRA ZAOS NO SALAO
                        sleep(1)
                        print("\33[33mVocê atravessa a ponte com dificuldades...\33[m")
                        sleep(1)
                        print("\33[33mDepois de atravessar entra num salão e se depara com Zaos...\33[m")
                        sleep(1)
                        print("\33[33mNo fundo ver novamente sua amada Azilia...\33[m")
                        sleep(1)
                        print("\33[33mLebrando, você só está com sua espada!\33[m")
                        sleep(1)
                        separa()
                        print("""\33[34m                         Diga qual sua ação?\33[m
                        
                        1 Você ataca Zaos.
                        2 Você aguarda ação de Zaos.""")
                        sleep(1)
                        op=int(input("\33[34mQual sua ação? [1 ou 2]:\33[m "))
                        if op < 1 or op > 2:
                            while True:
                                op=int(input("\33[34mDigite novamente entre [1 ou 2]:\33[m "))
                                if op == 1 or op == 2:
                                    break
                        separa()
                        if op == 1 :                  # ESPADA LONGA: VOCÊ ATACA ZAOS E VENCE O JOGO
                            sleep(1)
                            print("\33[33mVocê corre e ataca o Zaos...\33[m")
                            sleep(1)
                            print("\33[33mZaos se defende com sua magia, porém se cansa...\33[m")
                            sleep(1)
                            print("\33[33mVocê aproveita e ataca ferozmente...\33[m")
                            sleep(1)
                            print("\33[33mE assim consegui derrotar Zaos...\33[m")
                            sleep(1)
                            print("\33[33mPARABÉNS VOCÊ SALVOU SUA AMADA AZILIA\33[m")
                            sleep(1)
                            print()
                            print(f"{emoji.emojize(':couple:',use_aliases=True)} \33[33mFim de jogo!!\33[m {emoji.emojize(':couplekiss:',use_aliases=True)}")
                        else:                           # ESPADA LONGA: VOCÊ AGUARDA O ATAQUE DELE, MORTE
                            sleep(1)
                            print("\33[33mZaos lhe ataca com muita intensidade e você perde sua espada...\33[m")
                            sleep(1)
                            print("\33[33mZaos volta a lhe atacar, você estar sem defesa...\33[m")
                            sleep(1)
                            print("\33[33mE assim lhe ferindo fatalmente...\33[m")
                            sleep(1)
                            print()
                            print("\33[37mVOCÊ MORREU!!\33[m")
                            sleep(1)
                            print()
                            gameover()
                    else:                     # ESPADA LONGA: VOCÊ PROCURA OUTRO CAMINHO
                        sleep(1)
                        print("\33[33mVocê encontra um caminho que é um corredor de pedras, estreito e escuro...\33[m")
                        sleep(1)
                        separa()
                        print("""\33[34m                         Oque você quer fazer?\33[m
                        
                        1 Atravessar o caminho.
                        2 Voltar para ponte.""")
                        sleep(1)
                        separa()
                        escolha=int(input("\33[34mQual sua opção? [1 ou 2]:\33[m "))
                        if escolha < 1 or escolha > 2:
                            while True:
                                escolha=int(input("\33[34mDigite novamente entre [1 ou 2]:\33[m "))
                                if escolha == 1 or escolha == 2 :
                                    break
                        separa()
                        if escolha == 1:           # ESPADA LONGA: VOCÊ ATRAVESSA O CAMINHO
                            sleep(1)
                            print("\33[33mVocê segui o caminho estreito sem ver nada a um palmo de distância...\33[m")
                            sleep(1)
                            print("\33[33mQuando você menos espera cai umas pedras atrás de você e tranca o caminho de volta...\33[m")
                            sleep(1)
                            print("\33[33mVocê continuar e cai em um precipício...\33[m")
                            sleep(1)
                            print("\33[37mVOCê MORREU!!\33[m")
                            sleep(1)
                            print()
                            gameover()
                        else:               # ESPADA LONGA: VOCÊ VOLTA PARA PONTE
                            sleep(1)
                            print("\33[33mVocê quando chega na metade da ponte...\33[m")
                            sleep(1)
                            print("\33[33mZaos aparece no final da ponte com Azilia amarrada ao lado...\33[m")
                            sleep(1)
                            print("\33[33mAcena dando chau e em seguida rompe a ponte...\33[m")
                            sleep(1)
                            print("\33[33mVocê caiu na lava...\33[m")
                            sleep(1)
                            print("\33[37mVOCÊ MORREU!!\33[m")
                            sleep(1)
                            print()
                            gameover()
                else:                                    # ESPADA LONGA: ESCOLHEU DESCANSO, MORTE!
                    sleep(1)
                    print("\33[33mVocê adormeceu...\33[m")
                    sleep(1)
                    print("\33[33mO bruxo Zaos soube que você conseguiu vencer a criatura...\33[m")
                    sleep(1)
                    print("\33[33mZaos foi ao seu encontro, viu você adormecido. Ele lhe envenena...\33[m")
                    sleep(1)
                    print("\33[37mVOCÊ MORREU!!\33[m")
                    sleep(1)
                    print()
                    gameover()
            elif op == 2:                         #ATACA
                sleep(1)
                print("\33[33mO crocodilo antercipou seu ataque e conseguiu retira de você sua espada...\33[m")
                sleep(1)
                print("\33[33mE assim lhe derruba e lhe ataca vuneravel...\33[m \33[37mVOCÊ MORREU!!\33[m")
                sleep(1)
                print()
                gameover()
    else:                            # NÃO ENFRENTAR O CROCODILO
        sleep(1)
        print("\33[33mVocê está num pantano, só tem lama e arvores podres. O crocodilo te alcança e te ataca brutalmente...\33[m")
        sleep(1)
        print("\33[33mTe derrubando e te da outro ataque mortal...\33[m")
        sleep(1)
        print("\33[37mVOCÊ MORREU...\33[m")
        sleep(1)
        print()
        gameover()
else:                             # FLORESTA DESCONHECIDA OP 2
    sleep(1)
    print("\33[33mVocê entra na floresta desconhecida...\33[m")
    sleep(1)
    print("\33[33mNo meio do caminho encontra um duende, que se apresenta como Efeutis...\33[m")
    sleep(1)
    separa()
    print("\33[34mEle oferece lhe mostrar um caminho mas curto, um atalho: Oque você faz ?\33[m")
    print()
    print("""    1 Acompanhar o duende.
    2 Ingnorar e continuar o caminho.""")
    separa()
    sleep(1)
    op1 = int(input("\33[34mOque você escolhe? 1 ou 2:\33[m "))
    if op1 < 1 or op1 > 2:
        while True:
            op1=int(input("\33[34mDigitou uma escolha invalida. Digite novamente [ 1 ou 2 ]:\33[m "))
            if op1 == 1 or op1 == 2:
                break
    separa()
    if op1 == 1:                         # FLORESTA DESCONHECIDA: AJUDA OU NÃO O DUENDE
        sleep(1)
        print("\33[33mEfieus lhe oferece realmente um caminho mas curto...\33[m ")
        sleep(1)
        print("\33[33mEm troca você tem que ajuda-lo a recuperar sua varinha magica.\33[m")
        separa()
        sleep(1)
        print("""               \33[34mOque você faz ?\33[m
        
        1 Você ajuda o duende.
        2 Você não ajuda e continua no desconhecido.""")
        separa()
        sleep(1)
        escolha=int(input("\33[34mQual sua escolha? [1 ou 2]:\33[m "))
        if escolha < 1 or escolha > 2:
            while True:
                escolha=int(input("\33[34mEscolha incorreta, digite novamente [1 ou 2]:\33[m "))
                if escolha == 1 or escolha == 2:
                    break
        separa()
        if escolha == 1:       # FLORESTA DESCONHECIDA: DECIDE AJUDA EFIEUTIS
            sleep(1)
            print("\33[33mO duende Efieutes te leva a uma casa no meio da floresta...\33[m")
            sleep(1)
            print("\33[33mLogo vocês observam uma senhora na frente...\33[m")
            print("\33[33mEfieutis comenta ' Essa senhora que robou minha varinha, ela é uma bruxa!!...'\33[m")
            sleep(1)
            print("\33[33mEle continua falando: ' E é irmã de Zaos o bruxo da montanha de fogo...'\33[m")
            sleep(1)
            print("\33[33mVocê não esperava por essa grande surpresa...\33[m")
            sleep(1)
            separa()
            print("""           \33[34mOque você quer fazer ?\33[m
            
            1 Atacar a bruxa.
            2 Esperar ela sair.""")
            op=int(input("\33[34mQual sua escolha? [1 ou 2]:\33[m "))
            if op < 1 or op > 2:
                while True:
                    op=int(input("\33[34mEscolha incorreta, digite novamente [1 ou 2]:\33[m "))
                    if op == 1 or op == 2:
                        break
            separa()
            if op == 1:               # FLORESTA DESCONHECIDA: ATACA A BRUXA
                sleep(1)
                print("\33[33mAo ataca-la ela tenta se defender mas o ataque foi muito rapido...\33[m")
                sleep(1)
                print("\33[33mA bruxa não conseguiu contra atacar...\33[m")
                sleep(1)
                print("\33[33mEfieutis fala ' Ainda bem que conseguimos ataca-lá, sem que ela nos notasse...'\33[m ")
                sleep(1)
                print("\33[33mEle continuou: ' Ela provavelmente nos mataria no primeiro ataque!...'\33[m ")
                sleep(1)
                print("\33[33mEfieutis mostra para a montanha de fogo...\33[m")
                sleep(1)
                print("\33[33mEfieutis fala sobre os pontos fracos de Zaos, e deixa você na entrada da montanaha de fogo...\33[m")
                sleep(1)
                print("\33[33mE lhe mostra o caminho que deve seguir. Pela ponte que por baixo passa o rio de lava...\33[m")
                sleep(1)
                print("\33[33mVocê passa e entra num salão, logo a frente ver sua amada amordaçada...\33[m")
                sleep(1)
                separa()
                print("""               \33[33mZaos aparece...\33[m
                \33[34mQual sua ação?\33[m
                
                1 Ataca ele.
                2 Espera reação dele.""")
                sleep(1)
                escolha=int(input("\33[34mQual sua escolha? [1 ou 2]:\33[m "))
                if escolha < 1 or escolha > 2:
                    while True:
                        escolha=int(input("\33[34mEscolha incorreta, digite novamente [1 ou 2]:\33[m "))
                        if escolha == 1 or escolha == 2:
                            break
                separa()
                if escolha == 1:            # FLORESTA DECONHECIDA: ATACA ZAOS
                    sleep(1)
                    print("\33[33mVocê se lembra do ponto fraco que Efieutis lhe alertou antes de entrar na motanha de fogo...\33[m")
                    sleep(1)
                    print("\33[33mEfieutis: 'Você o ataca e mesmo que tente se defenda não pare de ataca-lo, pois ele se cansa muito rapido...'\33[m ")
                    sleep(1)
                    print("\33[33mVocê faz oque o duende Efietis o aconselhou...\33[m")
                    sleep(1)
                    print("\33[33mNo terceiro ataque Zaos se rende...\33[m")
                    sleep(1)
                    print("\33[33mE com um ultimo ataque você parte ele ao meio...\33[m")
                    sleep(1)
                    print("\33[33mE assim derrotando O bruxo da montanha de fogo do continente Lascard...\33[m")
                    sleep(1)
                    print("\33[33mAssim salvando sua amada Azilia...\33[m")
                    sleep(1)
                    print()
                    print(f"{emoji.emojize(':couple:',use_aliases=True)} \33[33mFim de jogo!!\33[m {emoji.emojize(':couplekiss:',use_aliases=True)}")
                else:          # FLORESTA DESCONHECIDA: AGUARDA ATAQUE DE ZAOS
                    sleep(1)
                    print("\33[33mZaos ataca você e lhe surpreende...\33[m")
                    sleep(1)
                    print("\33[33mVocê não tem tempo para revidar e fica gravimente ferido...\33[m")
                    sleep(1)
                    print("\33[33mZaos então finaliza com um ataque fatal...\33[m")
                    sleep(1)
                    print("\33[37mVOCÊ MORREU!!\33[m")
                    sleep(1)
                    print()
                    gameover()
            else:            # FLORESTA DESCONHECIDA: AGUARDA A BRUXA SAIR
                sleep(1)
                print("\33[33mEla sai, e vocês entram na casa...\33[m")
                sleep(1)
                print("\33[33mEfieutis procura sua varinha, ao não acha-la se preocupa com a chegada da bruxa...\33[m")
                sleep(1)
                print("\33[33mEle logo em seguida propõe sair e aguardar outro momento...\33[m")
                sleep(1)
                print("\33[33mZelia aparece...\33[m")
                sleep(1)
                print("\33[33mSurpreende vocês e solta um ataque sobre vocês, não conseguiram ter reação...\33[m")
                sleep(1)
                print("\33[37mVOCÊ MORREU!!\33[m")
                sleep(1)
                print()
                gameover()
        else:          # FLORESTA DESCONHECIDA: DECIDE NÂO AJUDA EFIEUSTIS
            sleep(1)
            print("\33[33mVocê continua o caminho da floresta desconhecida...\33[m")
            sleep(1)
            print("\33[33mPor dias, meses e não mas a saida nem o duende...\33[m")
            sleep(1)
            print("\33[33mVocê se perdeu para sempre!!\33[m")
            sleep(1)
            print()
            gameover()
    else:                  # FLORESTA DESCONHECIDA: AJUDA OU NÃO A SENHORA
        sleep(1)
        print("\33[33mVocê continua na floresta desconhecida, sem qualquer ajuda...\33[m")
        sleep(1)
        print("\33[33mVocê está perdido e com fome...\33[m")
        sleep(1)
        print("\33[33mAparece uma senhora dizendo se chamar Azelia, e lhe oferece ajuda, comida e agua...\33[m")
        sleep(1)
        separa()
        print("""               \33[34mOque você faz ?\33[m
        
        1 Ignora e continua no desconhecido.
        2 Aceita a ajuda da senhora.""")
        separa()
        op=int(input("\33[34mQual sua escolha? [1 ou 2]:\33[m "))
        if op < 1 or op > 2:
            while True:
                op=int(input("\33[34mEscolha incorreta, digite novamente [1 ou 2]:\33[m "))
                if op == 1 or op == 2:
                    break
        separa()
        if op == 1:  # FLORESTA DESCONHECIDA: CONTINUA NO DESCONHECIDO
            sleep(1)
            print("\33[33mVocê continua no caminho da floresta desconhecida...\33[m")
            sleep(1)
            print("\33[33mUm certo momento a senhora reaparece...\33[m")
            sleep(1)
            print("\33[33mE se revela como bruxa e lhe ataca sem lhe da tempo de reação...\33[m")
            sleep(1)
            print("\33[37mVOCÊ MORREU!!\33[m")
            sleep(1)
            print()
            gameover()
        else:        # FLORESTA DESCONHECIDA: AJUDA A SENHORA
            sleep(1)
            print("\33[33mEla lhe leva para casa dela, no meio da floresta desconhecida...\33[m")
            sleep(1)
            print("\33[33mLa ela lhe da comida e agua. Você se satifaz, em seguida lhe da sono...\33[m")
            sleep(1)
            print("\33[33mDo nada você dormi, mesmo inconciente você escuta ela falando...\33[m")
            sleep(1)
            print("\33[33mZelia fala: ' Esse é seu fim, você ira dormi aqui para sempre!!! '\33[m")
            sleep(1)
            print()
            gameover()
separa()
sleep(1)
print("\33[33mProjeto\33[m - \33[32mGAME EM PYTHON\33[m")
sleep(1)
print("\33[33mDiciplica\33[m - \33[32mIntrodução a programação\33[m")
sleep(1)
print("\33[33mProfessor\33[m - \33[32mMarcelo Fernandes\33[m")
sleep(1)
print("""\33[33mAlunos\33[m - \33[32mEduardo Meireles
         Lucas Gabriel\33[m""")
