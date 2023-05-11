#EP2 - Define Posições
import random

def define_posicoes(linha, coluna, orientacao, tamanho):
    resultado = [0]*tamanho
    for i in range(tamanho):
        if orientacao == "vertical":
            resultado[i] = [linha,coluna]
            linha += 1
        else:
            resultado[i] = [linha,coluna]
            coluna += 1
    return resultado

#EP2 - Preenche Frota
def preenche_frota (frota, nome_navio, linha, coluna, orientacao, tamanho):
    resultado=define_posicoes(linha, coluna, orientacao, tamanho)
    # frota={nome_navio: resultado}
    if nome_navio in frota:
        # armazenamento_navios[]=[resultado]
        frota[nome_navio].append(resultado)
    else:
        frota[nome_navio] = [resultado]

    return frota
    
#EP2 - Faz jogada
def faz_jogada(tabuleiro, linha, coluna):
    if tabuleiro[linha][coluna] == 1:
        tabuleiro[linha][coluna] = "X"
    elif tabuleiro[linha][coluna] == 0:
        tabuleiro[linha][coluna] = "-"
    return tabuleiro
    
#EP2 - Posiciona Frota
def posiciona_frota(frota):
    grid = [
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
      [0,0,0,0,0,0,0,0,0,0],
  ]
    for valores in frota.values():
        for posicao in valores:
            for linha_coluna in posicao:
                print(linha_coluna[1] )
                coluna=linha_coluna[1]
                linha=linha_coluna[0]
                grid[linha][coluna]= 1
    return grid

#EP2- Quantas embarcações afundadas?
def afundados(embarcacao,tabuleiro):
    nalfragio=0
    validando=0
    nome_navio=0
    for nome,navio in embarcacao.items():
        for localizacao in navio:
            for local in localizacao:
                if tabuleiro [local[0]] [local[1]]=='X':
                    validando=True
                else:
                    validando=False
                    break
            if validando == True:
                nalfragio+=1
                nome_navio=nome
    return nalfragio,nome_navio

#EP2 - Posição Válida
def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    posicao_desejada= define_posicoes(linha, coluna, orientacao, tamanho)
    retorno=0
    for posicao in posicao_desejada:
        if posicao[0] > 9 or posicao[0] <0:
            return False
        elif posicao[1] > 9 or posicao[1] <0:
            return False
    if frota == {}:
        return True
    for posicao in posicao_desejada:
        for barco in frota.values():
            for lista_maior_barco in barco :
                for lista in lista_maior_barco:
                    if posicao == lista:
                        retorno= False
                        return False
                    else:
                        retorno=True
                if retorno == False:
                    return retorno
    if retorno ==True:
        return retorno

#EP2 - Posicionando Frota
frota = {}
frotas = {
    "porta-aviões":{'quantidade':1,'tamanho':4},
    "navio-tanque":{'quantidade':2,'tamanho':3},
    "contratorpedeiro":{'quantidade':3,'tamanho':2},
    "submarino":{'quantidade':4,'tamanho':1},
}
lista=['0','1','2','3','4','5','6','7','8','9']
lista_orientacao=['1','2']
print('Bem Vindo ao Batalha Naval')
for navio, informacoes in frotas.items():
    for contador in range(0,informacoes['quantidade']):
        validando = False
        print('Insira as informações referentes ao navio {0} que possui tamanho {1}'.format(navio,informacoes['tamanho']))
        while validando != True:
            validando_linha=False
            while validando_linha!= True:
                linha = input('Qual Linha deseja posicionar seu navio : ')
                if linha in lista:
                    linha=int(linha)
                    validando_linha=True
            validando_coluna=False
            while validando_coluna!= True:
                coluna = input('Qual Linha deseja posicionar seu navio : ')
                if coluna in lista:
                    coluna=int(coluna)
                    validando_coluna=True
            
                if navio != 'submarino':
                    validando_orientacao=False    
                    while validando_orientacao != True:
                        orientacao = input('Orientação- Para ser vertical digite 1. Para ser horizontal digite 2: ')
                        if orientacao in lista_orientacao:
                            orientacao = int(orientacao)
                            validando_orientacao=True
                if orientacao == 1:
                    orientacao= 'vertical'
                if orientacao == 2:
                    orientacao= 'horizontal'
                validando = posicao_valida(frota, linha, coluna, orientacao, informacoes['tamanho'])
                if validando == False:
                    print('Esta posição não está válida!')
                    print('Insira as informações referentes ao navio {0} que possui tamanho {1}'.format(navio,informacoes['tamanho']))
        frota=preenche_frota(frota, navio, linha, coluna, orientacao, informacoes['tamanho'])


#EP 2 - Jogadas do jogador e jogadas do oponente




def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '____      ____\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_oponente=posiciona_frota(frota_oponente)

tabuleiro_jogador=posiciona_frota(frota)

posicoes=[]
posicoes_oponente=[]
jogando=True 
print('Agora que já posicionou seus navios, ATAQUE!')
while jogando:
    escolhas=True
    while escolhas:
        tabuleiro=monta_tabuleiros(tabuleiro_jogador,tabuleiro_oponente)
        print(tabuleiro)
        validando_ataque_linha=False
        while validando_ataque_linha != True:
            ataque_linha=input('Qual linha deseja atacar? ')
            if ataque_linha in lista:
                ataque_linha=int(ataque_linha)
                validando_ataque_linha=True
            else:
                print('Linha inválida!')

        validando_ataque_coluna=False
        while validando_ataque_coluna != True:
            ataque_coluna=input('Qual coluna deseja atacar? ')
            if ataque_coluna in lista:
                ataque_coluna=int(ataque_coluna)
                validando_ataque_coluna=True
            else:
                print('Coluna inválida!')
        posicao=[ataque_linha,ataque_coluna]
        if posicao not in posicoes:
            posicoes.append(posicao)
            tabuleiro_oponente=faz_jogada(tabuleiro_oponente,ataque_linha,ataque_coluna)
            jogadas_oponente=True
            while jogadas_oponente:
                ataque_linha_oponente=random.randint(0,9)
                ataque_coluna_oponente=random.randint(0,9)
                posicao_op=[ataque_linha_oponente,ataque_coluna_oponente]
                if posicao_op not in posicoes_oponente:
                    print('Seu oponente está atacando na linha {0} e coluna {1}'.format(ataque_linha_oponente,ataque_coluna_oponente))
                    posicoes_oponente.append(posicao_op)
                    tabuleiro_jogador=faz_jogada(tabuleiro_jogador,ataque_linha_oponente,ataque_coluna_oponente)
                    jogadas_oponente=False
                    escolhas=False
                    itens_jogador=afundados(frota_oponente,tabuleiro_oponente)
                    rodando=itens_jogador[0]
                    nome_afundados_jogador=itens_jogador[1]
    
                    
                    itens_oponente=afundados(frota,tabuleiro_jogador)
                    rodando_oponente=itens_oponente[0]
                    nome_afundados_oponente=itens_oponente[1]

                    
        else:
            print('A posição linha {0} e coluna {1} já foi informada anteriormente!'.format(ataque_linha,ataque_coluna))
            escolhas=False
            
    if rodando == 10:
        jogando=False
        escolhas=False
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        break
    else:
        if nome_afundados_jogador !=0:
            print(f'Você afundou o navio {nome_afundados_jogador}')
        print(f'Com esse faltam {10-rodando} navios')
    if rodando_oponente == 10:
        jogando=False
        escolhas=False
        print('Xi! O oponente derrubou toda a sua frota =(')
        break
    else:
        if nome_afundados_oponente !=0:
            print(f'Seu oponente afundou o navio {nome_afundados_oponente}')
        print(f'Seu oponente precisa afundar mais {10-rodando_oponente} navios')
