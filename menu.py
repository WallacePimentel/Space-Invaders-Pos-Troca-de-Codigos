from PPlay.window import *
from PPlay.sprite import *
from variaveis_menu import *
from select_dificuldade import dificuldade_select
from show_ranking import ranking_show

def menu():
    delay = 1
    while True:
        janela_menu.set_background_color([0,0,0])
        fundo.draw()

        jogar.draw()
        if click_menu.is_over_object(jogar):
            jogar_p.draw()
            if click_menu.is_button_pressed(1) and delay >= 0.5:
                delay = 0
                return True

        dificuldade.draw()

        if (click_menu.is_over_object(dificuldade) and delay >= 0.5):
            dificuldade_p.draw()
            if click_menu.is_button_pressed(1):
                dificuldade_atual = dificuldade_select()
                delay = 0

        ranking.draw()
        if (click_menu.is_over_object(ranking)) and delay >= 0.5:
            ranking_p.draw()
            if click_menu.is_button_pressed(1):
                ranking_show()
                delay = 0


        sair.draw()

        if (click_menu.is_over_object(sair) and delay >= 0.5):
            sair_p.draw()
            if click_menu.is_button_pressed(1):
                return False

        if delay <= 1:
            delay = delay + 1 * janela_menu.delta_time()
        janela_menu.update()