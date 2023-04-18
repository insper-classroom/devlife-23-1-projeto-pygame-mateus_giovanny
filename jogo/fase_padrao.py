from abc import ABC, abstractclassmethod
from constantes import *
from random import randint

class Fase(ABC):
    def gera_mapa(self):
        with open('jogo/mapas/mapa1.txt','w') as mapa1:
            for y in range(ALTURA_MAPA):
                for x in range(LARGURA_MAPA):
                    if (x == 0 or y == 0) or (x == LARGURA_MAPA - 1 or y == ALTURA_MAPA - 1):
                        mapa1.write('1')
                    else:
                        mapa1.write(f'{randint(1,2)}')
    
    # def desenha_mapa(self):
    #     with open('jogo/mapas/mapa1.txt','r') as mapa1:
            