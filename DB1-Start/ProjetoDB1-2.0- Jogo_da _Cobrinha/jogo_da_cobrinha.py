import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

largura = 640
altura = 420

x_cobra = largura/2
y_cobra = altura/2

velocidade = 10
x_controle = velocidade
y_controle = 0

x_maca = randint(50,600)
y_maca = randint(40,400)

# Define as configurações de texto. 
fonte = pygame.font.SysFont('arial', 20, True, False)
pontos = 0

# Configura som de fundo.
pygame.mixer.music.set_volume(0.05)
musica_de_fundo = pygame.mixer.music.load('ProjetoDB1-2.0- Jogo_da _Cobrinha/a1.mp3')
pygame.mixer.music.play(-1)

som_colisao = pygame.mixer.Sound('ProjetoDB1-2.0- Jogo_da _Cobrinha/a2.wav')
#-------------------------CRIANDO TELA--------------------------#

tela = pygame.display.set_mode((largura,altura))

relogio = pygame.time.Clock()

pygame.display.set_caption("Jogo")

tela.fill((200,200,200))

morreu = False

lista_corpo = []

comprimento = 5

def aumenta_cobra(lista_cobra):
    for coordenadas in lista_cobra:
        pygame.draw.rect(tela, (0,255,0), (coordenadas[0], coordenadas[1], 20, 20)) 

def reiniciar_jogo():
    global pontos, comprimento, x_cobra, y_cobra, lissta_cobra, lista_corpo, x_maca, y_maca, morreu

    pontos = 0
    comprimento = 5
    x_cobra = largura/2
    y_cobra = altura/2
    lista_cobra = []
    lista_corpo = []
    x_maca = randint(50,600)
    y_maca = randint(40,400)
    morreu = False

#---------------------------------------------------#
while True:
    
    relogio.tick(30)

    tela.fill((200,200,200))

    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (0,0,0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

#-------------------------OBJETOS--------------------------#

    cobra = pygame.draw.rect(tela,(0,255,0), (x_cobra,y_cobra,20,20))
    maca = pygame.draw.rect(tela,(255,0,0), (x_maca,y_maca,20,20))

#---------------------------------------------------#        
            
    if event.type == KEYDOWN:
        if event.key == K_LEFT :
            if x_controle == velocidade:
                pass
            else:
                x_controle = -velocidade
                y_controle = 0
        if event.key == K_RIGHT :
            if x_controle == -velocidade:
                pass
            else:
                x_controle = velocidade
                y_controle = 0
        if event.key == K_DOWN :
            if y_controle == -velocidade:
                pass
            else:
                x_controle = 0
                y_controle = velocidade
        if event.key == K_UP :
            if y_controle == velocidade:
                pass
            else:
                x_controle = 0
                y_controle = -velocidade  
       
    x_cobra += x_controle 
    y_cobra += y_controle

    if cobra.colliderect(maca):
        x_maca = randint(50,600)
        y_maca = randint(40,400)
        pontos += 1
        som_colisao.play()
        comprimento += 1

    lista_cobra= []
    lista_cobra.append(x_cobra)
    lista_cobra.append(y_cobra)
    
    lista_corpo.append(lista_cobra)

    if lista_corpo.count(lista_cobra) > 1 :
        fonte2 = pygame.font.SysFont('arial',20,True,False)
        mensagem = 'GAME OVER| pressione R para reiniciar.'
        texto_formatado = fonte2.render(mensagem,True,(0,0,0))
        ret_texto = texto_formatado.get_rect()
        morreu = True
        while morreu:
            tela.fill((200,200,200))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()

            ret_texto.center = (largura//2,altura//2)
            tela.blit(texto_formatado,ret_texto)
            pygame.display.update() 

    if x_cobra > largura:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = largura
    if y_cobra > altura:
        y_cobra = 0
    if y_cobra < 0:
        y_cobra = altura    
        

    if len(lista_corpo) > comprimento:
        del lista_corpo[0]

    aumenta_cobra(lista_corpo)

    tela.blit(texto_formatado,(450,40))

    pygame.display.update() 
