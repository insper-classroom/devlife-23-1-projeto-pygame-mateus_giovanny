import pygame
from constantes import *

class Tela_game_over:
    def __init__(self,pontuacao):
        self.imagem = IMG_TELA_GAME_OVER_1
        self.pontuacao = pontuacao
    def atualiza(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return None
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if 609>= evento.pos[0] >= 416 and 735 >= evento.pos[1] >=668:
                    from classes.Fase1 import Fase1
                    return Fase1(0,3)
        return self

    def text2image(self, text):
        fonte = pygame.font.Font(FONTE, 40)
        return fonte.render(text, True, BRANCO)
        

    def desenha(self):
        JANELA.blit(self.imagem,(TAMANHO_JANELA[0]//2 - 700//2 ,TAMANHO_JANELA[1]//2 - 760//2))
        #pygame.draw.rect(JANELA,AZUL,pygame.Rect(372, 670, 281, 46))
        #pygame.draw.rect(JANELA,AZUL,pygame.Rect(209, 44, 281, 35))
        JANELA.blit(self.text2image(f"{str(self.pontuacao)}"), ((194 + 281//2) - ((len(str(self.pontuacao))*15)//2), 45))
        





