import pygame
from constantes import *

class Jogador(pygame.sprite.Sprite):
    def __init__(self, grupos):
        super().__init__()
        self.grupos = grupos
        self.grupos['all_sprites'].add(self)
        self.image = PAC_MAN[0]
        self.rect = self.image.get_rect()
        self.rect.x = (LARGURA_MAPA//2) * BLOCO + MARGEM_X +2
        self.rect.y = (ALTURA_MAPA//2) * BLOCO + MARGEM_Y +2
        self.direcao = {'direita': False, 'esquerda': False, 'cima': False, 'baixo': False}
        self.prox_direcao = ''
        self.comedor = False
        self.velocidade = VELOCIDADE

    def update(self):
        self.pontuacao = 0
        if self.direcao['direita']:
            self.image = PAC_MAN[0]
            self.rect.x += self.velocidade
        elif self.direcao['esquerda']:
            self.image = PAC_MAN[1]
            self.rect.x -= self.velocidade
        elif self.direcao['cima']:
            self.image = PAC_MAN[2]
            self.rect.y -= self.velocidade
        elif self.direcao['baixo']:
            self.image = PAC_MAN[3]
            self.rect.y += self.velocidade

        if self.rect.x < MARGEM_X+1:
            self.rect.x = (LARGURA_MAPA-1) * BLOCO + MARGEM_X
        elif self.rect.x > (LARGURA_MAPA-1) * BLOCO + MARGEM_X:
            self.rect.x = MARGEM_X+1

        if self.rect.collidelist(self.grupos['paredes']) != -1:
            if self.direcao['direita']:
                self.rect.x -= self.velocidade
            elif self.direcao['esquerda']:
                self.rect.x += self.velocidade
            elif self.direcao['cima']:
                self.rect.y += self.velocidade
            elif self.direcao['baixo']:
                self.rect.y -= self.velocidade

        index = self.rect.collidelist(self.grupos['bolinhas'])
        if index != -1:
            del self.grupos['bolinhas'][index]
            self.pontuacao += 10

        index = self.rect.collidelist(self.grupos['come_fantasma'])
        if index != -1:
            del self.grupos['come_fantasma'][index]

            

    def reseta_direcao(self):
        self.direcao = {'direita': False, 'esquerda': False, 'cima': False, 'baixo': False}

    def verifica_direcao_livre(self):
        if self.prox_direcao == 'direita':
            if pygame.Rect(self.rect.x+self.velocidade,self.rect.y,self.rect.width,self.rect.height).collidelist(self.grupos['paredes']) == -1:
                self.reseta_direcao()
                self.direcao['direita'] = True
        elif self.prox_direcao == 'esquerda':
            if pygame.Rect(self.rect.x-self.velocidade,self.rect.y,self.rect.width,self.rect.height).collidelist(self.grupos['paredes']) == -1:
                self.reseta_direcao()
                self.direcao['esquerda'] = True
        elif self.prox_direcao == 'cima':
            if pygame.Rect(self.rect.x,self.rect.y-self.velocidade,self.rect.width,self.rect.height).collidelist(self.grupos['paredes']) == -1:
                self.reseta_direcao()
                self.direcao['cima'] = True
        elif self.prox_direcao == 'baixo':
            if pygame.Rect(self.rect.x,self.rect.y+self.velocidade,self.rect.width,self.rect.height).collidelist(self.grupos['paredes']) == -1:
                self.reseta_direcao()
                self.direcao['baixo'] = True