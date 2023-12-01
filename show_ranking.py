from variaveis_menu import *
from arquivo_ranking import *


def ranking_show():

    while True:

        janela_menu.set_background_color([0, 0, 0])
        fundo.draw()
        organizador_ranking('ranking.txt')
        lista = lista_ranking('ranking.txt')
        altura = 40
        contador = 0
        janela_menu.draw_text("Pontos - Nomes - Data", janela_menu.width / 2 - 180, janela_menu.height / 2 - 200, size=40,
                              color=(255, 255, 255), font_name="Arial", bold=True, italic=False)
        for i in lista:
            if (contador < 5):
                janela_menu.draw_text(i, janela_menu.width/2 - 180, janela_menu.height/2 - 140 + altura * contador, size=24,
                                      color=(255, 255, 255), font_name="Arial", bold=True, italic=False)
            contador += 1

        janela_menu.update()

        if tecla_menu.key_pressed("esc"):
            break