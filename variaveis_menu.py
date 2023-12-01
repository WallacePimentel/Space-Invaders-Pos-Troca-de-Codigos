from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *

#------JANELA-MENU------#
janela_menu = Window(800,800)
janela_menu.set_title("Space Invaders - Wallace Pimentel")

#------FUNDO------#
fundo = GameImage("Game_Assets/background_menu.png")

#------MOUSE-E-TECLADO------#
click_menu = janela_menu.get_mouse()
tecla_menu = janela_menu.get_keyboard()

#------BOTÕES-MENU------#
jogar = Sprite("Game_Assets/botoes_menu/bot_jogar.png")
jogar_p = Sprite("Game_Assets/botoes_menu/bot_jogar_pressed.png")
jogar.set_position(janela_menu.width/2 - jogar.width/2,janela_menu.height/ 2 - 230)
jogar_p.set_position(janela_menu.width/2 - jogar_p.width/2,janela_menu.height/ 2 - 230)

dificuldade = Sprite("Game_Assets/botoes_menu/bot_dificuldade.png")
dificuldade_p = Sprite("Game_Assets/botoes_menu/bot_dificuldade_pressed.png")
dificuldade.set_position(janela_menu.width/2 - dificuldade.width/2,janela_menu.height / 2 - 90)
dificuldade_p.set_position(janela_menu.width/2 - dificuldade_p.width/2,janela_menu.height / 2 - 90)

ranking = Sprite("Game_Assets/botoes_menu/bot_ranking.png")
ranking_p = Sprite("Game_Assets/botoes_menu/bot_ranking_pressed.png")
ranking.set_position(janela_menu.width/2 - ranking.width/2,janela_menu.height / 2 + 50)
ranking_p.set_position(janela_menu.width/2 - ranking_p.width/2,janela_menu.height / 2 + 50)

sair = Sprite("Game_Assets/botoes_menu/bot_sair.png")
sair_p = Sprite("Game_Assets/botoes_menu/bot_sair_pressed.png")
sair.set_position(janela_menu.width/2 - sair.width/2,janela_menu.height / 2 + 190)
sair_p.set_position(janela_menu.width/2 - sair_p.width/2,janela_menu.height / 2 + 190)

dificil = Sprite("Game_Assets/botoes_menu/bot_dificil.png")
dificil_p = Sprite("Game_Assets/botoes_menu/bot_dificil_pressed.png")
dificil.set_position(janela_menu.width / 2 - dificil.width / 2, janela_menu.height / 2 + 150)
dificil_p.set_position(janela_menu.width / 2 - dificil_p.width / 2, janela_menu.height / 2 + 150)

medio = Sprite("Game_Assets/botoes_menu/bot_medio.png")
medio_p = Sprite("Game_Assets/botoes_menu/bot_medio_pressed.png")
medio.set_position(janela_menu.width/2 - medio.width/2,janela_menu.height/2)
medio_p.set_position(janela_menu.width/2 - medio_p.width/2,janela_menu.height/2)

facil = Sprite("Game_Assets/botoes_menu/bot_facil.png")
facil_p = Sprite("Game_Assets/botoes_menu/bot_facil_pressed.png")
facil.set_position(janela_menu.width/2 - facil.width/2,janela_menu.height/2 - 150)
facil_p.set_position(janela_menu.width/2 - facil_p.width/2,janela_menu.height/2 - 150)