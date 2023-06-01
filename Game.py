import pygame
from Parameters import *
from Menu import *


def draw(display):
    display.fill('white')
    board.draw(display)
    pygame.display.update()


def game_cycle():
    running_game = True
    while running_game:
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_game = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    board.handle_click(mx, my)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            from Menu import pause
            pause()
        if board.is_in_checkmate('black'):
            from Menu import game_over
            game_over()
            running_game = False
        elif board.is_in_checkmate('white'):
            from Menu import game_over
            game_over()
            running_game = False
        pygame.display.update()
        draw(display)