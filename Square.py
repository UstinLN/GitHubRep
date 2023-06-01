import pygame


class Square:
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.abs_x = x * width
		self.abs_y = y * height
		self.abs_pos = (self.abs_x, self.abs_y)
		self.pos = (x, y)
		if (x + y) % 2 == 0:
			self.color = 'light'
		else:
			self.color = 'dark'
		if self.color == 'light':
			self.draw_color = (248, 231, 216)
		else:
			self.draw_color = (90, 61, 48)
		if self.color == 'light':
			self.highlight_color = (204, 247, 159)
		else:
			self.highlight_color = (127, 247, 159)
		self.occupying_piece = None
		self.coord = self.get_coord()
		self.highlight = False
		self.rect = pygame.Rect(self.abs_x, self.abs_y, self.width, self.height)

	def get_coord(self):
		columns = 'abcdefgh'
		return columns[self.x] + str(self.y + 1)

	def draw(self, display):
		if self.highlight:
			pygame.draw.rect(display, self.highlight_color, self.rect)
		else:
			pygame.draw.rect(display, self.draw_color, self.rect)
		if self.occupying_piece is not None:
			centering_rect = self.occupying_piece.img.get_rect()
			centering_rect.center = self.rect.center
			display.blit(self.occupying_piece.img, centering_rect.topleft)