import pygame
from constantes import *
from classes.Jogo import Jogo

if __name__ == '__main__':
    jogo = Jogo()
    jogo.game_loop()
    jogo.finaliza()

    