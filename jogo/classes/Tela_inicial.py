import pygame
from constantes import *



class Tela_inicial:
    def __init__(self):
        self.imagem = IMG_TELA_INICIAL

    def atualiza(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return None
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if 596>= evento.pos[0] >= 433 and 405 >= evento.pos[1] >=363:
                    from classes.Tela_placares import Tela_placares
                    return Tela_placares()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if 668>= evento.pos[0] >= 358 and 493 >= evento.pos[1] >=415:
                    from classes.Fase1 import Fase1
                    return Fase1(0,3)
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if 609>= evento.pos[0] >= 417 and 543 >= evento.pos[1] >=501:
                    from classes.Tela_instrucoes import Tela_instrucoes
                    return Tela_instrucoes()
        return self

    def desenha(self):
        JANELA.blit(self.imagem,(TAMANHO_JANELA[0]//2 - TAMANHO_IMG_TELA_INICIAL[0]//2 ,TAMANHO_JANELA[1]//2 - TAMANHO_IMG_TELA_INICIAL[1]//2))
        # pygame.draw.rect(JANELA,AZUL,pygame.Rect(433, 363, 163, 42))
        # pygame.draw.rect(JANELA,AZUL,pygame.Rect(358, 415, 310, 78))
        # pygame.draw.rect(JANELA,AZUL,pygame.Rect(417, 501, 192, 42))