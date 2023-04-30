import pygame
from constantes import *
from classes.Jogador import Jogador
from classes.Blinky import Blinky
from classes.Clyde import Clyde
from classes.Inky import Inky
from classes.Pinky import Pinky

class Fase1:
    def __init__(self,pontuacao, vidas):
        pygame.mixer.music.load('assets\som\ghostmove.ogg')
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(-1)
        COMENDO_FANTASMA.set_volume(0.6)
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
            'pontuacao' : pontuacao,
            'tempo_sair': 0,
            'animacao_pac': 0,
            'jogador_vidas': vidas,
            'tocando': 'ghostmove',
            'jogador_comeu': 0
            }
        self.jogador = Jogador(self.grupos)
        Blinky(self.grupos, FANTASMA_VERMELHO)
        Pinky(self.grupos, FANTASMA_ROSA)
        Inky(self.grupos, FANTASMA_AZUL)
        Clyde(self.grupos, FANTASMA_AMARELO)
        self.le_mapa()
        self.tempo_animacao_fugindo = 0

    def le_mapa(self):
        with open('mapas/mapa1.txt','r') as mapa1:
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
        for i in range(self.estado['jogador_vidas']):
            JANELA.blit(PAC_MAN[0], (i * PAC_MAN[0].get_width(),20))
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

        self.estado['tempo_sair'] += self.estado['delta_t']
        if self.estado['tempo_sair'] >= 2:
            self.estado['tempo_sair'] = 0
            for fantasma in self.grupos['fantasmas']:
                if fantasma.estado['preso']:
                    fantasma.estado['preso'] = False
                    break

        self.estado['animacao_pac'] += self.estado['delta_t']
        if self.estado['animacao_pac'] >= 0.05:
            self.estado['animacao_pac'] = 0
            self.jogador.index +=1

        if len(self.grupos['come_fantasma']) < self.estado['come_fantasma']['quantidade']:

            if self.estado['tocando'] == 'ghostmove':
                self.estado['tocando'] = 'power_pellet'
                pygame.mixer.music.load('assets\som\power_pellet.wav')
                pygame.mixer.music.set_volume(0.4)
                pygame.mixer.music.play(-1)

            self.estado['come_fantasma']['tempo'] += self.estado['delta_t']
            index = 0
            self.jogador.comedor = True

            for fantasma in self.grupos['fantasmas']:
                if not fantasma.estado['morto'] and fantasma.estado['mortes'] == 0:
                    fantasma.estado['fugindo'] = True

            if self.estado['come_fantasma']['tempo'] >= 8:
                self.tempo_animacao_fugindo += self.estado['delta_t']
                if self.tempo_animacao_fugindo > 0.3:
                    self.tempo_animacao_fugindo = 0
                    index += 1
                    
            for fantasma in self.grupos['fantasmas']:
                if fantasma.estado['fugindo']:
                    fantasma.image = FANTASMA_FUGINDO[index]

            if self.estado['come_fantasma']['tempo'] >= 10:
                self.estado['tocando'] = 'ghostmove'
                pygame.mixer.music.load('assets\som\ghostmove.ogg')
                pygame.mixer.music.set_volume(0.4)
                pygame.mixer.music.play(-1)

                self.estado['come_fantasma']['tempo'] = 0
                self.estado['jogador_comeu'] = 0

                for fantasma in self.grupos['fantasmas']:
                    fantasma.estado['fugindo'] = False
                    fantasma.estado['mortes'] = 0
                self.jogador.comedor = False
                self.estado['come_fantasma']['quantidade'] -= 1

        for fantasma in self.grupos['fantasmas']:
            fantasma.pos_jogador = (self.jogador.rect.x,self.jogador.rect.y)
            fantasma.prox_direcao_jogador = self.jogador.prox_direcao

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

        if self.jogador.comedor:
            for fantasma in colisao_fantasma:
                if fantasma.estado['fugindo']:
                    COMENDO_FANTASMA.play()
                    self.estado['jogador_comeu'] += 1
                    self.estado['pontuacao'] += 100 * 2**self.estado['jogador_comeu']
                    fantasma.estado['morto'] = True
                    fantasma.estado['mortes'] += 1
        else:
            for fantasma in colisao_fantasma:
                if not fantasma.estado['morto']:
                    for fantasma in self.grupos['fantasmas']:
                        fantasma.rect.x = fantasma.pos_inicial[0]
                        fantasma.rect.y = fantasma.pos_inicial[1]
                        fantasma.estado['preso'] = True
                    self.jogador.reseta_direcao()
                    self.jogador.prox_direcao = ''
                    self.jogador.index = 1
                    self.jogador.rect.x = (LARGURA_MAPA//2) * BLOCO + MARGEM_X +2
                    self.jogador.rect.y = (ALTURA_MAPA//2) * BLOCO + MARGEM_Y +2
                    self.estado['jogador_vidas'] -= 1
        
        if self.estado['jogador_vidas'] <= 0:
            pygame.mixer.music.load('assets\som\musica_fundo.mp3')
            pygame.mixer.music.set_volume(0.4)
            pygame.mixer.music.play(-1)
            from classes.Tela_game_over import Tela_game_over
            return Tela_game_over(self.estado['pontuacao'])
        
        if len(self.grupos['bolinhas']) == 0:
            return Fase1(self.estado['pontuacao'], self.estado['jogador_vidas'])

        return self