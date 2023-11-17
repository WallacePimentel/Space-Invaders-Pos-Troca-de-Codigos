from variaveis import *

#Função para criar os montros na lista e posicioná-los
def spawn_monstros(l_monstros):
    contador_y = 0
    for i in range(lin):
        linha = []
        l_monstros.append(linha)

    for i in range(lin):
        for j in range(col):
            monstro_novo = Sprite("monstro.png")
            l_monstros[i].append(monstro_novo)

    for i in range(lin):
        contador_x = 0
        for j in range(col):
            l_monstros[i][j].set_position(10 + pos_dif_x * contador_x, 10 + pos_dif_y * contador_y)
            contador_x += 1
        contador_y += 1

#Função para desenhar os monstros
def monstros_draw(l_monstros):
    for i in range(lin):
        for monstro in l_monstros[i]:
            monstro.draw()

#Função para a movimentação dos monstros
def monstros_move (l_monstros, velocidade_monstro):

    if l_monstros[0][col-1].x >= janela.width - l_monstros[0][col-1].width:
        velocidade_monstro *= -1

    if l_monstros[0][0].x <= 0:
        velocidade_monstro *= -1
        for i in range(lin):
            for monstro in l_monstros[i]:
                monstro.y += pos_dif_y

    for i in range(lin):
        for monstro in l_monstros[i]:
            monstro.x += velocidade_monstro * janela.delta_time()