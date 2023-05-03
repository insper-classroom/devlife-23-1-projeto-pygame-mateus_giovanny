import pygame
from constantes import *

class Tela_instrucoes:
    """
    Tela que mostra as instruções do jogo

    ...

    Atributos
    ---------
    imagem : pygame.surface
        é a imagem que fica no fundo da tela de instrucoes
    """
    def __init__(self):
        self.imagem = IMG_TELA_INSTRUCOES

    def atualiza(self):
        """
        atualiza o estado da tela de intrucoes, sempre verificando se o jogador clicou em algum dos botoes da tela,
        caso não tenha clicado retorna a própria classe
        """
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return None
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if 609>= evento.pos[0] >= 416 and 735 >= evento.pos[1] >=668:
                    from classes.Tela_inicial import Tela_inicial
                    return Tela_inicial()
        return self

    def desenha(self):
        """
        desenha a self.image na tela
        """
        JANELA.blit(self.imagem,(TAMANHO_JANELA[0]//2 - TAMANHO_IMG_TELA_INICIAL[0]//2 ,TAMANHO_JANELA[1]//2 - TAMANHO_IMG_TELA_INICIAL[1]//2))




