import pygame
TAMANHO_JANELA = (1024,760)
#mapa
LARGURA_MAPA = 6
ALTURA_MAPA = 6
BLOCO = min(TAMANHO_JANELA[0] // LARGURA_MAPA, TAMANHO_JANELA[1] // ALTURA_MAPA)
POSICOES_OCUPADAS = []

#jogo
JANELA = pygame.display.set_mode(TAMANHO_JANELA)
MARGEM_X = TAMANHO_JANELA[0]/2 - LARGURA_MAPA*BLOCO/2
MARGEM_Y = TAMANHO_JANELA[1]/2 - ALTURA_MAPA*BLOCO/2

#cores
PRETO = (0,0,0)
BRANCO = (255,255,255)
AZUL = (0,0,255)
AMARELO_PONTOS = (255,219,88)
AMARELO_PAC_MAN = (255,255,0)

#jogador
TAMANHO_JOGADOR = (BLOCO-4,BLOCO-4)
PAC_MAN = [pygame.transform.scale(pygame.image.load('jogo/assets\img\pac_man.png'), TAMANHO_JOGADOR),pygame.transform.scale(pygame.image.load('jogo/assets\img\pac_man_E.png'), TAMANHO_JOGADOR),
pygame.transform.scale(pygame.image.load('jogo/assets\img\pac_man_C.png'), TAMANHO_JOGADOR),pygame.transform.scale(pygame.image.load('jogo/assets\img\pac_man_B.png'), TAMANHO_JOGADOR)]
VELOCIDADE = 5

#fantasmas
TAMANHO_FANTASMA = (BLOCO-4,BLOCO-4)
FANTASMA_AMARELO = pygame.transform.scale(pygame.image.load('jogo/assets\img/fantasma_amarelo.png'), TAMANHO_FANTASMA)
