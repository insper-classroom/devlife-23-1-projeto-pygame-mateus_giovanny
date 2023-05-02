from classes.Fantasma import Fantasma
from constantes import *
from random import randint

class Clyde(Fantasma):
    def __init__(self, grupos, img):
        x = (LARGURA_MAPA//2) * BLOCO + MARGEM_X +2
        y = (ALTURA_MAPA//2 -5) * BLOCO + MARGEM_Y +2
        super().__init__(grupos, img, x, y)
        self.cor = 'LARANJA'

    def define_prioridade(self):
        direcao = randint(1,4)
        if direcao == 1:
            self.prioridade = 'cima'
        elif direcao == 2:
            self.prioridade = 'direita'
        elif direcao == 3:
            self.prioridade = 'baixo'
        elif direcao == 4:
            self.prioridade = 'esquerda'

    def escolhe_direcao(self):
        if self.prioridade == 'direita':
            if self.verifica_parede(self.rect.x + self.velocidade, self.rect.y) and self.direcao_oposta != 'direita':
                self.direcao_oposta = 'esquerda'
                self.reseta_direcao()
                self.direcao['direita'] = True
            else:
                if randint(0,1) and self.verifica_parede(self.rect.x, self.rect.y - self.velocidade) and self.direcao_oposta != 'cima':
                    self.direcao_oposta = 'baixo'
                    self.reseta_direcao()
                    self.direcao['cima'] = True
                elif self.verifica_parede(self.rect.x, self.rect.y + self.velocidade) and self.direcao_oposta != 'baixo':
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
                if randint(0,1) and self.verifica_parede(self.rect.x, self.rect.y - self.velocidade) and self.direcao_oposta != 'cima':
                    self.direcao_oposta = 'baixo'
                    self.reseta_direcao()
                    self.direcao['cima'] = True
                elif self.verifica_parede(self.rect.x, self.rect.y + self.velocidade) and self.direcao_oposta != 'baixo':
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
                if randint(0,1) and self.verifica_parede(self.rect.x - self.velocidade, self.rect.y) and self.direcao_oposta != 'esquerda':
                    self.direcao_oposta = 'direita'
                    self.reseta_direcao()
                    self.direcao['esquerda'] = True
                elif self.verifica_parede(self.rect.x + self.velocidade, self.rect.y) and self.direcao_oposta != 'direita':
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
                if randint(0,1) and self.verifica_parede(self.rect.x - self.velocidade, self.rect.y) and self.direcao_oposta != 'esquerda':
                    self.direcao_oposta = 'direita'
                    self.reseta_direcao()
                    self.direcao['esquerda'] = True
                elif self.verifica_parede(self.rect.x + self.velocidade, self.rect.y) and self.direcao_oposta != 'direita':
                    self.direcao_oposta = 'esquerda'
                    self.reseta_direcao()
                    self.direcao['direita'] = True
                else:
                    self.estado['perdido'] = True
                    self.reseta_direcao()