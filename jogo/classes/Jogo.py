import pygame
from constantes import *
from classes.Fase1 import Fase1

class Jogo:
    def __init__(self):
        pygame.init()
        self.tela_atual = Fase1()

    def atualiza(self):
        pygame.time.Clock().tick(30)

        self.tela_atual = self.tela_atual.atualiza()

        if self.tela_atual == None:
            return False
        return True
    
    def desenha(self):
        JANELA.fill(PRETO)
        self.tela_atual.desenha()
        pygame.display.update()

    def game_loop(self):
        while self.atualiza():
            self.desenha()
    
    def finaliza(self):
        pygame.quit()