import pygame
from constantes import *
from classes.Tela_inicial import Tela_inicial

class Jogo:
    """
    Essa é a classe que eu deixo toda a estrutura básica do meu jogo.

    ...

    Atributos
    ---------
    tela_atual : Classe de tela
        é a classe da tela atual que o jogo está
    pontuacao : int
        é a pontuação do jogador no jogo
    """
    def __init__(self):
        pygame.init()
        pygame.mixer.music.load('assets\som\musica_fundo.mp3')
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(-1)
        self.tela_atual = Tela_inicial()
        self.pontucao = 0

    def atualiza(self) -> bool:
        """
        atualiza a tela atual do jogo, se tela_atual -> None fecha o jogo
        """
        pygame.time.Clock().tick(30)

        self.tela_atual = self.tela_atual.atualiza()

        if self.tela_atual == None:
            return False
        return True
    
    def desenha(self) -> None:
        """
        chama a função desenha da tela atual
        """
        JANELA.fill(PRETO)
        self.tela_atual.desenha()
        pygame.display.update()

    def game_loop(self) -> None:
        """
        mantém o jogo em loop
        """
        while self.atualiza():
            self.desenha()
    
    def finaliza(self) -> None:
        """
        encerra o pygame
        """
        pygame.quit()