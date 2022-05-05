import pygame
import random
import time
import sys

class Player(pygame.sprite.Sprite):
	def __init__(self, x, y, img_file):
		super()
		self.image_set = [pygame.image.load(file_name) for f in filenames]
		self.current_image=0
		self.player_health=3
		self.image = self.image_set[self.current_image]
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		
	def collison(self, fallingobject):
		if pygame.sprite.spritecollideany(Player, FallingObjects):
			player_health-=1
			
	
	def move(self, direction):
		if direction == "left":
			self.rect.x = self.rect.x - 1
		elif direction == "right":
      self.rect.x = self.rect.x + 1
   



