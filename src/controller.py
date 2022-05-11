import pygame, sys
import random
import time
from src import player
from src import fallingobject

class Controller:
    def __init__(self, width=0, height=0):
        '''
    		initializes screen, game states and sprites
    			:params = width= (int)width of screen
    							height= (int) height of screen
    			:returns = None
    	'''
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.background= pygame.image.load('assets/CS110GameBackground.jpg').convert_alpha()
        self.background2 = pygame.image.load("assets/CS110GameOver.png").convert_alpha()
        self.background3 = pygame.image.load("assets/backgroundscreen.png")
        self.game_state = "BEGIN"
        self.width = width
        self.height = height
        self.lower_boundary = 500
        self.move_left = False
        self.move_right = False
        self.alive = True
        self.player = player.Player("karl", 50, 325, "assets/CS110Character2.png")
        self.player.image = pygame.transform.smoothscale(self.player.image, (50, 60))
        self.fallingobject = fallingobject.FallingObject((random.randrange(0,550)), 0, "assets/fallingobject.png")
        self.fallingobjects = pygame.sprite.Group()
        self.num_objects = 5
        self.all_sprites = pygame.sprite.Group((self.player,))
        self.clock = pygame.time.Clock()
        self.initial_time = time.time()
        #self.game_speed = 10
        self.score_count = 0
        #self.frame_count=0
        #self.frame_rate=60

    
    def mainloop(self):
        '''
		checks game state and creates intro screen, runs game loop, or creates game over screen
		:params = None
		:returns = None
		'''
        while self.alive:
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
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if(event.key == pygame.K_SPACE):
                    self.game_state = "GAME"
        background_size = self.screen.get_size()
        background_rect = self.background3.get_rect()
        background_screen=pygame.display.set_mode(background_size)
        background_screen.blit(self.background3, background_rect)
        my_font = pygame.font.SysFont("impact", 25)
        instructions1 = my_font.render('Use arrows to move left and right. Avoid the falling blocks.', False, (255,255,255))
        instructions2 = my_font.render('Press space to play.', False, (255,255,255))
        background_screen.blit(instructions1, (50, 325))
        background_screen.blit(instructions2, (200, 350))
        pygame.display.flip()
        
		
    
    def gameloop(self):
        '''
		creates main game screen and runs main game events
		:params = None
		:returns = None
	      '''
        
        while self.game_state == "GAME":
            for event in pygame.event.get():
                 if event.type == pygame.QUIT:
                     pygame.quit()
                     sys.exit()
								#establish player movement controls
                 if event.type == pygame.KEYDOWN:
                     if event.key == pygame.K_RIGHT:
                         self.move_right = True
                     if event.key == pygame.K_LEFT:
                         self.move_left = True
                 if event.type == pygame.KEYUP:
                     if event.key == pygame.K_RIGHT:
                         self.move_right = False
                     if event.key == pygame.K_LEFT:
                         self.move_left = False
            if(self.move_right):
             self.player.move_right()
            if(self.move_left):
              self.player.move_left()

					
            for i in range(self.num_objects):
             obj = fallingobject.FallingObject((random.randrange(0,550)), 0, "assets/fallingobject.png")
             self.fallingobjects.add( (obj,) )

            if self.fallingobject.rect.y == self.lower_boundary:
             self.fallingobject.kill()
							
            self.all_sprites.add(self.fallingobjects)

					#collisions
            collide = pygame.sprite.spritecollide(self.player, self.fallingobjects, True)
            if self.player.health==0:
              self.game_state == "LOSE"
            if(collide):
              self.player.health-=1


					  #update screen
            self.screen.blit(self.background, (0, 0))
            self.all_sprites.update()
            self.fallingobjects.draw(self.screen)
            self.all_sprites.draw(self.screen)
            pygame.display.flip()
				 

				
				
					
    def gameOverScreen(self):
			
        '''
        creates game over screen
        :params = None
        :returns = None
        '''
        background_size = self.screen.get_size()
        background_rect = self.background3.get_rect()
        background_screen=pygame.display.set_mode(background_size)
        background_screen.blit(self.background3, background_rect)
        #my_font = pygame.font.SysFont("impact", 30)
        title_font = pygame.font.SysFont("impact", 50)
        game_over = title_font.render('Click "Run" to try again', False, (255,0,0))
        background_screen.blit(game_over,((self.width / 3) + 50, self.height / 4))
         #background_screen.blit(your_score, ((self.width / 3) - 200, self.height / 1.5))


        self.screen.blit(self.background2, (0,0))
      
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                sys.exit()
        background_size = self.screen.get_size()
        background_rect = self.background2.get_rect()
        background_screen = pygame.display.set_mode(background_size)
        background_screen.blit(self.background2, background_rect)
        pygame.display.flip()

