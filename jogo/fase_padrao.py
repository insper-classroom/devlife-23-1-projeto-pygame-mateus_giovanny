from abc import ABC, abstractclassmethod
from constantes import *

class Fase(ABC):
    def gera_paredes_em_volta(self):
        BLOCO = max(TAMANHO_JANELA[0] // LARGURA_MAPA, TAMANHO_JANELA[1] // ALTURA_MAPA)
        for y in range(ALTURA_MAPA):
            for x in range(LARGURA_MAPA):
                if (x == 0 or y == 0) or (x == LARGURA_MAPA-1 or y == ALTURA_MAPA-1):
                    rect = pygame.Rect(x * BLOCO + MARGEM, y * BLOCO + MARGEM, BLOCO, BLOCO)
                    pygame.draw.rect(JANELA, AZUL, rect)

    def gera_mapa(self):
        self.gera_paredes_em_volta()