import pygame

class FallingObject(pygame.sprite.Sprite):
	def __init__(self, x, y, file_name):
		'''creates faling object sprite '''
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(file_name)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.speed = 1
		
	def update(self):
		self.rect.y+=1