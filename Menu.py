import pygame
from Button import *
from Game import *

pygame.init()


def print_text(message, x, y, font_size, font_color=(0, 0, 0), font_type='fonts/chess_fonts3.ttf'):
    font_type = pygame.font.Font(font_type, font_size)
    text = font_type.render(message, True, font_color)
    display.blit(text, (x, y))


def pause():
    paused = True
    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        print_text('Pause', 212, 244, 50)
        print_text('Press SPACE to continue', 94, 320, 28)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            paused = False

        pygame.display.update()
        clock.tick(15)


def show_menu():
    global menu_bckgr
    start_button = Button(416, 70)
    quit_button = Button(344, 70)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        display.blit(menu_bckgr, (0, 0))
        print_text("It's time to win!", 41, 60, 56, font_color=(255, 0, 0))
        start_button.draw(92, 200, 'Start Game', game_cycle, 55)
        quit_button.draw(128, 320, 'Quit Game', quit, 55)
        pygame.display.update()
        clock.tick(60)
    quit()


def game_over():
    from Piece import num_moves
    from Board import white_num_moves, black_num_moves
    global menu_bckgr
    quit_button = Button(344, 70)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        display.blit(menu_bckgr, (0, 0))
        quit_button.draw(128, 240, 'Quit Game', quit, 55)
        if board.is_in_checkmate('black'):
            print_text('White WON!', 112, 50, 60)
            print_text('Click on "Quit Game"', 120, 140, 30)
            print_text('to end the game', 148, 170, 30)
            print_text('Total moves: ' + str(num_moves), 10, 355, 25)
            print_text('Black moves: ' + str(black_num_moves), 10, 390, 25)
            print_text('White moves: ' + str(white_num_moves), 10, 425, 25)
        elif board.is_in_checkmate('white'):
            print_text('Black WON!', 110, 50, 60)
            print_text('Click on "Quit Game"', 120, 140, 30)
            print_text('to end the game', 148, 170, 30)
            print_text('Total moves: ' + str(num_moves), 10, 355, 25)
            print_text('Black moves: ' + str(black_num_moves), 10, 390, 25)
            print_text('White moves: ' + str(white_num_moves), 10, 425, 25)
        pygame.display.update()
        clock.tick(60)
    quit()