# Dessoft-ep2
#EP2 "define posicoes"
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

#EP2 "preenche frota (preenche frota + define posicoes)"
def preenche_frota (frota, nome_navio, linha, coluna, orientacao, tamanho):
    resultado=define_posicoes(linha, coluna, orientacao, tamanho)
    # frota={nome_navio: resultado}
    if nome_navio in frota:
        # armazenamento_navios[]=[resultado]
        frota[nome_navio].append(resultado)
    else:
        frota[nome_navio] = [resultado]

    return frota
    
#EP2 "faz jogada (código solo)"
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
    for navio in embarcacao.values():
        for localizacao in navio:
            for local in localizacao:
                if tabuleiro [local[0]] [local[1]]=='X':
                    validando=True
                else:
                    validando=False
                    break
            if validando == True:
                nalfragio+=1
    return nalfragio

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
frota={}
frotas = {
    "porta-aviões":{'quantidade':1,'tamanho':4},
    "navio-tanque":{'quantidade':2,'tamanho':3},
    "contratorpedeiro":{'quantidade':3,'tamanho':2},
    "submarino":{'quantidade':4,'tamanho':1},
}

for navio,informacoes in frotas.items():
    for contador in range(0,informacoes['quantidade']):
        validando=False
        print('Insira as informações referentes ao navio {0} que possui tamanho {1}'.format(navio,informacoes['tamanho']))
        while validando!= True:
            linha = int(input('Linha: '))
            coluna = int(input('Coluna: '))
            if navio !='submarino':
                orientacao = int(input('Orientação- Para ser vertical digite 1. Para ser horizontal digite 2: '))
            if orientacao == 1:
                orientacao='vertical'
            if orientacao == 2:
                orientacao='horizontal'
            validando=posicao_valida(frota, linha, coluna, orientacao, informacoes['tamanho'])
            if validando == False:
                print('Esta posição não está válida!')
                print('Insira as informações referentes ao navio {0} que possui tamanho {1}'.format(navio,informacoes['tamanho']))
        frota=preenche_frota(frota, navio, linha, coluna, orientacao, informacoes['tamanho'])

print(frota)