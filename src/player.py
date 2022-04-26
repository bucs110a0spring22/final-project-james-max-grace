import pygame
import random
import time
import sys

class Player(pygame.sprite.Sprite):
	def __init__(self, x=0, y=0, filenames=None):
		super()
		self.image_set = [pygame.image.load(file_name) for f in filenames]
		self.current_image=0
    self.image = self.image_set[self.current_image] 
    self.rect = self.image.get_rect() 
    self.rect.x = x
    self.rect.y = y

  def collison(self, fallingobject):
    if pygame.sprite.spritecollideany(Player, FallingObjects):
      playerHealth()
	
	def move(self, direction):
		if direction == "left":
			self.rect.x = self.rect.x - 1
		elif direction == "right":
            self.rect.x = self.rect.x + 1
		elif direction == "up":
            self.rect.y = self.rect.y - 1 
    elif direction == "down":
            self.rect.y = self.rect.y + 1
  
	def playerHealth(self):
	#player loses 1/3 health when collision occurs




