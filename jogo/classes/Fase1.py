import pygame
from constantes import *
from classes.Jogador import Jogador
from classes.Fantasma import Fantasma



class Fase1:
    def __init__(self,pontuacao):
        self.grupos = {
            'all_sprites': pygame.sprite.Group(),
            'paredes': [],
            'bolinhas': [],
            'come_fantasma': [],
            'fantasmas': pygame.sprite.Group()
            }
        self.estado = {
            'come_fantasma': {
            'quantidade': 0,
            'tempo': 0
            },
            'delta_t': 0,
            't0': 0,
            'pontuacao' : pontuacao
            }
        self.jogador = Jogador(self.grupos)
        self.fatasma_vermelho = Fantasma(self.grupos, FANTASMA_AMARELO, (LARGURA_MAPA//2) * BLOCO + MARGEM_X +2, (ALTURA_MAPA//2 -5) * BLOCO + MARGEM_Y +2)
        self.le_mapa()
        self.tempo_animacao_fugindo = 0
    
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
                        self.estado['come_fantasma']['quantidade'] += 1
                    elif linha[x] == '4':
                        rect = pygame.Rect(x * BLOCO + MARGEM_X, y * BLOCO + MARGEM_Y, BLOCO, BLOCO//2)
                        self.grupos['paredes'].append(rect)

    def text2image(self, text):
        fonte = pygame.font.Font(FONTE, 20)
        return fonte.render(text, True, BRANCO)

    def desenha(self):
        JANELA.blit(self.text2image(f"Pontuação: {str(self.estado['pontuacao'])}"), (0,0))
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
        t1 = pygame.time.get_ticks()
        self.estado['delta_t'] = (t1 - self.estado['t0']) / 1000
        self.estado['t0'] = t1

        if len(self.grupos['come_fantasma']) < self.estado['come_fantasma']['quantidade']:
            self.estado['come_fantasma']['tempo'] += self.estado['delta_t']
            index = 0
            self.jogador.comedor = True
            if not self.fatasma_vermelho.morto:
                self.fatasma_vermelho.fugindo = True

            if self.estado['come_fantasma']['tempo'] >= 8:
                self.tempo_animacao_fugindo += self.estado['delta_t']
                if self.tempo_animacao_fugindo > 0.3:
                    self.tempo_animacao_fugindo = 0
                    index += 1
            self.fatasma_vermelho.image = FANTASMA_FUGINDO[index]
            if self.estado['come_fantasma']['tempo'] >= 10:
                self.jogador.comedor = True
                self.estado['come_fantasma']['tempo'] = 0
                self.fatasma_vermelho.fugindo = False
                self.jogador.comedor = False
                self.estado['come_fantasma']['quantidade'] -= 1
                self.fatasma_vermelho.image = FANTASMA_AMARELO


        self.fatasma_vermelho.pos_jogador = (self.jogador.rect.x,self.jogador.rect.y)
        self.grupos['all_sprites'].update()
        self.jogador.verifica_direcao_livre()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return None
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RIGHT:
                    self.jogador.prox_direcao = 'direita'
                elif evento.key == pygame.K_LEFT:
                    self.jogador.prox_direcao = 'esquerda'
                elif evento.key == pygame.K_UP:
                    self.jogador.prox_direcao = 'cima'
                elif evento.key == pygame.K_DOWN:
                    self.jogador.prox_direcao = 'baixo'
        colisao_fantasma = pygame.sprite.spritecollide(self.jogador, self.grupos['fantasmas'], False)

        if self.jogador.pontuacao != 0:
            self.estado['pontuacao'] += self.jogador.pontuacao

        if self.fatasma_vermelho.morto:
            self.fatasma_vermelho.fugindo = False

        if self.jogador.comedor:
            for colisao in colisao_fantasma:
                self.fatasma_vermelho.morto = True
        else:
            for colisao in colisao_fantasma:
                print (self.estado['pontuacao'])
                from classes.Tela_game_over import Tela_game_over
                return Tela_game_over(self.estado['pontuacao'])
        
        if len(self.grupos['bolinhas']) == 0:

            return Fase1(self.estado['pontuacao'])

        return self