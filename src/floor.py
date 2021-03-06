import pygame

class Floor(pygame.sprite.DirtySprite):
	'''
    defines floor dirty sprite into which falling blocks will be killed if collide
    :params = x(int), y(int)
    :returns = None
    '''
	def __init__(self, x, y):
		super().__init__()
		self.dirty = 1
		self.visible = 0
		self.image = pygame.Surface((1000, 1000))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y