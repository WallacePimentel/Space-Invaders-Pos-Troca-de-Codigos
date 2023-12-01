from inimigos import *
from variaveis import *
from arquivo_ranking import *


janela_jogo.set_title("Jogo")

nave.set_position((janela_jogo.width / 2) - (nave.width / 2), janela_jogo.height - (nave.height * 1.5))

spawn_monstros(l_monstros,verificador_lm)

while True:

    #------DRAWINGS------#
    background.draw()
    nave.draw()
    if (not start):
        janela_jogo.draw_text("Pressione ENTER para iniciar!", janela_jogo.width/2 - 170, janela_jogo.height/2, size=24, color=(255, 255, 255),
                              font_name="Arial", bold=True, italic=False)

    if (tecla.key_pressed("enter")):
        start = True
        vidas = 3

    if (start):
        #------MOVIMENTAÇÃO------#
        if tecla.key_pressed("left"):
            if nave.x > (nave.width):
                nave.x -= vx * janela_jogo.delta_time()

        if tecla.key_pressed("right"):
            if nave.x < (janela_jogo.width - nave.width * 2):
                nave.x += vx * janela_jogo.delta_time()

        # ----  TIRO    ----
        if tecla.key_pressed("space") and (cronometro > 0.2):
            fogo = Sprite("Game_Assets/fogo.png")
            fogo.set_position(nave.x + nave.width / 2 - fogo.width / 2, nave.y)
            tiros.append(fogo)
            cronometro = 0

        cronometro += janela_jogo.delta_time()

        for n in tiros:
            n.draw()
            n.y = n.y + velocidade_tiro * janela_jogo.delta_time()
            if n.y <= 0:
                del tiros[tiros.index(n)]

        #Detectando colisão entre tiro e monstro e apagando-os da lista caso ocorra
        if (tiros != []):
            for n in tiros:
                for i in range(5):
                    for monstro in l_monstros[i]:
                        if (monstro.x) <= n.x <= (monstro.x + monstro.width):
                            if (monstro.y) <= n.y <= (monstro.y + monstro.height):
                                index_atual_monstro = l_monstros[i].index(monstro)
                                if (verificador_lm[i][index_atual_monstro] == True):
                                    pontos += 1
                                    del tiros[tiros.index(n)]
                                    verificador_lm[i][index_atual_monstro] = False

        #----------TIROS-MONSTROS--------------------#
        cronometro_m += janela_jogo.delta_time()

        if (cronometro_m > 0.3):
            numero_random_linha = random.randint(0, 4)
            numero_random_coluna = random.randint(0, 9)
            if (verificador_lm[numero_random_linha][numero_random_coluna] == True):
                tiro_m = Sprite("Game_Assets/tiro_monstro.png")
                tiro_m.set_position(l_monstros[numero_random_linha][numero_random_coluna].x + nave.width / 2 - tiro_m.width / 2,
                                    l_monstros[numero_random_linha][numero_random_coluna].y)
                tiros_monstros.append(tiro_m)
                cronometro_m *= 0

        for n in tiros_monstros:
            n.draw()
            n.y = n.y + velocidade_tm * janela_jogo.delta_time()
            if ((n.y + n.height) >= janela_jogo.height):
                del tiros_monstros[tiros_monstros.index(n)]
            if ((nave.x <= n.x <= nave.x + nave.width) and (nave.y <= n.y <= nave.y + nave.height) and (invunerabilidade == False)):
                tomou_dano = True
                vidas -= 1
                del tiros_monstros[tiros_monstros.index(n)]

        #-------VERIFICANDO SE O PLAYER TOMOU DANO E CRIANDO A JANELA DE INVUNERABILIDADE------#
        if (tomou_dano):
            cronometro_dano += janela_jogo.delta_time()

        if (cronometro_dano > 0):
            invunerabilidade = True
            pos_x = nave.x
            pos_y = nave.y
            nave = Sprite("Game_Assets/nave_danificada.png")
            nave.set_position(pos_x,pos_y)
        if (cronometro_dano >= 3):
            invunerabilidade = False
            tomou_dano = False
            cronometro_dano = 0
            pos_x = nave.x
            pos_y = nave.y
            nave = Sprite("Game_Assets/nave.png")
            nave.set_position(pos_x, pos_y)

        for x in range(lin):
            for monstro in l_monstros[x]:
                if (monstro.y + monstro.height) >= nave.y:
                    vidas = 0


        monstro_direction = monstros_move(l_monstros,v_monstro,monstro_direction)

        #-----------VERIFICADOR-MORTE-PLAYER----------------#
        if (vidas == 0):
            start = False
            nome_atual = input("Digite o nome do player: ")
            data_atual = input("Digite a data atual: ")
            pontos_atual = pontos
            set_ranking("ranking.txt", pontos_atual, nome_atual, data_atual)
            pontos = 0
            l_monstros = []
            verificador_lm = []
            spawn_monstros(l_monstros,verificador_lm)

        monstros_draw(l_monstros)

    if tecla.key_pressed("esc"):
        janela_jogo.close()

    #------STRINGS-DOS-PONTOS-E-VIDAS-----#
    desenho_pontos = str(pontos)
    desenho_vidas = str(vidas)

    #-----DESENHOS-DE-TEXTO-NA-TELA-DE-JOGO------#
    janela_jogo.draw_text("Vidas", janela_jogo.width - 70 , janela_jogo.height - 140, size=24, color=(255, 255, 255), font_name="Arial", bold=True, italic=False)
    janela_jogo.draw_text(desenho_vidas, janela_jogo.width - 50 , janela_jogo.height - 100, size=50, color=(255, 255, 255), font_name="Arial", bold=True, italic=False)
    janela_jogo.draw_text("Pontos", 10, janela_jogo.height - 140, size=24, color=(255, 255, 255), font_name="Arial", bold=True, italic=False)
    janela_jogo.draw_text(desenho_pontos, 10, janela_jogo.height - 100, size=50, color=(255, 255, 255), font_name="Arial", bold=True, italic=False)

    janela_jogo.update()