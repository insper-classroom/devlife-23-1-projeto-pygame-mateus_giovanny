import pygame
from constantes import *
import os

class Tela_placares:
    """
    Essa tela mostra as 5 melhores pontuações salvas no computador do jogador

    ...

    Atributos
    ---------
    imagem : pygame.surface
        essa tela tambem é uma imagem definida em constantes
    """
    def __init__(self):
        self.imagem = IMG_TELA_PLACARES

    def text2image(self, text) -> pygame.surface:
        """
        converte uma string em imagem para ser desenhada

        Parâmetros
        ----------
        text :  str
            o texto que vai ser transformado em imagem(obrigatório)
        """
        fonte = pygame.font.Font(FONTE, 40)
        return fonte.render(text, True, AMARELO_PAC_MAN)
    
    def ordena_placar(self) -> list:
        """
        lê o arquivo de pontuação e retorna uma lista de tuplas ordenada pela pontuação de forma decresente
        """
        placar_tuplas = []
        contador = 0
        with open('pontuacao.txt', 'r') as arquivo:
            arquivo.seek(0)
            for linha in arquivo:
                contador += 1
                conteudo_linha = linha.strip()
                if conteudo_linha == '':
                    break
                nome_pontuacao = conteudo_linha.split(':')
                placar_tuplas.append((int(nome_pontuacao[1]), nome_pontuacao[0].upper()))
        return sorted(placar_tuplas, reverse=True)
    
    def atualiza(self):
        """
        atualiza o estado da tela de placares, sempre verificando se o jogador clicou em algum dos botoes da tela,
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
        desenha a imagem da tela no fundo e desenha as pontuações por cima
        """
        contador = 0
        JANELA.blit(self.imagem,(TAMANHO_JANELA[0]//2 - TAMANHO_IMG_TELA_INICIAL[0]//2 ,TAMANHO_JANELA[1]//2 - TAMANHO_IMG_TELA_INICIAL[1]//2))
        lista_placar = self.ordena_placar()
        for tupla in lista_placar:
            if contador < 5:
                img = self.text2image(f'{tupla[1]} : {tupla[0]}')
                JANELA.blit(img, (405,200 + img.get_height() * lista_placar.index(tupla)))
            contador += 1



