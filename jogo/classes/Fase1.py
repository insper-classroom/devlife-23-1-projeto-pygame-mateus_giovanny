import pygame
from constantes import *
from classes.Jogador import Jogador
from classes.Fantasma import Fantasma

class Fase1:
    def __init__(self):
        self.grupos = {
            'all_sprites': pygame.sprite.Group(),
            'paredes': [],
            'bolinhas': [],
            'come_fantasma': [],
            'fantasmas': pygame.sprite.Group()
            }
        self.jogador = Jogador(self.grupos)
        self.fatasma_vermelho = Fantasma(self.grupos, FANTASMA_AMARELO, (LARGURA_MAPA//2) * BLOCO + MARGEM_X +2, (ALTURA_MAPA//2 -5) * BLOCO + MARGEM_Y +2)
        self.le_mapa()
    
    # def gera_mapa(self):
    #     with open('jogo/mapas/mapa2.txt','w') as mapa1:
    #         for y in range(ALTURA_MAPA):
    #             if y != 0:
    #                 mapa1.write('\n')
    #             for x in range(LARGURA_MAPA):
    #                 if (x == 0 or y == 0) or (x == LARGURA_MAPA - 1 or y == ALTURA_MAPA - 1):
    #                     mapa1.write('1')
    #                 # elif LARGURA_MAPA // 2 - 5 <= x <= LARGURA_MAPA // 2 + 5 and ALTURA_MAPA // 2 - 5 <= y <= ALTURA_MAPA // 2 + 5:
    #                 #     mapa1.write('1')
    #                 else:
    #                     mapa1.write('2')

    def le_mapa(self):
        with open('jogo/mapas/mapa1.txt','r') as mapa1:
            for y in range(ALTURA_MAPA):
                linha = mapa1.readline()
                for x in range(len(linha)):
                    if linha[x] == '1':
                        rect = pygame.Rect(x * BLOCO + MARGEM_X, y * BLOCO + MARGEM_Y, BLOCO, BLOCO)
                        self.grupos['paredes'].append(rect)
                    elif linha[x] == '2':
                        rect = pygame.Rect(x * BLOCO + BLOCO // 2 + MARGEM_X, y * BLOCO + BLOCO // 2 + MARGEM_Y, BLOCO // 10, BLOCO // 10)
                        self.grupos['bolinhas'].append(rect)
                    elif linha[x] == '3':
                        rect = pygame.Rect(x * BLOCO + BLOCO // 4 + MARGEM_X, y * BLOCO + BLOCO // 4 + MARGEM_Y, BLOCO // 2, BLOCO // 2)
                        self.grupos['come_fantasma'].append(rect)
                    elif linha[x] == '4':
                        rect = pygame.Rect(x * BLOCO + MARGEM_X, y * BLOCO + MARGEM_Y, BLOCO, BLOCO//2)
                        self.grupos['paredes'].append(rect)

    def desenha(self):
        for parede in self.grupos['paredes']:
            if parede.height == BLOCO//2:
                pygame.draw.rect(JANELA, BRANCO, parede)
            else:
                pygame.draw.rect(JANELA, AZUL, parede, 1)
        for bolinha in self.grupos['bolinhas']:
            pygame.draw.rect(JANELA, AMARELO_PONTOS, bolinha, 0, BLOCO // 10)
        for come_fantasma in self.grupos['come_fantasma']:
            pygame.draw.rect(JANELA, AMARELO_PONTOS, come_fantasma, 0, BLOCO // 2)
        self.grupos['all_sprites'].draw(JANELA)
    
    def atualiza(self):
        self.fatasma_vermelho.pos_jogador = (self.jogador.rect.x,self.jogador.rect.y)
        self.grupos['all_sprites'].update()
        self.jogador.verifica_direcao_livre()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return None
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_d:
                    self.jogador.prox_direcao = 'direita'
                elif evento.key == pygame.K_a:
                    self.jogador.prox_direcao = 'esquerda'
                elif evento.key == pygame.K_w:
                    self.jogador.prox_direcao = 'cima'
                elif evento.key == pygame.K_s:
                    self.jogador.prox_direcao = 'baixo'

        colisao_fantasma = pygame.sprite.spritecollide(self.jogador, self.grupos['fantasmas'], False)
        for colisao in colisao_fantasma:
            return None
        
        # if len(self.grupos['bolinhas']) == 0:
        #     return Fase2()
        # pra quando tiver uma proxima fase

        return self