import pygame, sys
import random
from src import player
from src import fallingobject
from src import floor

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
        self.background1= pygame.image.load('assets/CS110GameBackground.jpg').convert_alpha()
        self.background1 = pygame.transform.smoothscale(self.background1, (670, 420))
        self.background2 = pygame.image.load("assets/backgroundscreen.png")
        self.game_state = "BEGIN"
        self.width = width
        self.height = height
        self.background_size = self.screen.get_size()
        self.background_screen = pygame.display.set_mode(self.background_size)
        self.move_left = False
        self.move_right = False
        self.alive = True
        self.player = player.Player("karl", 50, 325, "assets/CS110Character2.png")
        self.player.image = pygame.transform.smoothscale(self.player.image, (50, 60))
        self.fallingobject = fallingobject.FallingObject((random.randrange(0,550)), 0, "assets/fallingobject.png")
        self.floor = floor.Floor(0, 415)
        self.fallingobjects = pygame.sprite.Group()
        self.num_objects = 6
        self.all_sprites = pygame.sprite.Group((self.player,), (self.floor,))
        self.clock = pygame.time.Clock()
        self.score_count = 0
        self.music_state = None
        self.music_sound = pygame.mixer.Sound("assets/game_music.mp3")

    
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
									
        background_rect = self.background2.get_rect()
        self.background_screen.blit(self.background2, background_rect)
        my_font = pygame.font.SysFont("impact", 25)
        instructions1 = my_font.render('Use arrows to move left and right. Avoid the falling blocks.', False, (255,255,255))
        instructions2 = my_font.render('Press space to play.', False, (255,255,255))
        self.background_screen.blit(instructions1, (100, 325))
        self.background_screen.blit(instructions2, (250, 350))
        pygame.display.flip()
        
    def generate_blocks(self):
     for i in range(self.num_objects):
      obj = fallingobject.FallingObject((random.randrange(0,550)), self.height, "assets/fallingobject.png")
      self.fallingobjects.add( (obj,) )
     self.all_sprites.add(self.fallingobjects)

    def sound(self):
     if self.music_state == None:
       self.music_sound.play(-1)
       self.music_state = 1

    #def check_collisions(self):
     #if pygame.sprite.spritecollide(self.player, self.fallingobjects, True):
      #return True
    
    def gameloop(self):
        '''
		creates main game screen and runs main game events
		:params = None
		:returns = None
	      '''
        while self.game_state == "GAME":
            pygame.mixer.init()
            pygame.mixer.music.set_volume(0.2)
            self.sound()
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

            if len(self.fallingobjects) == 0:
             self.generate_blocks()
							
					#collisions
            playercollide = pygame.sprite.spritecollide(self.player, self.fallingobjects, True)
            if(playercollide):
             for object in playercollide:
              self.player.health-=1
              self.fallingobjects.empty()

            floorcollide = pygame.sprite.spritecollide(self.floor, self.fallingobjects, True)
            if(floorcollide):
              for object in floorcollide:
               self.fallingobjects.empty()

            if self.player.health <= 0:
              self.game_state == "LOSE"
              self.highscore_record()
              self.gameOverScreen()
              break

					  #update screen
            background_rect = self.background1.get_rect()
            self.background_screen.blit(self.background1, background_rect)
            #timer display
            font1 = pygame.font.SysFont("impact",45)
            ticks = pygame.time.get_ticks()
            millis = ticks%1000
            seconds = int(ticks/1000%60)
            minutes = int(ticks/1000/60%60)
            displayed_time = '{minutes:02d}:{seconds:02d}:{millis}'.format(minutes=minutes, millis=millis, seconds=seconds)
            display = font1.render(displayed_time, False, (255,255,0))
            self.background_screen.blit(display, (400,30))
            self.clock.tick(60)
					  #score count
            for t in range(seconds):
             self.score_count += 1
            score = font1.render('Score: ' +str(self.score_count), False, (255, 255, 0))
            self.background_screen.blit(score, (400, 60))
            #life display
            lives = font1.render('Lives: ' +str(self.player.health), False, (255,255,0))
            self.background_screen.blit(lives, (20,20))
            #update sprites
            self.all_sprites.update()
            self.fallingobjects.draw(self.screen)
            self.all_sprites.draw(self.screen)
            pygame.display.flip()

    def highscore_record(self):
     newfile = open("src/highscore.txt", 'w')
     value = str(self.score_count)
     newfile.write(value)
     newfile.close()
					
    def gameOverScreen(self):
        '''
        creates game over screen, writes in and displays high score
        :params = None
        :returns = None
        '''
        title_font1 = pygame.font.SysFont("impact", 100)
        title_font2 = pygame.font.SysFont("impact", 50)
        
        game_over1 = title_font1.render('GAME OVER', False, (255,0,0))
        game_over2 = title_font2.render('Click "Run" to try again', False, (255,0,0))

        myfile = open("src/highscore.txt", 'r')
        highscore = myfile.read()
        myfile.close()
        game_over3 = title_font2.render('High Score: '+ highscore, False, (255,0,0))

        self.screen.fill((0,0,0))
        self.background_screen.blit(game_over1,(150, 100))
        self.background_screen.blit(game_over2,(170, 200))
        self.background_screen.blit(game_over3,(220, 300))
        pygame.display.flip()
			  
			