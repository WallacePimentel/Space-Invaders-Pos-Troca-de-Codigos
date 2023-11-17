from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *

#Janela de jogo
janela = Window(800, 800)

#Imagem de fundo
background = GameImage("background_jogo.png")

#Sprite da nave e sua velocidades de x
nave = Sprite("nave.png")
vx = 350

#Lista de tiros, sua velocidade padrão e o cronômetro de intervalo entre eles
tiros = []
velocidade_tiro = -1000
cronometro = 0

#Entrada do teclado
tecla = janela.get_keyboard()

#Entrada do mouse
click = janela.get_mouse()

#Seção monstros
l_monstros = []
lin = 5
col = 10
v_monstro = 40
pos_dif_x = 72
pos_dif_y = 54

#Pontuação
pontos = 0
