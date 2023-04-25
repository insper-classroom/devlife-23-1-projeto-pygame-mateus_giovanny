import pygame
from constantes import *

class Fantasma(pygame.sprite.Sprite):
    def __init__(self, grupos, img, x, y):
        super().__init__()

        self.grupos = grupos
        self.grupos['all_sprites'].add(self)
        self.grupos['fantasmas'].add(self)
        self.quantidade_come_fantasmas = 4

        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.direcao = {'direita': False, 'esquerda': False, 'cima': False, 'baixo': False}
        self.prox_direcao = ''
        self.posicoes_anteriores = ''

        self.pos_jogador = None

        self.prioridade = ''
        self.perdido = False
                
    
    def verifica_parede(self, x, y):
        if pygame.Rect(x, y, self.rect.width, self.rect.height).collidelist(self.grupos['paredes']) == -1:
            return True
        return False
    
    def reseta_direcao(self):
        self.direcao = {'direita': False, 'esquerda': False, 'cima': False, 'baixo': False}

    def mao_direita(self):
        if self.prioridade == 'direita':
            if self.verifica_parede(self.rect.x + VELOCIDADE, self.rect.y) and self.posicoes_anteriores != self.prioridade:
                self.perdido = False
            elif self.verifica_parede(self.rect.x, self.rect.y - VELOCIDADE) and self.posicoes_anteriores != 'cima':
                self.reseta_direcao()
                self.posicoes_anteriores = 'baixo'
                self.direcao['cima'] = True
            elif self.verifica_parede(self.rect.x - VELOCIDADE, self.rect.y) and self.posicoes_anteriores != 'esquerda':
                self.reseta_direcao()
                self.posicoes_anteriores = 'direita'
                self.direcao['esquerda'] = True
            else:
                self.reseta_direcao()
                self.posicoes_anteriores = 'cima'
                self.direcao['baixo'] = True

        elif self.prioridade == 'esquerda':
            if self.verifica_parede(self.rect.x - VELOCIDADE, self.rect.y) and self.posicoes_anteriores != self.prioridade:
                self.perdido = False
            elif self.verifica_parede(self.rect.x, self.rect.y + VELOCIDADE) and self.posicoes_anteriores != 'baixo':
                self.reseta_direcao()
                self.posicoes_anteriores = 'cima'
                self.direcao['baixo'] = True
            elif self.verifica_parede(self.rect.x + VELOCIDADE, self.rect.y) and self.posicoes_anteriores != 'direita':
                self.reseta_direcao()
                self.posicoes_anteriores = 'esquerda'
                self.direcao['direita'] = True
            else:
                self.reseta_direcao()
                self.posicoes_anteriores = 'baixo'
                self.direcao['cima'] = True

        elif self.prioridade == 'cima':
            if self.verifica_parede(self.rect.x, self.rect.y - VELOCIDADE) and self.posicoes_anteriores != self.prioridade:
                self.perdido = False
            elif self.verifica_parede(self.rect.x - VELOCIDADE, self.rect.y) and self.posicoes_anteriores != 'esquerda':
                self.reseta_direcao()
                self.posicoes_anteriores = 'direita'
                self.direcao['esquerda'] = True
            elif self.verifica_parede(self.rect.x, self.rect.y + VELOCIDADE) and self.posicoes_anteriores != 'baixo':
                self.reseta_direcao()
                self.posicoes_anteriores = 'cima'
                self.direcao['baixo'] = True
            else:
                self.reseta_direcao()
                self.posicoes_anteriores = 'esquerda'
                self.direcao['direita'] = True

        elif self.prioridade == 'baixo':
            if self.verifica_parede(self.rect.x, self.rect.y + VELOCIDADE) and self.posicoes_anteriores != self.prioridade:
                self.perdido = False
            elif self.verifica_parede(self.rect.x + VELOCIDADE, self.rect.y) and self.posicoes_anteriores != 'direita':
                self.reseta_direcao()
                self.posicoes_anteriores = 'esquerda'
                self.direcao['direita'] = True
            elif self.verifica_parede(self.rect.x, self.rect.y - VELOCIDADE) and self.posicoes_anteriores != 'cima':
                self.reseta_direcao()
                self.posicoes_anteriores = 'baixo'
                self.direcao['cima'] = True
            else:
                self.reseta_direcao()
                self.posicoes_anteriores = 'direita'
                self.direcao['esquerda'] = True

    #algoritimos de busca em matriz

    def escolhe_direcao(self):
        if self.prioridade == 'direita':
            if self.verifica_parede(self.rect.x + VELOCIDADE, self.rect.y) and self.posicoes_anteriores != 'direita':
                self.posicoes_anteriores = 'esquerda'
                self.reseta_direcao()
                self.direcao['direita'] = True
            else:
                if self.verifica_parede(self.rect.x, self.rect.y - VELOCIDADE) and self.rect.y > self.pos_jogador[1] and self.posicoes_anteriores != 'cima':
                    self.posicoes_anteriores = 'baixo'
                    self.reseta_direcao()
                    self.direcao['cima'] = True
                elif self.verifica_parede(self.rect.x, self.rect.y + VELOCIDADE):
                    self.posicoes_anteriores = 'cima'
                    self.reseta_direcao()
                    self.direcao['baixo'] = True
                else:
                    self.perdido = True
                    self.reseta_direcao()
        
        elif self.prioridade == 'esquerda':
            if self.verifica_parede(self.rect.x - VELOCIDADE, self.rect.y) and self.posicoes_anteriores != 'esquerda':
                self.posicoes_anteriores = 'direita'
                self.reseta_direcao()
                self.direcao['esquerda'] = True
            else:
                if self.verifica_parede(self.rect.x, self.rect.y - VELOCIDADE) and self.rect.y > self.pos_jogador[1] and self.posicoes_anteriores != 'cima':
                    self.posicoes_anteriores = 'baixo'
                    self.reseta_direcao()
                    self.direcao['cima'] = True
                elif self.verifica_parede(self.rect.x, self.rect.y + VELOCIDADE):
                    self.posicoes_anteriores = 'cima'
                    self.reseta_direcao()
                    self.direcao['baixo'] = True
                else:
                    self.perdido = True
                    self.reseta_direcao()
        
        elif self.prioridade == 'cima':
            if self.verifica_parede(self.rect.x, self.rect.y - VELOCIDADE) and self.posicoes_anteriores != 'cima':
                self.posicoes_anteriores = 'baixo'
                self.reseta_direcao()
                self.direcao['cima'] = True
            else:
                if self.verifica_parede(self.rect.x - VELOCIDADE, self.rect.y) and self.rect.x > self.pos_jogador[0] and self.posicoes_anteriores != 'esquerda':
                    self.posicoes_anteriores = 'direita'
                    self.reseta_direcao()
                    self.direcao['esquerda'] = True
                elif self.verifica_parede(self.rect.x + VELOCIDADE, self.rect.y):
                    self.posicoes_anteriores = 'esquerda'
                    self.reseta_direcao()
                    self.direcao['direita'] = True
                else:
                    self.perdido = True
                    self.reseta_direcao()
        
        elif self.prioridade == 'baixo':
            if self.verifica_parede(self.rect.x, self.rect.y + VELOCIDADE) and self.posicoes_anteriores != 'baixo':
                self.posicoes_anteriores = 'cima'
                self.reseta_direcao()
                self.direcao['baixo'] = True
            else:
                if self.verifica_parede(self.rect.x - VELOCIDADE, self.rect.y) and self.rect.x > self.pos_jogador[0] and self.posicoes_anteriores != 'esquerda':
                    self.posicoes_anteriores = 'direita'
                    self.reseta_direcao()
                    self.direcao['esquerda'] = True
                elif self.verifica_parede(self.rect.x + VELOCIDADE, self.rect.y):
                    self.posicoes_anteriores = 'esquerda'
                    self.reseta_direcao()
                    self.direcao['direita'] = True
                else:
                    self.perdido = True
                    self.reseta_direcao()
        
    def define_prioridade(self):
        if len(self.grupos['come_fantasma']) < self.quantidade_come_fantasmas:
            if abs(self.rect.x - self.pos_jogador[0]) > abs(self.rect.y - self.pos_jogador[1]):
                if self.rect.x > self.pos_jogador[0]:
                    self.prioridade = 'direita'
                else:
                    self.prioridade = 'esquerda'
            else:
                if self.rect.y > self.pos_jogador[1]:
                    self.prioridade = 'baixo'
                else:
                    self.prioridade = 'cima'
        else:
            if abs(self.rect.x - self.pos_jogador[0]) > abs(self.rect.y - self.pos_jogador[1]):
                if self.rect.x > self.pos_jogador[0]:
                    self.prioridade = 'esquerda'
                else:
                    self.prioridade = 'direita'
            else:
                if self.rect.y > self.pos_jogador[1]:
                    self.prioridade = 'cima'
                else:
                    self.prioridade = 'baixo'

    def update(self):
        if self.perdido:
            self.mao_direita()
        else:
            self.define_prioridade()
            self.escolhe_direcao()

        if self.direcao['direita']:
            self.rect.x += VELOCIDADE
        elif self.direcao['esquerda']:
            self.rect.x -= VELOCIDADE
        elif self.direcao['cima']:
            self.rect.y -= VELOCIDADE
        elif self.direcao['baixo']:
            self.rect.y += VELOCIDADE

        if self.rect.x < MARGEM_X+1:
            self.rect.x = (LARGURA_MAPA-1) * BLOCO + MARGEM_X
        elif self.rect.x > (LARGURA_MAPA-1) * BLOCO + MARGEM_X:
            self.rect.x = MARGEM_X+1

        if self.rect.collidelist(self.grupos['paredes']) != -1:
            if self.direcao['direita']:
                self.rect.x -= VELOCIDADE
            elif self.direcao['esquerda']:
                self.rect.x += VELOCIDADE
            elif self.direcao['cima']:
                self.rect.y += VELOCIDADE
            elif self.direcao['baixo']:
                self.rect.y -= VELOCIDADE