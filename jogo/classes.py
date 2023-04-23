import pygame
from constantes import *
import math
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
            'come_fantasma': [],
            'fantasmas': pygame.sprite.Group()
            }
        self.pos_navegaveis = []
        self.jogador = Jogador(self.grupos)
        self.fatasma_vermelho = Fantasma(self.grupos, FANTASMA_AMARELO, (LARGURA_MAPA//2) * BLOCO + MARGEM_X + 2, (ALTURA_MAPA//2 - 5) * BLOCO + MARGEM_Y + 2, self.pos_navegaveis)
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
                        self.pos_navegaveis.append((round(x * BLOCO + MARGEM_X + 2), round(y * BLOCO + MARGEM_Y + 2)))
                    elif linha[x] == '3':
                        rect = pygame.Rect(x * BLOCO + BLOCO // 4 + MARGEM_X, y * BLOCO + BLOCO // 4 + MARGEM_Y, BLOCO // 2, BLOCO // 2)
                        self.grupos['come_fantasma'].append(rect)
                        self.pos_navegaveis.append((round(x * BLOCO + MARGEM_X + 2), round(y * BLOCO + MARGEM_Y + 2)))
                    elif linha[x] == '4':
                        rect = pygame.Rect(x * BLOCO + MARGEM_X, y * BLOCO + MARGEM_Y, BLOCO, BLOCO//2)
                        self.grupos['paredes'].append(rect)
                    elif linha[x] == '0':
                        self.pos_navegaveis.append((round(x * BLOCO + MARGEM_X + 2), round(y * BLOCO + MARGEM_Y + 2)))

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
        
        # if len(self.grupos['bolinhas']) == 0:
        #     return Fase2()
        # pra quando tiver uma proxima fase

        return self

class Jogador(pygame.sprite.Sprite):
    def __init__(self, grupos):
        super().__init__()
        self.grupos = grupos
        self.grupos['all_sprites'].add(self)
        self.image = PAC_MAN[0]
        self.rect = self.image.get_rect()
        self.rect.x = (LARGURA_MAPA//2) * BLOCO + MARGEM_X + 2
        self.rect.y = (ALTURA_MAPA/2) * BLOCO + MARGEM_Y + 2
        self.direcao = {'direita': False, 'esquerda': False, 'cima': False, 'baixo': False}
        self.prox_direcao = ''

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

        if self.rect.x < MARGEM_X:
            self.rect.x = LARGURA_MAPA * BLOCO + MARGEM_X
        elif self.rect.x > LARGURA_MAPA * BLOCO + MARGEM_X:
            self.rect.x = MARGEM_X

        if self.rect.collidelist(self.grupos['paredes']) != -1:
            if self.direcao['direita']:
                self.rect.x -= VELOCIDADE
            elif self.direcao['esquerda']:
                self.rect.x += VELOCIDADE
            elif self.direcao['cima']:
                self.rect.y += VELOCIDADE
            elif self.direcao['baixo']:
                self.rect.y -= VELOCIDADE

        index = self.rect.collidelist(self.grupos['bolinhas'])
        if index != -1:
            del self.grupos['bolinhas'][index]

        index = self.rect.collidelist(self.grupos['come_fantasma'])
        if index != -1:
            del self.grupos['come_fantasma'][index]

    def reseta_direcao(self):
        self.direcao = {'direita': False, 'esquerda': False, 'cima': False, 'baixo': False}

    def verifica_direcao_livre(self):
        if self.prox_direcao == 'direita':
            if pygame.Rect(self.rect.x+VELOCIDADE,self.rect.y,self.rect.width,self.rect.height).collidelist(self.grupos['paredes']) == -1:
                self.reseta_direcao()
                self.direcao['direita'] = True
        elif self.prox_direcao == 'esquerda':
            if pygame.Rect(self.rect.x-VELOCIDADE,self.rect.y,self.rect.width,self.rect.height).collidelist(self.grupos['paredes']) == -1:
                self.reseta_direcao()
                self.direcao['esquerda'] = True
        elif self.prox_direcao == 'cima':
            if pygame.Rect(self.rect.x,self.rect.y-VELOCIDADE,self.rect.width,self.rect.height).collidelist(self.grupos['paredes']) == -1:
                self.reseta_direcao()
                self.direcao['cima'] = True
        elif self.prox_direcao == 'baixo':
            if pygame.Rect(self.rect.x,self.rect.y+VELOCIDADE,self.rect.width,self.rect.height).collidelist(self.grupos['paredes']) == -1:
                self.reseta_direcao()
                self.direcao['baixo'] = True

class Fantasma(pygame.sprite.Sprite):
    def __init__(self, grupos, img, x, y, pos_navegaveis):
        super().__init__()

        self.grupos = grupos
        self.grupos['all_sprites'].add(self)
        self.grupos['fantasmas'].add(self)

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direcao = {'direita': False, 'esquerda': False, 'cima': False, 'baixo': False}
        self.prox_direcao = ''

        self.pos_jogador = 0
        self.pos_navegaveis = pos_navegaveis

    def update(self):
        print(self.persegicao())

    def persegicao(self):
        abertas = []
        expandidas = []
        print(self.pos_navegaveis)
        abertas.append((self.rect.x, self.rect.y))

        while len(abertas) > 0:
            print(abertas)
            atual = abertas.pop(0)
            expandidas.append(atual)

            if atual == self.pos_jogador:
                break
            else:
                self.prox_celula(abertas, expandidas, atual)

        return expandidas

    def prox_celula(self, abertas, expandidas, atual):
        menor_distancia = math.inf
        posicao_aberta = None

        if atual[0] > MARGEM_X:
            if (atual[0]-BLOCO+1,atual[1]) not in abertas and (atual[0]-BLOCO+1,atual[1]) not in expandidas and (atual[0]-BLOCO+1,atual[1]) in self.pos_navegaveis:
                distancia = self.distancia_euclidiana(atual[0]-BLOCO+1, atual[1], self.pos_jogador[0], self.pos_jogador[1])
                if distancia < menor_distancia:
                    menor_distancia = distancia
                    posicao_aberta = (atual[0]-BLOCO+1,atual[1])

        if atual[0] < LARGURA_MAPA * BLOCO + MARGEM_X:
            if (atual[0]+BLOCO+1,atual[1]) not in abertas and (atual[0]+BLOCO+1,atual[1]) not in expandidas and (atual[0]+BLOCO+1,atual[1]) in self.pos_navegaveis:
                distancia = self.distancia_euclidiana(atual[0]+BLOCO+1, atual[1], self.pos_jogador[0], self.pos_jogador[1])
                if distancia < menor_distancia:
                    menor_distancia = distancia
                    posicao_aberta = (atual[0]+BLOCO+1,atual[1])

        if atual[1] > MARGEM_Y:
            if (atual[0],atual[1]-BLOCO) not in abertas and (atual[0],atual[1]-BLOCO) not in expandidas and (atual[0],atual[1]-BLOCO) in self.pos_navegaveis:
                distancia = self.distancia_euclidiana(atual[0], atual[1]-BLOCO, self.pos_jogador[0], self.pos_jogador[1])
                if distancia < menor_distancia:
                    menor_distancia = distancia
                    posicao_aberta = (atual[0],atual[1]-BLOCO)

        if atual[1] < ALTURA_MAPA * BLOCO + MARGEM_Y:
            if (atual[0],atual[1]+BLOCO) not in abertas and (atual[0],atual[1]+BLOCO) not in expandidas and (atual[0],atual[1]+BLOCO) in self.pos_navegaveis:
                distancia = self.distancia_euclidiana(atual[0], atual[1]+BLOCO, self.pos_jogador[0], self.pos_jogador[1])
                if distancia < menor_distancia:
                    menor_distancia = distancia
                    posicao_aberta = (atual[0],atual[1]+BLOCO)
        
        if posicao_aberta != None:
            abertas.append(posicao_aberta)

    def distancia_euclidiana(self,x1,y1,x2,y2):
        distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        return distancia




if __name__ == '__main__':
    jogo = Jogo()
    jogo.game_loop()
    jogo.finaliza()