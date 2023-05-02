import pygame
from constantes import *
import os

class Tela_placares:
    def __init__(self):
        self.imagem = IMG_TELA_PLACARES

    def text2image(self, text):
        fonte = pygame.font.Font(FONTE, 40)
        return fonte.render(text, True, AMARELO_PAC_MAN)
    
    def ordena_placar(self):
        placar_tuplas = []
        with open('pontuacao.txt', 'r') as arquivo:
            arquivo.seek(0)
            for linha in arquivo:
                conteudo_linha = linha.strip()
                if conteudo_linha == '':
                    break
                nome_pontuacao = conteudo_linha.split(':')
                placar_tuplas.append((nome_pontuacao[1], nome_pontuacao[0].upper()))
        return sorted(placar_tuplas, reverse=True)
    
    def atualiza(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return None
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if 609>= evento.pos[0] >= 416 and 735 >= evento.pos[1] >=668:
                    from classes.Tela_inicial import Tela_inicial
                    return Tela_inicial()
        return self

    def desenha(self):
        JANELA.blit(self.imagem,(TAMANHO_JANELA[0]//2 - TAMANHO_IMG_TELA_INICIAL[0]//2 ,TAMANHO_JANELA[1]//2 - TAMANHO_IMG_TELA_INICIAL[1]//2))
        for tupla in self.ordena_placar():
            JANELA.blit(self.text2image(f'{tupla[1]} : {tupla[0]}'), (405,200))



