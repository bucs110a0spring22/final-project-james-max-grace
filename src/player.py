import pygame

class Player(pygame.sprite.Sprite):
  '''
  Defines player sprite
  :params = x(int), y(int), img_file(str)
  :returns = None
  '''
  def __init__(self, name, x, y, img_file):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load(img_file).convert_alpha()
    self.rect = self.image.get_rect()
    self.rect.x = x
    self.rect.y = y
    self.rect.width = 40
    self.rect.height= 40
    self.health = 3
    self.speed = 5

    '''
    These methods allow the player to move left and right utilizing the arrow keys
    :params = None
    :returns = None
    '''
  def move_left(self):
	  self.rect.x = self.rect.x - 5
  def move_right(self):
	  self.rect.x = self.rect.x + 5


		
   



