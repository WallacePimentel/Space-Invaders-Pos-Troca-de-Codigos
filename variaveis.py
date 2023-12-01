from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *

#Janela do Menu
janela_menu = Window(800,800)
start = False

#Janela de jogo
janela_jogo = Window(800, 800)

#Imagem de fundo
background = GameImage("Game_Assets/background_jogo.png")

#Sprite da nave e sua velocidades de x
nave = Sprite("Game_Assets/nave.png")
nave_danificada = Sprite("Game_Assets/nave_danificada.png")
vx = 350
vidas = 0
cronometro_dano = 0
invunerabilidade = False
tomou_dano = False
morreu = False

#Lista de tiros, sua velocidade padrão e o cronômetro de intervalo entre eles
tiros = []
velocidade_tiro = -1000
cronometro = 0

#Lista de tiros dos montros
tiros_monstros = []
velocidade_tm = 700
cronometro_m = 0

#Entrada do teclado
tecla = janela_jogo.get_keyboard()

#Entrada do mouse
click = janela_jogo.get_mouse()

#Seção monstros
l_monstros = []
verificador_lm = []
lin = 5
col = 10
v_monstro = 40
pos_dif_x = 72
pos_dif_y = 54
monstro_direction = 1

#Pontuação
pontos = 0

#Round
round = 0