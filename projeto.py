import sys
def formarMapa():
    mapa = [
        ["| torre1   ", "x Galeria ⬇", "|   Cozinha ⬇", "x  Armazem   ", "|  Quarto       "],
        ["| Entrada  ", "x Pátio  ⬍ ", "x  Trono   ⬆ ", "x Corredor1 ⬇", "l  Aposentos    "], 
        ["| torre2   ", "x Jardim ⬍ ", "x  Cemitério ", "x  Capela ⬍  ", "|       ?       "],
        ["| Armas    ", "x Guerra ⬆ ", "|  Tesouro   ", "x Corredor2 ⬆", "x Laboratório  ⬇"],
        ["x Saída    ", "x Esgotos  ", "x  Esgotos   ", "x  Esgotos   ", "x  Esgotos      "]
        ]
    return mapa
    
def printarMapa(mapa):
    for i in range (0, len(mapa)):
        print("+------------+------------+--------------+--------------+-----------------+")
        for j in range (0, len(mapa[0])):
          print(mapa[i][j], end = "  ")
        print("|")
    print("+------------+------------+--------------+--------------+-----------------+")


def barreirasLaterais(posicao, x, y):
    return posicao[1] + y >= 0 and posicao[1] + y <= 4 and posicao[0] + x >=0 and posicao[0] + x <= 4

def verificarPassagensD(mapa, posicao, x, y):
    try:
        return 'x' in mapa[posicao[0] + x][posicao[1] + y]
    except:
        print("Está fora de área!")

def verificarPassagensA(mapa, posicao, x, y):
    try:
        return not('|' in mapa[posicao[0]][posicao[1]])
    except:
        print("Está fora de área!")
    
def verificarPassagensW(mapa, posicao, x, y):
    try:
        if '⬍' in mapa[posicao[0]][posicao[1]]:
            return True
        elif "⬆" in mapa[posicao[0]][posicao[1]]:
            return True
        else:
            return False
    except:
        print("Está fora de área!")

def verificarPassagensS(mapa, posicao, x, y):
    try: 
        if '⬍' in mapa[posicao[0]][posicao[1]]:
            return True
        elif "⬇" in mapa[posicao[0]][posicao[1]]:
            return True
        else:
            return False
    except:
        print("Está fora de área!")

def TesteAtribuicoesDeMovimento(mapa, x, y):
    try:
        if (barreirasLaterais(posicao, x, y)):
            valida = mapa[posicao[0] + x][posicao[1] + y]
            posicao[0] += x
            posicao[1] += y
            return valida
        else:
            print("Esse caminho é inválido!")
            return mapa[posicao[0]][posicao[1]]
    except:
        print("Movimentação inválida!")

def movimentarPersonagem(movimento, mapa, posicao, local):
    if (movimento == "d"):
        if verificarPassagensD(mapa, posicao, 0 , 1):
           local = TesteAtribuicoesDeMovimento(mapa, 0, 1)
        else:
            print("Isso é uma parede!")
    elif (movimento == "s"):
        if verificarPassagensS(mapa, posicao, 1, 0):
            local = TesteAtribuicoesDeMovimento(mapa, 1, 0)
        else:
            print("Isso é uma parede!")
    elif (movimento == "a"):
        if verificarPassagensA(mapa, posicao, 0, -1):
            local = TesteAtribuicoesDeMovimento(mapa, 0, -1)
        else:
            print("Isso é uma parede!")
    elif (movimento == "w"):
        if verificarPassagensW(mapa, posicao, -1, 0):
            local = TesteAtribuicoesDeMovimento(mapa, -1, 0)
        else:
            print("Isso é uma parede!")
    else:
        print("Valor inválido!")
    
    return local

def opcao1(posicao, local, mapa):
    movimento = input("Informe o movimento que deseja fazer (wasd, q para sair): ")
    while (movimento != "q"):
        local = movimentarPersonagem(movimento, mapa, posicao, local)
        printarMapa(mapa)
        print("Legenda: x = porta aberta, | = parede, setas = subir e descer")
        print()
        print("Local atual: [", local[2:len(local) + 1], "]")
        movimento = input("Informe o movimento que deseja fazer (wasd, q para sair): ")
    return local


def criarInventario():
    inventario = ["espada brega: 5 dmg"]
    return inventario

def adicionarAoInventario(inventario, item):
    inventario.append(item)
    print("          ITEM ADQUIRIDO: ", item)

def opcao2(inventario):
    print()
    print ("Seu inventário: ", inventario)


def adicionarMissao(missoes, msg):
    missoes.append(msg)
    print("          UMA NOVA MISSÃO FOI ADICIONADA: ", msg)
    print()

def concluirMissao(missoes, num):
    print("          MISSÃO CONCLUÍDA: ", missoes[num])
    missoes[num] += (" (feito!) ")
    print()

def opcao4 (missoes):
    print("-------------------------------------")
    for i in range (0, len(missoes)):
        print("★ Missão ", i + 1, ": ", missoes[i])

def descrever (local, missoes):
    # os mais importantes primeiro:
    print("-----------------------------------------------------------------------------------------------------------------------------------------")
    if (local == "x Laboratório  ⬇" and not("(feito!)") in missoes[0]):
        print("Descrção: Um laboratório extremamente bagunçado. Na parede mais distante, parece ter um quadro com a sigla de alguns elmentos químicos.")
        print("          Olhando de mais perto, você percebe que faltam alguns símbolos: Carbono (C), Iodo(I), Érbio(E), Nitrogênio(N) e Arsênio(A). ")
        print("          Assim como seu pai lhe disse, você deve recuperá-los ao longo do castelo para desbloquear a sala e salvar o seu pai de lá.")
        print("          (vai saber como ele se meteu lá dentro)")

        print()

        adicionarMissao(missoes, "Carbono na tesouraria")
        adicionarMissao(missoes, "Iodo na cozinha")
        adicionarMissao(missoes, "Érbio na galeria de arte")
        adicionarMissao(missoes, "Nitrogênio no jardim")
        adicionarMissao(missoes, "Arsênio na sala de armas")
        concluirMissao(missoes, 0)
    elif (local == "|   Cozinha ⬇"):
        print("Descrição: A cozinha real está bem organizada, porém com um buraco no meio dela, ao lado do buraco, uma placa dizendo 'Me alimente' ")
    
    elif (local == "x Galeria ⬇"):
        print("Um lugar extremamente branco está na sua frente. Nas paredes, alguns quadros que registram os grandes feitos do castelo. Quadros estes")
        print("que ambientam a sala em conjunto com alguns vasos de cor rosada.")
    elif (local == "x  Cemitério "):
        print("Lápides monumentais se estendem por aqui. Além disso, uma pá recém usada está apoiada na lápide mais próxima.")
    elif (local == "x Jardim ⬍ "):
        print("Um belo jardim está a sua frente, composto por flores de todos os tipos. No entanto, há um conjunto grande de rosas recém plantadas")
    elif (local == "| Armas    "):
        print("Estranhamente, a sala de armas estava vazia: nem uma ferramenta mortal estava presente. Porém, 3 garrafas de vidro estão sobrepostas")
        print("lado a lado. Ao lado da garrafa ao extremo direito, há um placa dizendo: uma está com um líquido mágico, as outras, com veneno mortal.")
        print("Escolha sabiamente com base nessa pergunta: Embora cercado de solitários, estou sempre acompanhado. Quem eu sou?")
    elif (local == "|  Tesouro   "):
        print("Goblins estão comendo os tesouros do castelo! Eles te olham. O que você faz?")
    elif (local == "x  Armazem   "):
        print("O armazem está cheio de comidas deliciosas. No meio delas, há um pódio com uma comida aparentemente deliciosa")
    else:
        print("Não há nada muito importante para se ver aqui.")

def toFora():
    print("Os goblins não vão deixar você fugir!")

def alocar(missoes, inventario, mapa):
    if ("C" in inventario and "I" in inventario and "E" in inventario and "N" in inventario and "A" in inventario):
        print("===========================")
        print("Salvou o seu pai!!!!!!")
        print("===========================")
        mapa[2][4] = "|    sala f ⬇   "
        mapa[3][4] = "x Laboratório  ⬍"
    else:
        print("Você precisa ter todos os símbolos!")

def atacarGoblins(missoes, inventario):
    print("-----------------------------------------------------------------------------------------------------------------------------------------")
    print("Os goblins são mortos e suas barrigas são rasgadas ao meio, deixando cair vários diamantes de suas estranhas! Quando você se aproxima para")
    print("examinar seus orgãos, você encontra o símbolo do carbono na barriga do primeiro goblin")
    print()

    concluirMissao(missoes, 1)
    adicionarAoInventario(inventario, "C")

def examinarQuadros():
    ("-----------------------------------------------------------------------------------------------------------------------------------------")
    print("Os quadros possuem algumas letras pequenas nas suas molduras. Elas dizem: os vasos são o tesouro artístico do castelo, feitos da cores")
    print("intensas do Érbio...")

def quebrarTudo(missoes, inventario):
    ("-----------------------------------------------------------------------------------------------------------------------------------------")
    print("Com a sua espada brega, você quebra as obras de artes caríssimas uma a uma. Dentro de um dos vasos, você encontra o símbolo de Érbio!")
    print()

    adicionarAoInventario(inventario, "E")
    concluirMissao(missoes, 3)

def jogarComidaNoBuraco(missoes, inventario):
    ("-------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Você arremessa o rango que você obteve. Depois de alguns barulhos estranhos vindos do fundo do buraco, o símbolo do Iodo é jogado pra fora!")
    print()

    adicionarAoInventario(inventario, "I")
    concluirMissao(missoes, 2)

def cavarBuraco(missoes, inventario):
    ("-----------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Ao terminar o trabalho árduo de cavar aquele monte de terra suspeitos, você encontra um esqueleto humano recém decomposto segurando o símbolo do nitrogênio!")
    print()

    adicionarAoInventario(inventario, "N")
    concluirMissao(missoes, 4)

def beberFrasco(missoes, inventario):
    ("-------------------------------------------------------------------------------------------------------------------------------------------------")
    print("Quando você bebe o segundo frasco, uma caixa que estava invisível se revela na sua frente. Em cima dela está o símbolo do Arsênio!")
    print()

    adicionarAoInventario(inventario, "A")
    concluirMissao(missoes, 5)

def elementoAcoes(local, missoes, inventario, mapa):
    if "(feito!)" in missoes[0]:
        # Todas as ações são feitas após a visita do laboratório
        if local == "x Laboratório  ⬇":
            elementoAcao = int(input("1. colocar elementos no quadro \n 2. sair do modo de ação \n Resposta: "))
            if elementoAcao == 1:
                alocar(missoes, inventario, mapa)
        elif local == "|  Tesouro   ":
            try:
                elementoAcao = int(input("1. Ataco eles com a minha espada brega! \n 2. Tô fora! \n 3. sair do modo de ação \n Resposta: "))
                if elementoAcao == 1:
                    atacarGoblins(missoes, inventario)
                elif elementoAcao == 2:
                    toFora()
                else:
                    print("Valor inválido!")
            except:
                print("Valor inválido!")
        elif local == "x Galeria ⬇":
            try:
                elementoAcao = int(input("1. Examino os quadros e os vasos \n 2. Ignoro tudo. \n 3. Quebro tudo! \n 4. sair do modo de ação \n Respota: "))
                if elementoAcao == 1:
                    lido = examinarQuadros()
                elif elementoAcao == 2:
                    print("Você ignora tudo.")
                elif elementoAcao == 3:
                    quebrarTudo(missoes, inventario)
                else:
                    print("Valor inválido!")
            except:
                print("Valor inválido!")

        elif local == "|   Cozinha ⬇":
            try:
                print("1. jogar comida no buraco.")
                print("2. pular no buraco.")
                elementoAcao = int(input("Resposta: "))

                if elementoAcao == 1:
                    if ("Rango brabo" in inventario):
                        jogarComidaNoBuraco(missoes, inventario)
                    elif ("Comida estranha" in inventario):
                        print("-----------------------------------------------------------------------------------")
                        print("Depois de um tempo, o buraco cospe a Comida estranha na sua cara")
                    else:
                        print("-----------------------------------------------------------------------------------")
                        print("Você não tem nada comestível para jogar no buraco, talvez tenha algo no armazem...")
                elif elementoAcao == 2:
                    print("-----------------------------------------------------------------------------------")
                    print("Por que você faria isso?")
                else:
                    print("Valor inválido!")
            except:
                print("Valor inválido!")

        elif local == "x  Armazem   ":
            try:
                print("1. pegar Rango brabo")
                print("2. pegar comida estranha")
                elementoAcao = int(input("Resposta: "))
                if (elementoAcao == 1):
                    adicionarAoInventario(inventario, "Rango brabo")
                elif (elementoAcao == 2):
                    adicionarAoInventario(inventario, "Comida estranha")
                else:
                    print("inválido!")
            except:
                print("Valor inválido!")

        elif local == "| Armas    ":
            try:
                print("(Recomendável observar a sala antes)")
                print("1. Tomar o líquido do primeiro frasco. ")
                print("2. Tomar o líquido do segundo fraco.")
                print("3. Tomar o líquido do terceiro frasco.")
                elementoAcao = int(input("Resposta: "))

                if (elementoAcao == 1 or elementoAcao == 3):
                    print("Você morreu!")
                    sys.exit()
                elif (elementoAcao == 2):
                    beberFrasco(missoes, inventario)
                else:
                    print("Valor inválido!")
            except:
                print("Valor inválido!")

        elif local == "x  Cemitério ":
            try:
                print("1. pegar Pá usada")
                elementoAcao = int(input("Resposta: "))
                if (elementoAcao == 1):
                    adicionarAoInventario(inventario, "Pá usada")
                else:
                    print("inválido!")
            except:
                print("Valor inválido!")
        elif local == "x Jardim ⬍ ":
            try:
                print("1. Cavar debaixo das roseiras")
                print("2. Continuar explorando.")
                elementoAcao = int(input("Resposta: "))

                if elementoAcao == 1:
                    if ("Pá usada" in inventario):
                        cavarBuraco(missoes, inventario)
                    else:
                        print("-----------------------------------------------------------------------------------")
                        print("Você não tem nada útil para cavar um buraco, talvez tenha algo no cemitério...")
                elif elementoAcao == 2:
                    print("-----------------------------------------------------------------------------------")
                    print("Você continua explorando")
                else:
                    print("Valor inválido!")
            except:
                print("Valor inválido!")

        elif local == mapa[2][4] == "|    sala f ⬇   ":
            try: 
                print("1. Pegar A ARMA SECRETA")
                elementoAcao = int(input("Resposta: "))
                if elementoAcao == 1:
                    adicionarAoInventario(inventario, "3-OITÃO")
                else:
                    print("Valor inválido")
            except: 
                print("Valor inválido!")
        else:
            print("Nada muito surpreendente por aqui para interagir")


def interagir(local, missoes, inventario, mapa):
    print("O que gostaria de fazer nesse lugar? (a, b): ")
    print()
    print("a. observá-lo")
    if len(missoes) > 1:
        print("b. Ações no lugar ")  

    resposta = input("Resposta: ")
    if (resposta == 'a'):
        descrever(local, missoes)
    elif (resposta == 'b' and len(missoes) > 1):
        elementoAcoes(local, missoes, inventario, mapa)
    else:
        print("valor inválido!")
    # opcoesExtras(local, missoes)

missoes = ["Vá até o labolatório"]
mapa = formarMapa()
posicao = [1, 0]
local = mapa[posicao[0]][posicao[1]]
inventario = criarInventario()
while (mapa[2][4] != "|    sala f ⬇   "):
    printarMapa(mapa)
    print("Legenda: x = porta aberta, | = parede, setas = subir e descer")
    print()
    print("Local atual: [", local[2:len(local) + 1], "]")
    print("O que deseja fazer? (1, 2, 3, 4, 5): ")
    valor = int(input("  1. Andar \n 2.Inventário \n 3. Interagir \n 4. Missões \n 5. Sair do jogo \n input: "))
    if (valor == 1): 
        local = opcao1(posicao, local, mapa)
    if (valor == 2):
        opcao2(inventario)
    if (valor == 3):
        interagir(local, missoes, inventario, mapa)
    if (valor == 4):
        opcao4(missoes)
    if (valor == 5):
        sys.exit()
print("Fim de jogo!")
