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
            'all_sprites': pygame.sprite.Group(),
            'paredes': [],
            'bolinhas': [],
            'come_fantasma': []
            }
        self.jogador = Jogador(self.grupos)
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

    def desenha(self):
        for parede in self.grupos['paredes']:
            pygame.draw.rect(JANELA, AZUL, parede, 1)
        for bolinha in self.grupos['bolinhas']:
            pygame.draw.rect(JANELA, AMARELO_PONTOS, bolinha, 0, BLOCO // 10)
        for come_fantasma in self.grupos['come_fantasma']:
            pygame.draw.rect(JANELA, AMARELO_PONTOS, come_fantasma, 0, BLOCO // 2)
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
        self.image = PAC_MAN[0]
        self.rect = self.image.get_rect()
        x = 14
        y = 16
        self.rect.x = x * BLOCO + MARGEM_X + 2
        self.rect.y = y * BLOCO + MARGEM_Y + 2
        self.direcao = {'direita': False, 'esquerda': False, 'cima': False, 'baixo': False}

    def update(self):
        if self.direcao['direita']:
            self.image = PAC_MAN[0]
            self.rect.x += VELOCIDADE
        elif self.direcao['esquerda']:
            self.image = PAC_MAN[1]
            self.rect.x -= VELOCIDADE
        elif self.direcao['cima']:
            self.image = PAC_MAN[2]
            self.rect.y -= VELOCIDADE
        elif self.direcao['baixo']:
            self.image = PAC_MAN[3]
            self.rect.y += VELOCIDADE

    def reseta_direcao(self):
        self.direcao = {'direita': False, 'esquerda': False, 'cima': False, 'baixo': False}

# class Parede(pygame.sprite.Sprite):
#     def __init__(self, x, y, grupos):
#         super().__init__()
#         self.rect = pygame.Rect(x * BLOCO + MARGEM_X, y * BLOCO + MARGEM_Y, BLOCO, BLOCO)
#         self.image = self.rect
#         self.grupos = grupos
#         self.grupos['all_sprites'].add(self)
#         self.grupos['paredes'].add(self)

if __name__ == '__main__':
    jogo = Jogo()
    jogo.game_loop()
    jogo.finaliza()