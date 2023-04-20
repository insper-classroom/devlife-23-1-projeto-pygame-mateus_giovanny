import pygame
from constantes import *
class Jogo:
    def __init__(self):
        pygame.init()
        self.tela_atual = Fase1()

    def atualiza(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
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
        # self.gera_mapa()
        self.mapa_img = pygame.image.load('jogo/assets\img\mapa.png')
    
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

    def desenha(self):
        with open('jogo/mapas/mapa1.txt','r') as mapa1:
            for y in range(ALTURA_MAPA):
                linha = mapa1.readline()
                for x in range(len(linha)):
                    if linha[x] == '1':
                        rect = pygame.Rect(x * BLOCO + MARGEM_X, y * BLOCO + MARGEM_Y, BLOCO, BLOCO)
                        pygame.draw.rect(JANELA, AZUL, rect, 1)
                    elif linha[x] == '2':
                        pos_x = x * BLOCO + BLOCO // 2 + MARGEM_X
                        pos_y = y * BLOCO + BLOCO // 2 + MARGEM_Y
                        raio = BLOCO // 10
                        pygame.draw.circle(JANELA, AMARELO_PONTOS, (pos_x, pos_y), raio)
                    # elif linha[x] == '0':
                    #     pos_x = x * BLOCO + BLOCO // 2 + MARGEM_X
                    #     pos_y = y * BLOCO + BLOCO // 2 + MARGEM
                    #     raio = BLOCO // 2.5
                    #     pygame.draw.circle(JANELA, AMARELO_PONTOS, (pos_x, pos_y), raio)

if __name__ == '__main__':
    jogo = Jogo()
    jogo.game_loop()
    jogo.finaliza()