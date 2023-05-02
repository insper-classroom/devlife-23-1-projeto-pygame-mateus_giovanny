import pygame
from constantes import *

class Tela_game_over_pontuacao:
    def __init__(self,pontuacao):
        self.imagem = IMG_TELA_GAME_OVER_PONTUACAO
        self.pontuacao = pontuacao
        self.nome = ''
        self.alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    def atualiza(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return None
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if 609>= evento.pos[0] >= 416 and 735 >= evento.pos[1] >=668:
                    from classes.Fase1 import Fase1
                    return Fase1(0)
            if evento.type == pygame.KEYDOWN:
                if len(self.nome) <  3 and pygame.key.name(evento.key) in self.alfabeto:
                    self.nome += pygame.key.name(evento.key)
                if evento.key == pygame.K_BACKSPACE and len(self.nome) > 0:
                    self.nome = self.nome.replace(self.nome[-1],'',1)

        if len(self.nome) == 3:
            self.grava_pontuação()
            self.nome = 'Salvo'
                
        return self
    
    def grava_pontuação(self):
        with open('pontuacao.txt','a') as arquivo:
            arquivo.write(f'{self.nome}:{self.pontuacao}\n')

    def text2image(self, text):
        fonte = pygame.font.Font(FONTE, 40)
        return fonte.render(text, True, BRANCO)
        

    def desenha(self):
        JANELA.blit(self.imagem,(TAMANHO_JANELA[0]//2 - 700//2 ,TAMANHO_JANELA[1]//2 - 760//2))
        #pygame.draw.rect(JANELA,AZUL,pygame.Rect(372, 670, 281, 46))
        #pygame.draw.rect(JANELA,AZUL,pygame.Rect(209, 44, 281, 35))
        #pygame.draw.rect(JANELA,AZUL,pygame.Rect(560, 78, 281, 35))
        JANELA.blit(self.text2image(f"{str(self.pontuacao)}"), ((194 + 281//2) - ((len(str(self.pontuacao))*15)//2), 45))
        JANELA.blit(self.text2image(self.nome), ((545 + 286//2) - len(self.nome)*10, 80))







