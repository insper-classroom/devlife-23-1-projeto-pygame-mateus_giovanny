from classes.Fantasma import Fantasma
from constantes import *
from random import randint

class Inky(Fantasma):
    def __init__(self, grupos, img):
        x = (LARGURA_MAPA//2) * BLOCO + MARGEM_X +2
        y = (ALTURA_MAPA//2 -5) * BLOCO + MARGEM_Y +2 
        super().__init__(grupos, img, x, y)
        self.zona = randint(1,4)
        self.cor = 'AZUL'

    def define_prioridade(self):
        if self.pos_jogador[0] < (LARGURA_MAPA//2) * BLOCO + MARGEM_X and self.pos_jogador[1] < (ALTURA_MAPA//2 -5) * BLOCO + MARGEM_Y:
            self.zona = 1
        elif self.pos_jogador[0] > (LARGURA_MAPA//2) * BLOCO + MARGEM_X and self.pos_jogador[1] < (ALTURA_MAPA//2 -5) * BLOCO + MARGEM_Y:
            self.zona = 2
        elif self.pos_jogador[0] > (LARGURA_MAPA//2) * BLOCO + MARGEM_X and self.pos_jogador[1] > (ALTURA_MAPA//2 -5) * BLOCO + MARGEM_Y:
            self.zona = 3
        elif self.pos_jogador[0] < (LARGURA_MAPA//2) * BLOCO + MARGEM_X and self.pos_jogador[1] > (ALTURA_MAPA//2 -5) * BLOCO + MARGEM_Y:
            self.zona = 4
            
        if self.zona == 1:
            if randint(0,1):
                self.prioridade = 'cima'
            else:
                self.prioridade = 'esquerda'
        elif self.zona == 2:
            if randint(0,1):
                self.prioridade = 'cima'
            else:
                self.prioridade = 'direita'
        elif self.zona == 3:
            if randint(0,1):
                self.prioridade = 'baixo'
            else:
                self.prioridade = 'direita'
        elif self.zona == 4:
            if randint(0,1):
                self.prioridade = 'baixo'
            else:
                self.prioridade = 'esquerda'

    def escolhe_direcao(self):
        if self.prioridade == 'direita':
            if self.verifica_parede(self.rect.x + self.velocidade, self.rect.y) and self.direcao_oposta != 'direita':
                self.direcao_oposta = 'esquerda'
                self.reseta_direcao()
                self.direcao['direita'] = True
            else:
                if self.zona == 2 and self.verifica_parede(self.rect.x, self.rect.y - self.velocidade) and self.direcao_oposta != 'cima':
                    self.direcao_oposta = 'baixo'
                    self.reseta_direcao()
                    self.direcao['cima'] = True
                elif self.zona == 3 and self.verifica_parede(self.rect.x, self.rect.y + self.velocidade) and self.direcao_oposta != 'baixo':
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
                if self.zona == 1 and self.verifica_parede(self.rect.x, self.rect.y - self.velocidade) and self.direcao_oposta != 'cima':
                    self.direcao_oposta = 'baixo'
                    self.reseta_direcao()
                    self.direcao['cima'] = True
                elif self.zona == 4 and self.verifica_parede(self.rect.x, self.rect.y + self.velocidade) and self.direcao_oposta != 'baixo':
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
                if self.zona == 1 and self.verifica_parede(self.rect.x - self.velocidade, self.rect.y) and self.direcao_oposta != 'esquerda':
                    self.direcao_oposta = 'direita'
                    self.reseta_direcao()
                    self.direcao['esquerda'] = True
                elif self.zona == 2 and self.verifica_parede(self.rect.x + self.velocidade, self.rect.y) and self.direcao_oposta != 'direita':
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
                if self.zona == 4 and self.verifica_parede(self.rect.x - self.velocidade, self.rect.y) and self.direcao_oposta != 'esquerda':
                    self.direcao_oposta = 'direita'
                    self.reseta_direcao()
                    self.direcao['esquerda'] = True
                elif self.zona == 3 and self.verifica_parede(self.rect.x + self.velocidade, self.rect.y) and self.direcao_oposta != 'direita':
                    self.direcao_oposta = 'esquerda'
                    self.reseta_direcao()
                    self.direcao['direita'] = True
                else:
                    self.estado['perdido'] = True
                    self.reseta_direcao()