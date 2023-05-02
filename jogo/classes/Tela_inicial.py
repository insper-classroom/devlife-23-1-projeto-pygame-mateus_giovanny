import pygame
from constantes import *

class Tela_inicial:
    """
    Essa é a classe da tela inicial do jogo

    ...

    Atributos
    ---------
    imagem : pygame.surface
        a tela incial é uma imagem que está definida em constantes

    Métodos
    -------
    atualiza() : Class
        atualiza o estado da tela inicial, sempre verificando se o jogador clicou em algum dos botoes da tela,
        caso não tenha clicado retorna a própria classe
    desenha() : None
        desenha a imagem da tela incial
    """
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