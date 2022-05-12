import pygame

class FallingObject(pygame.sprite.Sprite):
	def __init__(self, x, y, file_name):
		'''creates faling object sprite '''
		super().__init__()
		self.image = pygame.image.load(file_name)
		self.image = pygame.transform.smoothscale(self.image, (50, 50))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.speed = 5
		
	def update(self):
		self.rect.y+=3