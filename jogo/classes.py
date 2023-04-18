import pygame
from constantes import *
from fase_padrao import Fase
class Jogo:
    def __init__(self):
        pygame.init()
        self.tela_atual = Fase1()

    def atualiza(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
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

class Fase1(Fase):
    def __init__(self):
        self.gera_mapa()

    def desenha(self):
        pass

if __name__ == '__main__':
    jogo = Jogo()
    jogo.game_loop()
    jogo.finaliza()