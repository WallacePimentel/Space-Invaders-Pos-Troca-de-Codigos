from variaveis import *
import random

#Função para criar os montros na lista e posicioná-los
def spawn_monstros(l_monstros,verificador_lm):
    contador_y = 0
    for i in range(lin):
        linha = []
        l_monstros.append(linha)

    for i in range(lin):
        for j in range(col):
            monstro_novo = Sprite("Game_Assets/monstro.png")
            l_monstros[i].append(monstro_novo)

    for i in range(lin):
        contador_x = 0
        for j in range(col):
            l_monstros[i][j].set_position(10 + pos_dif_x * contador_x, 10 + pos_dif_y * contador_y)
            contador_x += 1
        contador_y += 1

    for i in range(lin):
        linha = []
        verificador_lm.append(linha)

    for i in range(lin):
        for j in range(col):
            booleano = True
            verificador_lm[i].append(booleano)
    


#Função para desenhar os monstros
def monstros_draw(l_monstros):
    for i in range(lin):
        for j in range(col):
            if verificador_lm[i][j] == True:
                l_monstros[i][j].draw()

#Função para a movimentação dos monstros

def monstros_move(l_monstros, velocidade_monstro, monstro_direction):
    print(monstro_direction)
    for linha in l_monstros:
        for monstro in linha:
            if (monstro.x + monstro.width) > janela_jogo.width and monstro_direction > 0:
                monstro_direction *= -1
                for linha in l_monstros:
                    for monstro in linha:
                        monstro.y += 20
            if monstro.x < 0 and monstro_direction < 0:
                monstro_direction *= -1
                for linha in l_monstros:
                    for monstro in linha:
                        monstro.y += 20

            monstro.x += (velocidade_monstro * monstro_direction) * janela_jogo.delta_time() 
    return monstro_direction
            

def cronometro_tiro(l_monstros,tiros_monstros,cronometro_m):
    if (cronometro_m > 1):
        numero_random_linha = random.randint(0, 4)
        numero_random_coluna = random.randint(0, 9)
        tiro_m = Sprite("Game_Assets/tiro_monstro.png")
        tiro_m.set_position(l_monstros[numero_random_linha][numero_random_coluna].x + nave.width / 2 - tiro_m.width / 2, l_monstros[numero_random_linha][numero_random_coluna].y)
        tiros_monstros.append(tiro_m)
        return 0