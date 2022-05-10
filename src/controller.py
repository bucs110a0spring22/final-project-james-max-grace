import pygame, sys
import random
import time
from src import player
from src import fallingobject

class Controller:
  def __init__(self, width=600, height=400):
		 '''
		initializes screen, game states and sprites
			:params = width= (int)width of screen
							height= (int) height of screen
			:returns = None
	   '''
		 self.screen = pygame.display.set_mode((width, height))
		 self.obj_layer = pygame.display.set_mode((width, height))
		 self.clock = pygame.time.Clock()
		 self.FPS = 60
		 self.frame_count=0
		 self.background= pygame.image.load('assets/CS110GameBackground.jpg').convert_alpha()
		 self.background2 = pygame.image.load("assets/CS110GameOver.png").convert_alpha()
		 self.background3 = pygame.image.load("assets/backgroundscreen.png").convert_alpha()
		 self.game_state = "BEGIN"
		 self.player_state = "RUN"
		 self.width = width
		 self.height = height
		 self.white = (255,255,255)
		 self.alive = True
		 self.player = player.Player("karl", 10, 15, "assets/CS110Character2.png")
		 self.fallingobjects = pygame.sprite.Group()
		 self.x = 0
		 self.all_sprites = pygame.sprite.Group((self.player,) + tuple(self.fallingobjects))
		 self.clock = pygame.time.Clock()
		 self.initial_time = time.time()
		 self.game_speed = 10       
		 self.score_count = 0

    
  def mainloop(self):
		 '''
		checks game state and creates intro screen, runs game loop, or creates game over screen
		:params = None
		:returns = None
		 '''
		 while self.alive == True:
			  if self.game_state == "BEGIN":
					 self.gameIntroScreen()
			  elif self.game_state == "GAME":
					 self.gameloop()
			  elif self.game_state == "LOSE":
					 self.gameOverScreen()

	
  def gameIntroScreen(self):
		 '''
		creates intro main menu screen
		:params = None
		:returns = None
		'''
		 background_size = self.screen.get_size()
		 background_rect = self.background3.get_rect()
		 background_screen=pygame.display.set_mode(background_size)
		 background_screen.blit(self.background3, background_rect)
		 my_font = pygame.font.SysFont("impact", 30)
		 instructions = my_font.render('Use arrows to move left and right. Avoid the falling blocks. Press space to play.', False, self.white)
		 background_screen.blit(instructions, ((self.width / 3) - 200, self.height / 1.5))
		 pygame.display.flip()
		 for event in pygame.event.get():
			 if event.type == pygame.QUIT:
				 sys.exit()
			 if event.type == pygame.KEYDOWN:
				 if(event.key == pygame.K_SPACE):
					 self.game_state = "GAME"
					 self.gameloop()

  #def draw_fallingblock(self):
		
    
  def gameloop(self):
		 '''
		creates main game screen and runs main game events
		:params = None
		:returns = None
		'''
		 background_size = self.screen.get_size()
		 background_rect = self.background.get_rect()
		 background_screen = pygame.display.set_mode(background_size)
		 background_screen.blit(self.background, background_rect)
		 while self.alive == True:
			 pygame.display.flip()
				 
			 for event in pygame.event.get():
				 if event.type == pygame.QUIT:
					 pygame.quit()
					 sys.exit()
				 if event.type == pygame.KEYDOWN:
					 if event.key == pygame.K_RIGHT:
						 self.player.move_right()
					 if event.key == pygame.K_LEFT:
						 self.player.move_left()
					
			 num_blocks = 5
			 for i in range(num_blocks):
				 x = random.randrange(0, 601)
				 y = 0
				 self.fallingobjects.add(fallingobject.FallingObject(x, y, 'assets/fallingobject.png'))
			 self.all_sprites.draw(self.screen)
			 self.fallingobjects.update()
				 

				
				
					
  def gameOverScreen(self):
		 '''
		creates game over screen
		:params = None
		:returns = None
		'''
		 background_size = self.screen.get_size()
		 background_rect = self.background2.get_rect()
		 background_screen = pygame.display.set_mode(background_size)
		 background_screen.blit(self.background2, background_rect)
		 #my_font = pygame.font.SysFont("impact", 30)
		 title_font = pygame.font.SysFont("impact", 50)
		 game_over = title_font.render('GAME OVER!', False, (255,0,0))
		 background_screen.blit(game_over, ((self.width / 3) + 50, self.height / 4))
		 #background_screen.blit(your_score, ((self.width / 3) - 200, self.height / 1.5))
		 pygame.display.flip()
		 for event in pygame.event.get():
			 if event.type == pygame.MOUSEBUTTONDOWN:
				 sys.exit()

'''
			 if pygame.player.Player.spritecollide(self.FallingObjects,self.player,True):
				 #player.health-=1

      WHITE=(225,225,225)
      time_font=pygame.font.Font.bold(None,25)
    	total_seconds=self.frame_count//self.FPS
      minutes=total_seconds//60
      seconds=total_seconds
      output_string="Time Alive: {0:02}:{1:02}".format(minutes,seconds)
      text=time_font.render(output_string, True, WHITE)
      self.screen.blit(text,[0,250])
    '''