import pygame

class Player(pygame.sprite.Sprite):
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
			
  def move_left(self):
	  self.rect.x = self.rect.x - 5
  def move_right(self):
	  self.rect.x = self.rect.x + 5


		
   



