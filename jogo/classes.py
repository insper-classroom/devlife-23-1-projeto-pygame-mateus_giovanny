import pygame
from constantes import *
import math
import heapq
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
        # self.fatasma_vermelho.update_caminho()
        self.grupos['all_sprites'].update()
        self.jogador.verifica_direcao_livre()
        # self.fatasma_vermelho.verifica_direcao_livre()
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

class No(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.pos = (x,y)
        self.vizinhos = []
        self.pai = None

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
        self.direcao_anterior = None

        self.pos_jogador = None
        self.pos_navegaveis = pos_navegaveis
        self.caminho = []
        self.celula_alvo = None
        self.contador = 0

        self.prioridade = ''

    def update_caminho(self):
        no_atual = No(self.rect.x, self.rect.y)
        no_final = No(self.pos_jogador[0], self.pos_jogador[1])
        visitados = []
        para = False

        if no_atual.pos not in visitados:
            self.visita(no_atual, visitados, no_final, para)

    def visita(self, no, visitados, no_final, para):
        visitados.append(no.pos)
        self.add_vizinhos(no, visitados)
        for no_vizinho in no.vizinhos:
            if para:
                return
            if no_vizinho.pos not in visitados:
                no_vizinho.pai = no
                if no_vizinho.pos == no_final.pos:
                    print(1)
                    para = True
                    return
                self.visita(no_vizinho, visitados, no_final, para)

    def add_vizinhos(self, no_atual, visitados):
        if no_atual.x > MARGEM_X:
            if self.verifica_parede((no_atual.x - VELOCIDADE, no_atual.y)):
                novo_no = No(no_atual.x - VELOCIDADE, no_atual.y)
                if novo_no.pos not in visitados:
                    no_atual.vizinhos.append(novo_no)

        if no_atual.x < (LARGURA_MAPA * BLOCO + MARGEM_X) - 1:
            if self.verifica_parede((no_atual.x + VELOCIDADE, no_atual.y)):
                novo_no = No(no_atual.x + VELOCIDADE, no_atual.y)
                if novo_no.pos not in visitados:
                    no_atual.vizinhos.append(novo_no)

        if no_atual.y > MARGEM_Y:
            if self.verifica_parede((no_atual.x, no_atual.y - VELOCIDADE)):
                novo_no = No(no_atual.x, no_atual.y - VELOCIDADE)
                if novo_no.pos not in visitados:
                    no_atual.vizinhos.append(novo_no)

        if no_atual.y < (ALTURA_MAPA * BLOCO + MARGEM_Y) - 1:
            if self.verifica_parede((no_atual.x, no_atual.y + VELOCIDADE)):
                novo_no = No(no_atual.x, no_atual.y + VELOCIDADE)
                if novo_no.pos not in visitados:
                    no_atual.vizinhos.append(novo_no)
                
    
    def verifica_parede(self, x, y):
        if pygame.Rect(x, y, self.rect.width, self.rect.height).collidelist(self.grupos['paredes']) == -1:
            return True
        return False
    
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

    def escolhe_direcao(self):
        if self.prioridade == 'direita':
            if self.verifica_parede(self.rect.x + VELOCIDADE, self.rect.y):
                self.reseta_direcao()
                self.direcao['direita'] = True
            else:
                self.prox_direcao = 'direita'
                if self.rect.y > self.pos_jogador[1]:
                    self.reseta_direcao()
                    self.direcao['cima'] = True
                else:
                    self.reseta_direcao()
                    self.direcao['baixo'] = True
        elif self.prioridade == 'esquerda':
            if self.verifica_parede(self.rect.x - VELOCIDADE, self.rect.y):
                self.reseta_direcao()
                self.direcao['esquerda'] = True
            else:
                self.prox_direcao = 'esquerda'
                if self.rect.y > self.pos_jogador[1]:
                    self.reseta_direcao()
                    self.direcao['cima'] = True
                else:
                    self.reseta_direcao()
                    self.direcao['baixo'] = True
        elif self.prioridade == 'cima':
            if self.verifica_parede(self.rect.x, self.rect.y - VELOCIDADE):
                self.reseta_direcao()
                self.direcao['cima'] = True
            else:
                self.prox_direcao = 'cima'
                if self.rect.x > self.pos_jogador[0]:
                    self.reseta_direcao()
                    self.direcao['esquerda'] = True
                else:
                    self.reseta_direcao()
                    self.direcao['direita'] = True
        elif self.prioridade == 'baixo':
            if self.verifica_parede(self.rect.x, self.rect.y + VELOCIDADE):
                self.reseta_direcao()
                self.direcao['baixo'] = True
            else:
                self.prox_direcao = 'baixo'
                if self.rect.x > self.pos_jogador[0]:
                    self.reseta_direcao()
                    self.direcao['esquerda'] = True
                else:
                    self.reseta_direcao()
                    self.direcao['direita'] = True
        # tentar fazer a ideia do A* mas dessa vez fazer um lista com as direcoes e não com as posicoes

        # for i in range(2):
        #     menor_distancia = math.inf

        #     distancia = self.distancia_euclidiana(self.rect.x + VELOCIDADE, self.rect.y, self.pos_jogador[0], self.pos_jogador[1])
        #     if distancia < menor_distancia and 'direita' not in self.prox_direcao and self.verifica_parede((self.rect.x + VELOCIDADE, self.rect.y, self.pos_jogador[0])) and self.direcao_anterior != 'direita':
        #         menor_distancia = distancia
        #         direcao = 'direita'
        #     distancia = self.distancia_euclidiana(self.rect.x - VELOCIDADE, self.rect.y, self.pos_jogador[0], self.pos_jogador[1])
        #     if distancia < menor_distancia and 'esquerda' not in self.prox_direcao and self.verifica_parede((self.rect.x - VELOCIDADE, self.rect.y)) and self.direcao_anterior != 'esquerda':
        #         menor_distancia = distancia
        #         direcao = 'esquerda'
        #     distancia = self.distancia_euclidiana(self.rect.x, self.rect.y + VELOCIDADE, self.pos_jogador[0], self.pos_jogador[1])
        #     if distancia < menor_distancia and 'baixo' not in self.prox_direcao and self.verifica_parede((self.rect.x, self.rect.y + VELOCIDADE)) and self.direcao_anterior != 'baixo':
        #         menor_distancia = distancia
        #         direcao = 'baixo'
        #     distancia = self.distancia_euclidiana(self.rect.x, self.rect.y - VELOCIDADE, self.pos_jogador[0], self.pos_jogador[1])
        #     if distancia < menor_distancia and 'cima' not in self.prox_direcao and self.verifica_parede((self.rect.x, self.rect.y - VELOCIDADE)) and self.direcao_anterior != 'cima':
        #         menor_distancia = distancia
        #         direcao = 'cima'

        #     self.prox_direcao.append(direcao)
        

    def define_prioridade(self):
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

        if self.rect.x < MARGEM_X:
            self.rect.x = LARGURA_MAPA * BLOCO + MARGEM_X
        elif self.rect.x > LARGURA_MAPA * BLOCO + MARGEM_X:
            self.rect.x = MARGEM_X

        # if self.rect.collidelist(self.grupos['paredes']) != -1:
        #     if self.direcao['direita']:
        #         self.rect.x -= VELOCIDADE
        #         self.direcao_anterior = self.prox_direcao.pop(0)
        #         # self.escolhe_direcao()
        #     elif self.direcao['esquerda']:
        #         self.rect.x += VELOCIDADE
        #         self.direcao_anterior = self.prox_direcao.pop(0)
        #         # self.escolhe_direcao()
        #     elif self.direcao['cima']:
        #         self.rect.y += VELOCIDADE
        #         self.direcao_anterior = self.prox_direcao.pop(0)
        #         # self.escolhe_direcao()
        #     elif self.direcao['baixo']:
        #         self.rect.y -= VELOCIDADE
        #         self.direcao_anterior = self.prox_direcao.pop(0)

                # self.escolhe_direcao()
        # if self.celula_alvo:
        #     dx = self.celula_alvo.x - self.rect.x
        #     dy = self.celula_alvo.y - self.rect.y
        #     distancia = math.sqrt(dx**2 + dy**2)
        #     if distancia > 0:
        #         dx /= distancia
        #         dy /= distancia
        #     self.rect.x += dx * VELOCIDADE
        #     self.rect.y += dy * VELOCIDADE

        #     if distancia < VELOCIDADE:
        #         if self.caminho:
        #             self.caminho.pop(0)
        #         self.celula_alvo = None

    def persegicao(self):
        abertas = []
        expandidas = []
        abertas.append((self.rect.x, self.rect.y))

        while len(abertas) > 0:
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