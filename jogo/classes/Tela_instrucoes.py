import pygame
from constantes import *

class Tela_instrucoes:
    def __init__(self):
        self.imagem = IMG_TELA_INSTRUCOES

    def atualiza(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return None
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if 609>= evento.pos[0] >= 416 and 735 >= evento.pos[1] >=668:
                    return None
        return self

    def desenha(self):
        JANELA.blit(self.imagem,(TAMANHO_JANELA[0]//2 - TAMANHO_IMG_TELA_INICIAL[0]//2 ,TAMANHO_JANELA[1]//2 - TAMANHO_IMG_TELA_INICIAL[1]//2))
        #   pygame.draw.rect(JANELA,AZUL,pygame.Rect(416, 668, 193, 67))



