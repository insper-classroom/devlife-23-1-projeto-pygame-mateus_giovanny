import pygame
from constantes import *

class Jogador(pygame.sprite.Sprite):
    """
    classe que representa o jogador

    ...

    Atributos
    ---------
    grupos : dict
        dicionario onde eu guardo os grupos de sprites e listas de retangulos que a classe usa pra colisao
    image : pygame.surface
        é a imagem que vai ser blitada na tela
    rect : pygame.Rect
        é o retangulo do jogador
    direcao : dict
        é um dicionario que indica em qual direcao o jogador está indo
    comedor : bool
        é um estado do jogador que indica que ele comeu um come-fantasmas
    index : int
        usado pra fazer a animacao da boca do pac man
    velocidade : int
        velocidade de movimento do jogador
    prox_direcao : str
        string contendo a direcao desejada pelo jogador
    """
    def __init__(self, grupos):
        """
        Parâmetros
        ----------
        grupos : dict
            dicionario onde eu guardo os grupos de sprites e listas de retangulos que a classe usa pra colisao
        """
        super().__init__()
        self.grupos = grupos
        self.grupos['all_sprites'].add(self)
        self.image = PAC_MAN
        self.rect = self.image.get_rect()
        self.rect.x = (LARGURA_MAPA//2) * BLOCO + MARGEM_X +2
        self.rect.y = (ALTURA_MAPA//2) * BLOCO + MARGEM_Y +2
        self.direcao = {'direita': False, 'esquerda': False, 'cima': False, 'baixo': False}
        self.prox_direcao = ''
        self.comedor = False
        self.velocidade = VELOCIDADE
        self.index = 1
        COMENDO.set_volume(0.5)
        COMENDO_POWER.set_volume(0.5)

    def update(self):
        """
        atualiza a posição do jogador, verifica as colisoes com objetos e muda a imagem fazendo a animação
        """
        if self.index == 4:
            self.index = 1
            
        self.pontuacao = 0
        if self.direcao['direita']:
            self.image = pygame.transform.scale(pygame.image.load(f'assets\img\PACs/direita{self.index}.png'), TAMANHO_JOGADOR)
            self.rect.x += self.velocidade
        elif self.direcao['esquerda']:
            self.image = pygame.transform.scale(pygame.image.load(f'assets\img\PACs/esquerda{self.index}.png'), TAMANHO_JOGADOR)
            self.rect.x -= self.velocidade
        elif self.direcao['cima']:
            self.image = pygame.transform.scale(pygame.image.load(f'assets\img\PACs/cima{self.index}.png'), TAMANHO_JOGADOR)
            self.rect.y -= self.velocidade
        elif self.direcao['baixo']:
            self.image = pygame.transform.scale(pygame.image.load(f'assets\img\PACs/baixo{self.index}.png'), TAMANHO_JOGADOR)
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
            # COMENDO.play(0, 105)
            COMENDO_POWER.play(0,105)
            del self.grupos['bolinhas'][index]
            self.pontuacao += 10

        index = self.rect.collidelist(self.grupos['come_fantasma'])
        if index != -1:
            COMENDO_POWER.play(0,105)
            del self.grupos['come_fantasma'][index]

            

    def reseta_direcao(self):
        """
        reseta o dicionario de direcao, para o pac man não tentar ir em duas direcoes ao mesmo tempo
        """
        self.direcao = {'direita': False, 'esquerda': False, 'cima': False, 'baixo': False}

    def verifica_direcao_livre(self):
        """
        verifica se o pac man pode ir pra uma direcao
        """
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