from abc import ABC, abstractclassmethod
from constantes import *
from random import randint

class Fase(ABC):
    def gera_posicao_desocupada(self):
        x = randint(1, LARGURA_MAPA-2)
        y = randint(1, ALTURA_MAPA-2)
        posicao = [x, y]
        
        while posicao in POSICOES_OCUPADAS:
            x = randint(1, LARGURA_MAPA-2)
            y = randint(1, ALTURA_MAPA-2)
            posicao = [x, y]
        
        POSICOES_OCUPADAS.append(posicao)
        return posicao
    
    def gera_paredes_em_volta(self):
        for y in range(ALTURA_MAPA):
            for x in range(LARGURA_MAPA):
                if (x == 0 or y == 0) or (x == LARGURA_MAPA-1 or y == ALTURA_MAPA-1):
                    POSICOES_OCUPADAS.append([x,y])
                    rect = pygame.Rect(x * BLOCO + MARGEM, y * BLOCO + MARGEM, BLOCO, BLOCO)
                    OBJETOS.append({'cor':AZUL,
                                    'rect':rect})

    def gera_paredes_retangulo(self):
        posicao = self.gera_posicao_desocupada()
        for i in range(12):
            if posicao[1] < ALTURA_MAPA:
                    posicao = [posicao[0], posicao[1]]
                    if not posicao in POSICOES_OCUPADAS:
                        POSICOES_OCUPADAS.append(posicao)
                        rect = pygame.Rect(posicao[0] * BLOCO + MARGEM, posicao[1] * BLOCO + MARGEM, BLOCO, BLOCO)
                        OBJETOS.append({'cor':AZUL,
                                        'rect':rect})
            posicao[1] += 1
        for i in range(8):
            if posicao[0] < LARGURA_MAPA:
                posicao = [posicao[0], posicao[1]]
                if not posicao in POSICOES_OCUPADAS:
                    POSICOES_OCUPADAS.append(posicao)
                    rect = pygame.Rect(posicao[0] * BLOCO + MARGEM, posicao[1] * BLOCO + MARGEM, BLOCO, BLOCO)
                    OBJETOS.append({'cor':AZUL,
                                    'rect':rect})
            posicao[0] += 1
    def gera_mapa(self):
        self.gera_paredes_em_volta()
        self.gera_paredes_retangulo()