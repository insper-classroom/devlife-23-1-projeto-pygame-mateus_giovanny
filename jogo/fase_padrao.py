from abc import ABC, abstractclassmethod
from constantes import *
from random import randint

class Fase(ABC):
    def gera_mapa(self):
        with open('jogo/mapas/mapa1.txt','w') as mapa1:
            for y in range(ALTURA_MAPA):
                if y != 0:
                    mapa1.write('\n')
                for x in range(LARGURA_MAPA):
                    if (x == 0 or y == 0) or (x == LARGURA_MAPA - 1 or y == ALTURA_MAPA - 1):
                        mapa1.write('1')
                    else:
                        mapa1.write('2')
    # @abstractclassmethod
    def desenha_mapa(self):
        with open('jogo/mapas/mapa1.txt','r') as mapa1:
            for y in range(ALTURA_MAPA):
                linha = mapa1.readline()
                for x in range(len(linha)):
                    if linha[x] == '1':
                        rect = pygame.Rect(x * BLOCO + MARGEM, y * BLOCO + MARGEM, BLOCO, BLOCO)
                        pygame.draw.rect(JANELA, AZUL, rect)
                    elif linha[x] == '2':
                        pos_x = x * BLOCO + BLOCO // 2 + MARGEM
                        pos_y = y * BLOCO + BLOCO // 2 + MARGEM
                        raio = BLOCO // 10
                        pygame.draw.circle(JANELA, AMARELO_PONTOS, (pos_x, pos_y), raio)