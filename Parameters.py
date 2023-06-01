import pygame
from Board import Board
from turtledemo import clock

pygame.init()

icon = pygame.image.load('images/chess_icon.png')
menu_bckgr = pygame.image.load('images/Chess_background_menu.jpg')
button_sound = pygame.mixer.Sound('sound/sound_button.wav')
pygame.display.set_icon(icon)
display_size = width, height = (600, 600)
display = pygame.display.set_mode(display_size)
pygame.display.set_caption('Chess')
board = Board(display_size[0], display_size[1])
ARIAL_50 = pygame.font.SysFont('arial', 50)
clock = pygame.time.Clock()