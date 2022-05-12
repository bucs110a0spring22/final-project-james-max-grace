import pygame

class FallingObject(pygame.sprite.Sprite):
	def __init__(self, x, y, file_name):
		'''
    creates faling object sprite
    :params = x (int), y(int), file_name(str)
    :returns = None
    '''
		super().__init__()
		self.image = pygame.image.load(file_name)
		self.image = pygame.transform.smoothscale(self.image, (50, 50))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.speed = 5
    
	def update(self):
		'''
    This method updates the falling block so that 
    it to fall smoothly down the screen
    :params = None
    :returns = None
    '''
		self.rect.y+=3