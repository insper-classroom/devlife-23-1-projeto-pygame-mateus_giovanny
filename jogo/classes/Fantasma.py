import pygame
from constantes import *

class Fantasma(pygame.sprite.Sprite):
    def __init__(self, grupos, img, x, y):
        super().__init__()

        self.img = img
        self.grupos = grupos
        self.grupos['all_sprites'].add(self)
        self.grupos['fantasmas'].add(self)
        self.image = img
        self.rect = self.image.get_rect()
        self.pos_inicial = [x,y]
        self.rect.x = x
        self.rect.y = y
        self.velocidade = 5
        self.estado = {'perdido': False, 'fugindo': False, 'morto': False, 'mortes': 0, 'preso': True}
        self.direcao = {'direita': False, 'esquerda': False, 'cima': False, 'baixo': False}
        self.direcao_oposta = ''
        self.pos_jogador = None
        self.prox_direcao_jogador = None
        self.prioridade = ''
                
    
    def verifica_parede(self, x, y):
        if pygame.Rect(x, y, self.rect.width, self.rect.height).collidelist(self.grupos['paredes']) == -1:
            return True
        return False
    
    def reseta_direcao(self):
        self.direcao = {'direita': False, 'esquerda': False, 'cima': False, 'baixo': False}

    def mao_direita(self):
        if self.prioridade == 'direita':
            if self.verifica_parede(self.rect.x + self.velocidade, self.rect.y) and self.direcao_oposta != self.prioridade:
                self.estado['perdido'] = False
            elif self.verifica_parede(self.rect.x, self.rect.y - self.velocidade) and self.direcao_oposta != 'cima':
                self.reseta_direcao()
                self.direcao_oposta = 'baixo'
                self.direcao['cima'] = True
            elif self.verifica_parede(self.rect.x - self.velocidade, self.rect.y) and self.direcao_oposta != 'esquerda':
                self.reseta_direcao()
                self.direcao_oposta = 'direita'
                self.direcao['esquerda'] = True
            else:
                self.reseta_direcao()
                self.direcao_oposta = 'cima'
                self.direcao['baixo'] = True

        elif self.prioridade == 'esquerda':
            if self.verifica_parede(self.rect.x - self.velocidade, self.rect.y) and self.direcao_oposta != self.prioridade:
                self.estado['perdido'] = False
            elif self.verifica_parede(self.rect.x, self.rect.y + self.velocidade) and self.direcao_oposta != 'baixo':
                self.reseta_direcao()
                self.direcao_oposta = 'cima'
                self.direcao['baixo'] = True
            elif self.verifica_parede(self.rect.x + self.velocidade, self.rect.y) and self.direcao_oposta != 'direita':
                self.reseta_direcao()
                self.direcao_oposta = 'esquerda'
                self.direcao['direita'] = True
            else:
                self.reseta_direcao()
                self.direcao_oposta = 'baixo'
                self.direcao['cima'] = True

        elif self.prioridade == 'cima':
            if self.verifica_parede(self.rect.x, self.rect.y - self.velocidade) and self.direcao_oposta != self.prioridade:
                self.estado['perdido'] = False
            elif self.verifica_parede(self.rect.x - self.velocidade, self.rect.y) and self.direcao_oposta != 'esquerda':
                self.reseta_direcao()
                self.direcao_oposta = 'direita'
                self.direcao['esquerda'] = True
            elif self.verifica_parede(self.rect.x, self.rect.y + self.velocidade) and self.direcao_oposta != 'baixo':
                self.reseta_direcao()
                self.direcao_oposta = 'cima'
                self.direcao['baixo'] = True
            else:
                self.reseta_direcao()
                self.direcao_oposta = 'esquerda'
                self.direcao['direita'] = True

        elif self.prioridade == 'baixo':
            if self.verifica_parede(self.rect.x, self.rect.y + self.velocidade) and self.direcao_oposta != self.prioridade:
                self.estado['perdido'] = False
            elif self.verifica_parede(self.rect.x + self.velocidade, self.rect.y) and self.direcao_oposta != 'direita':
                self.reseta_direcao()
                self.direcao_oposta = 'esquerda'
                self.direcao['direita'] = True
            elif self.verifica_parede(self.rect.x, self.rect.y - self.velocidade) and self.direcao_oposta != 'cima':
                self.reseta_direcao()
                self.direcao_oposta = 'baixo'
                self.direcao['cima'] = True
            else:
                self.reseta_direcao()
                self.direcao_oposta = 'direita'
                self.direcao['esquerda'] = True

    def escolhe_direcao(self):
        pass

    def escolhe_direcao_morto(self):
        if self.prioridade == 'direita':
            if self.verifica_parede(self.rect.x + self.velocidade, self.rect.y) and self.direcao_oposta != 'direita':
                self.direcao_oposta = 'esquerda'
                self.reseta_direcao()
                self.direcao['direita'] = True
            else:
                if self.verifica_parede(self.rect.x, self.rect.y - self.velocidade) and self.rect.y > self.pos_inicial[1] and self.direcao_oposta != 'cima':
                    self.direcao_oposta = 'baixo'
                    self.reseta_direcao()
                    self.direcao['cima'] = True
                elif self.verifica_parede(self.rect.x, self.rect.y + self.velocidade):
                    self.direcao_oposta = 'cima'
                    self.reseta_direcao()
                    self.direcao['baixo'] = True
                else:
                    self.estado['perdido'] = True
                    self.reseta_direcao()
        
        elif self.prioridade == 'esquerda':
            if self.verifica_parede(self.rect.x - self.velocidade, self.rect.y) and self.direcao_oposta != 'esquerda':
                self.direcao_oposta = 'direita'
                self.reseta_direcao()
                self.direcao['esquerda'] = True
            else:
                if self.verifica_parede(self.rect.x, self.rect.y - self.velocidade) and self.rect.y > self.pos_inicial[1] and self.direcao_oposta != 'cima':
                    self.direcao_oposta = 'baixo'
                    self.reseta_direcao()
                    self.direcao['cima'] = True
                elif self.verifica_parede(self.rect.x, self.rect.y + self.velocidade):
                    self.direcao_oposta = 'cima'
                    self.reseta_direcao()
                    self.direcao['baixo'] = True
                else:
                    self.estado['perdido'] = True
                    self.reseta_direcao()
        
        elif self.prioridade == 'cima':
            if self.verifica_parede(self.rect.x, self.rect.y - self.velocidade) and self.direcao_oposta != 'cima':
                self.direcao_oposta = 'baixo'
                self.reseta_direcao()
                self.direcao['cima'] = True
            else:
                if self.verifica_parede(self.rect.x - self.velocidade, self.rect.y) and self.rect.x > self.pos_inicial[0] and self.direcao_oposta != 'esquerda':
                    self.direcao_oposta = 'direita'
                    self.reseta_direcao()
                    self.direcao['esquerda'] = True
                elif self.verifica_parede(self.rect.x + self.velocidade, self.rect.y):
                    self.direcao_oposta = 'esquerda'
                    self.reseta_direcao()
                    self.direcao['direita'] = True
                else:
                    self.estado['perdido'] = True
                    self.reseta_direcao()
        
        elif self.prioridade == 'baixo':
            if self.verifica_parede(self.rect.x, self.rect.y + self.velocidade) and self.direcao_oposta != 'baixo':
                self.direcao_oposta = 'cima'
                self.reseta_direcao()
                self.direcao['baixo'] = True
            else:
                if self.verifica_parede(self.rect.x - self.velocidade, self.rect.y) and self.rect.x > self.pos_inicial[0] and self.direcao_oposta != 'esquerda':
                    self.direcao_oposta = 'direita'
                    self.reseta_direcao()
                    self.direcao['esquerda'] = True
                elif self.verifica_parede(self.rect.x + self.velocidade, self.rect.y):
                    self.direcao_oposta = 'esquerda'
                    self.reseta_direcao()
                    self.direcao['direita'] = True
                else:
                    self.estado['perdido'] = True
                    self.reseta_direcao()

    def escolhe_direcao_fugindo(self):
        if self.prioridade == 'direita':
            if self.verifica_parede(self.rect.x + self.velocidade, self.rect.y) and self.direcao_oposta != 'direita':
                self.direcao_oposta = 'esquerda'
                self.reseta_direcao()
                self.direcao['direita'] = True
            else:
                if self.verifica_parede(self.rect.x, self.rect.y - self.velocidade) and self.rect.y < self.pos_jogador[1] and self.direcao_oposta != 'cima':
                    self.direcao_oposta = 'baixo'
                    self.reseta_direcao()
                    self.direcao['cima'] = True
                elif self.verifica_parede(self.rect.x, self.rect.y + self.velocidade):
                    self.direcao_oposta = 'cima'
                    self.reseta_direcao()
                    self.direcao['baixo'] = True
                else:
                    self.estado['perdido'] = True
                    self.reseta_direcao()
        
        elif self.prioridade == 'esquerda':
            if self.verifica_parede(self.rect.x - self.velocidade, self.rect.y) and self.direcao_oposta != 'esquerda':
                self.direcao_oposta = 'direita'
                self.reseta_direcao()
                self.direcao['esquerda'] = True
            else:
                if self.verifica_parede(self.rect.x, self.rect.y - self.velocidade) and self.rect.y < self.pos_jogador[1] and self.direcao_oposta != 'cima':
                    self.direcao_oposta = 'baixo'
                    self.reseta_direcao()
                    self.direcao['cima'] = True
                elif self.verifica_parede(self.rect.x, self.rect.y + self.velocidade):
                    self.direcao_oposta = 'cima'
                    self.reseta_direcao()
                    self.direcao['baixo'] = True
                else:
                    self.estado['perdido'] = True
                    self.reseta_direcao()
        
        elif self.prioridade == 'cima':
            if self.verifica_parede(self.rect.x, self.rect.y - self.velocidade) and self.direcao_oposta != 'cima':
                self.direcao_oposta = 'baixo'
                self.reseta_direcao()
                self.direcao['cima'] = True
            else:
                if self.verifica_parede(self.rect.x - self.velocidade, self.rect.y) and self.rect.x < self.pos_jogador[0] and self.direcao_oposta != 'esquerda':
                    self.direcao_oposta = 'direita'
                    self.reseta_direcao()
                    self.direcao['esquerda'] = True
                elif self.verifica_parede(self.rect.x + self.velocidade, self.rect.y):
                    self.direcao_oposta = 'esquerda'
                    self.reseta_direcao()
                    self.direcao['direita'] = True
                else:
                    self.estado['perdido'] = True
                    self.reseta_direcao()
        
        elif self.prioridade == 'baixo':
            if self.verifica_parede(self.rect.x, self.rect.y + self.velocidade) and self.direcao_oposta != 'baixo':
                self.direcao_oposta = 'cima'
                self.reseta_direcao()
                self.direcao['baixo'] = True
            else:
                if self.verifica_parede(self.rect.x - self.velocidade, self.rect.y) and self.rect.x < self.pos_jogador[0] and self.direcao_oposta != 'esquerda':
                    self.direcao_oposta = 'direita'
                    self.reseta_direcao()
                    self.direcao['esquerda'] = True
                elif self.verifica_parede(self.rect.x + self.velocidade, self.rect.y):
                    self.direcao_oposta = 'esquerda'
                    self.reseta_direcao()
                    self.direcao['direita'] = True
                else:
                    self.estado['perdido'] = True
                    self.reseta_direcao()

    def define_prioridade_fugindo(self):
        if abs(self.rect.x - self.pos_jogador[0]) < abs(self.rect.y - self.pos_jogador[1]):
            if self.rect.x > self.pos_jogador[0]:
                self.prioridade = 'direita'
            else:
                self.prioridade = 'esquerda'
        else:
            if self.rect.y > self.pos_jogador[1]:
                self.prioridade = 'baixo'
            else:
                self.prioridade = 'cima'

    def define_prioridade_morto(self):
        if self.pos_inicial[0] - self.velocidade <= self.rect.x <= self.pos_inicial[0] + self.velocidade and self.pos_inicial[1] - self.velocidade <= self.rect.y <= self.pos_inicial[1] + self.velocidade:
            self.estado['morto'] = False
            self.estado['preso'] = True
        if abs(self.rect.x - self.pos_inicial[0]) > abs(self.rect.y - self.pos_inicial[1]):
            if self.rect.x > self.pos_inicial[0]:
                self.prioridade = 'esquerda'
            else:
                self.prioridade = 'direita'
        else:
            if self.rect.y > self.pos_inicial[1]:
                self.prioridade = 'cima'
            else:
                self.prioridade = 'baixo'

    def define_prioridade(self):
        pass

    def update(self):

        if self.estado['perdido']:
            self.mao_direita()
        else:
            if self.estado['morto']:
                self.define_prioridade_morto()
                self.escolhe_direcao_morto()
            elif self.estado['fugindo']:
                self.define_prioridade_fugindo()
                self.escolhe_direcao_fugindo()
            else:
                self.escolhe_direcao()
                self.define_prioridade()

        if self.estado['preso']:
            pass
        else:
            if self.direcao['direita']:
                self.rect.x += self.velocidade
            elif self.direcao['esquerda']:
                self.rect.x -= self.velocidade
            elif self.direcao['cima']:
                self.rect.y -= self.velocidade
            elif self.direcao['baixo']:
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

        if self.estado['morto']:
            self.estado['fugindo'] =  False
            self.image = FANTASMA_MORTO

        if not self.estado['fugindo'] and not self.estado['morto']:
            self.image = self.img