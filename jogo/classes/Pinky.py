from classes.Fantasma import Fantasma
from constantes import *

class Pinky(Fantasma):
    def __init__(self, grupos, img):
        x = (LARGURA_MAPA//2) * BLOCO + MARGEM_X +2
        y = (ALTURA_MAPA//2 -5) * BLOCO + MARGEM_Y +2
        super().__init__(grupos, img, x, y)
        self.cor = 'ROSA'

    def define_prioridade(self):
        if self.prox_direcao_jogador == 'direita':
            if abs(self.rect.x - self.pos_jogador[0] + VELOCIDADE) > abs(self.rect.y - self.pos_jogador[1]):
                if self.rect.x > self.pos_jogador[0] + VELOCIDADE:
                    self.prioridade = 'esquerda'
                else:
                    self.prioridade = 'direita'
            else:
                if self.rect.y > self.pos_jogador[1]:
                    self.prioridade = 'cima'
                else:
                    self.prioridade = 'baixo'
        
        elif self.prox_direcao_jogador == 'esquerda':
            if abs(self.rect.x - self.pos_jogador[0] - VELOCIDADE) > abs(self.rect.y - self.pos_jogador[1]):
                if self.rect.x > self.pos_jogador[0] - VELOCIDADE:
                    self.prioridade = 'esquerda'
                else:
                    self.prioridade = 'direita'
            else:
                if self.rect.y > self.pos_jogador[1]:
                    self.prioridade = 'cima'
                else:
                    self.prioridade = 'baixo'

        elif self.prox_direcao_jogador == 'cima':
            if abs(self.rect.x - self.pos_jogador[0]) > abs(self.rect.y - self.pos_jogador[1] - VELOCIDADE):
                if self.rect.x > self.pos_jogador[0]:
                    self.prioridade = 'esquerda'
                else:
                    self.prioridade = 'direita'
            else:
                if self.rect.y > self.pos_jogador[1] - VELOCIDADE:
                    self.prioridade = 'cima'
                else:
                    self.prioridade = 'baixo'
        
        elif self.prox_direcao_jogador == 'baixo':
            if abs(self.rect.x - self.pos_jogador[0]) > abs(self.rect.y - self.pos_jogador[1] + VELOCIDADE):
                if self.rect.x > self.pos_jogador[0]:
                    self.prioridade = 'esquerda'
                else:
                    self.prioridade = 'direita'
            else:
                if self.rect.y > self.pos_jogador[1] + VELOCIDADE:
                    self.prioridade = 'cima'
                else:
                    self.prioridade = 'baixo'

    def escolhe_direcao(self):
        if self.prioridade == 'direita':
            if self.verifica_parede(self.rect.x + self.velocidade, self.rect.y) and self.direcao_oposta != 'direita':
                self.direcao_oposta = 'esquerda'
                self.reseta_direcao()
                self.direcao['direita'] = True
            else:
                if self.verifica_parede(self.rect.x, self.rect.y - self.velocidade) and self.rect.y > self.pos_jogador[1] and self.direcao_oposta != 'cima':
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
                if self.verifica_parede(self.rect.x, self.rect.y - self.velocidade) and self.rect.y > self.pos_jogador[1] and self.direcao_oposta != 'cima':
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
                if self.verifica_parede(self.rect.x - self.velocidade, self.rect.y) and self.rect.x > self.pos_jogador[0] and self.direcao_oposta != 'esquerda':
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
                if self.verifica_parede(self.rect.x - self.velocidade, self.rect.y) and self.rect.x > self.pos_jogador[0] and self.direcao_oposta != 'esquerda':
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