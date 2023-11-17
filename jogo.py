from inimigos import *
from variaveis import *

janela.set_title("Jogo")

nave.set_position((janela.width / 2) - (nave.width / 2), janela.height - (nave.height * 1.5))

spawn_monstros(l_monstros)

while True:

    # ----  DRAWINGS    ----
    background.draw()
    nave.draw()
    monstros_draw(l_monstros)

    # ---- MOVIMENTAÇÃO ----
    if tecla.key_pressed("left"):
        if nave.x > (nave.width):
            nave.x -= vx * janela.delta_time()

    if tecla.key_pressed("right"):
        if nave.x < (janela.width - nave.width * 2):
            nave.x += vx * janela.delta_time()

    # ----  TIRO    ----
    if tecla.key_pressed("space") and (cronometro > 0.2):
        fogo = Sprite("fogo.png")
        fogo.set_position(nave.x + nave.width / 2 - fogo.width / 2, nave.y)
        tiros.append(fogo)
        cronometro = 0

    cronometro += janela.delta_time()

    for n in tiros:
        n.draw()
        n.y = n.y + velocidade_tiro * janela.delta_time()
        if n.y <= 0:
            del tiros[tiros.index(n)]

    #Detectando colisão entre tiro e monstro e apagando-os da lista caso ocorra
    if (tiros != []):
        for n in tiros:
            for i in range(5):
                for monstro in l_monstros[i]:
                    if (monstro.x) <= n.x <= (monstro.x + monstro.width):
                        if (monstro.y) <= n.y <= (monstro.y + monstro.height):
                            pontos += 1
                            del tiros[tiros.index(n)]
                            del l_monstros[i][l_monstros[i].index(monstro)]

    monstros_move(l_monstros,v_monstro)

    desenho_pontos = str(pontos)
    janela.draw_text(desenho_pontos, 10,janela.height - 100, size=50, color=(255,255,255), font_name="Arial", bold=True, italic=False)
    janela.update()