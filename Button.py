import pygame
from Parameters import *


class Button:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.inactive_clr = (30, 144, 255)
        self.active_clr = (23, 204, 58)

    def draw(self, x, y, message, action=None, font_size=30):
        mouse = pygame.mouse.get_pos()
        self.type_action = action
        click = pygame.mouse.get_pressed()
        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            pygame.draw.rect(display, self.active_clr, (x, y, self.width, self.height))
            if click[0] == 1 and action is not None:
                pygame.mixer.Sound.play(button_sound)
                pygame.time.delay(300)
                if action is not None:
                    if action == quit:
                        pygame.quit()
                        quit()
                    else:
                        action()
        else:
            pygame.draw.rect(display, self.inactive_clr, (x, y, self.width, self.height))

        from Menu import print_text
        print_text(message=message, x=x+10, y=y+10, font_size=font_size)