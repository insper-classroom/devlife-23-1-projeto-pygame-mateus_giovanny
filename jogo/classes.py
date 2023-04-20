import pygame
from constantes import *
class Jogo:
    def __init__(self):
        pygame.init()
        self.tela_atual = Fase1()

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

class Fase1:
    def __init__(self):
        self.grupos = {
            'all_sprites': pygame.sprite.Group()
            }
        self.jogador = Jogador(self.grupos)
    
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

    def desenha(self):
        with open('jogo/mapas/mapa1.txt','r') as mapa1:
            for y in range(ALTURA_MAPA):
                linha = mapa1.readline()
                for x in range(len(linha)):
                    if linha[x] == '1':
                        rect = pygame.Rect(x * BLOCO + MARGEM_X, y * BLOCO + MARGEM_Y, BLOCO, BLOCO)
                        pygame.draw.rect(JANELA, AZUL, rect, 1)
                    elif linha[x] == '2':
                        pos_x = x * BLOCO + BLOCO // 2 + MARGEM_X
                        pos_y = y * BLOCO + BLOCO // 2 + MARGEM_Y
                        raio = BLOCO // 10
                        pygame.draw.circle(JANELA, AMARELO_PONTOS, (pos_x, pos_y), raio)
                    elif linha[x] == '3':
                        pos_x = x * BLOCO + BLOCO // 2 + MARGEM_X
                        pos_y = y * BLOCO + BLOCO // 2 + MARGEM_Y
                        raio = BLOCO // 2.5
                        pygame.draw.circle(JANELA, AMARELO_PONTOS, (pos_x, pos_y), raio)
        self.grupos['all_sprites'].draw(JANELA)
    
    def atualiza(self):
        self.grupos['all_sprites'].update()
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                return None
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_d:
                    self.jogador.reseta_direcao()
                    self.jogador.direcao['direita'] = True
                elif evento.key == pygame.K_a:
                    self.jogador.reseta_direcao()
                    self.jogador.direcao['esquerda'] = True
                elif evento.key == pygame.K_w:
                    self.jogador.reseta_direcao()
                    self.jogador.direcao['cima'] = True
                elif evento.key == pygame.K_s:
                    self.jogador.reseta_direcao()
                    self.jogador.direcao['baixo'] = True

        return self

class Jogador(pygame.sprite.Sprite):
    def __init__(self, grupos):
        super().__init__()
        self.grupos = grupos
        self.grupos['all_sprites'].add(self)
        img = PAC_MAN0
        self.image = pygame.transform.scale(img, TAMANHO_JOGADOR)
        self.rect = self.image.get_rect()
        x = 14
        y = 16
        self.rect.x = x * BLOCO + MARGEM_X + 2
        self.rect.y = y * BLOCO + MARGEM_Y + 2
        self.direcao = {'direita': False, 'esquerda': False, 'cima': False, 'baixo': False}

    def update(self):
        if self.direcao['direita']:
            self.rect.x += VELOCIDADE
        elif self.direcao['esquerda']:
            self.rect.x -= VELOCIDADE
        elif self.direcao['cima']:
            self.rect.y -= VELOCIDADE
        elif self.direcao['baixo']:
            self.rect.y += VELOCIDADE

    def reseta_direcao(self):
        self.direcao = {'direita': False, 'esquerda': False, 'cima': False, 'baixo': False}

if __name__ == '__main__':
    jogo = Jogo()
    jogo.game_loop()
    jogo.finaliza()