import pygame
from constantes import *

class Tela_game_over_pontuacao:
    def __init__(self,pontuacao):
        self.imagem = IMG_TELA_GAME_OVER_PONTUACAO
        self.pontuacao = pontuacao
    def atualiza(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return None
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if 609>= evento.pos[0] >= 416 and 735 >= evento.pos[1] >=668:
                    from classes.Fase1 import Fase1
                    return Fase1(0)
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if 841>= evento.pos[0] >= 560 and 113 >= evento.pos[1] >=78:
                    return None
            if evento.type == pygame.KEYDOWN:
                print (f'apertou uma letra{letra}')
                
        return self

    def text2image(self, text):
        fonte = pygame.font.Font(FONTE, 40)
        return fonte.render(text, True, BRANCO)
        

    def desenha(self):
        JANELA.blit(self.imagem,(TAMANHO_JANELA[0]//2 - 700//2 ,TAMANHO_JANELA[1]//2 - 760//2))
        #pygame.draw.rect(JANELA,AZUL,pygame.Rect(372, 670, 281, 46))
        #pygame.draw.rect(JANELA,AZUL,pygame.Rect(209, 44, 281, 35))
        #pygame.draw.rect(JANELA,AZUL,pygame.Rect(560, 78, 281, 35))
        JANELA.blit(self.text2image(f"{str(self.pontuacao)}"), ((194 + 281//2) - ((len(str(self.pontuacao))*15)//2), 45))
        JANELA.blit(self.text2image(f"{str(self.pontuacao)}"), ((545 + 286//2) - ((len(str(self.pontuacao))*15)//2), 80))







