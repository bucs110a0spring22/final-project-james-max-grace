import pygame

class FallingObjects(pygame.sprite.Sprite):
	def __init__(self, x=0, y=0, file_name=""):
		super().__init__(self)
		self.image = pygame.image.load(file_name)
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y+ str(id(self))
		self.speed = 1
		
	def move(self):
    
		
#generate random location for the object to appear
#have blocks fall at certain speed depending on which level of difficulty was chosen
#blocks disappear when they hit the bottom of the screen


#create a group w these sprites


#use update() method
#increase y by 1 every frome