import pygame
from constantes import *
from classes.Tela_inicial import Tela_inicial

class Jogo:
    def __init__(self):
        pygame.init()
        self.tela_atual = Tela_inicial()
        self.pontucao = 0

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