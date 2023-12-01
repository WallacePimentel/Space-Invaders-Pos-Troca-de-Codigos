from variaveis_menu import *


def dificuldade_select():
    delay = 0

    while True:

        janela_menu.set_background_color([0, 0, 0])
        fundo.draw()

        facil.draw()
        if click_menu.is_over_object(facil):
            facil_p.draw()
            if click_menu.is_button_pressed(1):
                return 1

        medio.draw()
        if (click_menu.is_over_object(medio) and delay >= 0.5):
            medio_p.draw()
            if click_menu.is_button_pressed(1):
                return 2

        dificil.draw()
        if click_menu.is_over_object(dificil):
            dificil_p.draw()
            if click_menu.is_button_pressed(1):
                return 3

        janela_menu.update()
        if delay <= 1:
            delay = delay + 1 * janela_menu.delta_time()

        if tecla_menu.key_pressed("esc"):
            break