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
