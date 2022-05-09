import pygame
from src import player
from src import fallingobjects


class Controller:
  def __init__(self, width=600, height=400):
    self.screen = pygame.display.set_mode((width, height))
    self.obj_layer = pygame.display.set_mode((width, height))
    self.clock = pygame.time.Clock()
    self.FPS = 60
    self.frame_count=0
    self.background= pygame.image.load('assets/CS110GameBackground.jpg').convert_alpha()
    self.background2 = pygame.image.load("assets/CS110GameOver.png").convert_alpha()
    self.game_state = "BEGIN"
    self.player_state = "RUN"
    self.width = width
    self.height = height
    self.white = (255,255,255)
    self.alive = True
    self.player = player.Player("karl", 50, 100, "assets/CS110Character2.png")
    self.fallingobjects = fallingobjects.FallingObjects(100, 100, 'assets/fallingobject.png')
    self.x = 0
    self.all_sprites = pygame.sprite.Group((self.player))
    self.clock = pygame.time.Clock()
    self.game_speed = 10
    self.obj_list = []       ##idk
    self.obj_sprites = pygame.sprite.Group()
    self.score_count = 0
    self.font=pygame.font.Font(None,25)

    
  def mainLoop(self):
    while self.alive == True:
      if self.game_state == "BEGIN":
        self.gameIntroScreen()
      elif self.game_state == "GAME":
        self.gameLoop()
      elif self.game_state == "LOSE":
        self.gameOverScreen()

	
  def gameIntroScreen(self):
		 background_size = self.screen.get_size()
		 background_rect = self.background.get_rect()
		 background_screen=pygame.display.set_mode(background_size)
		 background_screen.blit(self.background, background_rect)
		 my_font = pygame.font.SysFont("impact", 30)
		 title_font = pygame.font.SysFont("impact", 30)
		 name_of_game = title_font.render('Falling Frenzy', False, self.white)
		 instructions = my_font.render('Right Arrow to move right  Left Arrow to move left  Press space to play.', False, self.white)
		 background_screen.blit(name_of_game, ((self.width / 3) + 50, self.height / 4))
		 background_screen.blit(instructions, ((self.width / 3) - 200, self.height / 1.5))
		 pygame.display.flip()
		 for event in pygame.event.get():
			 if event.type == pygame.QUIT:
				 sys.exit()
			 if event.type == pygame.KEYDOWN:
				 if(event.key == pygame.K_SPACE):
					 self.game_state = "GAME"
					 self.mainLoop()
    
    
  def gameloop(self):
    while self.alive():
      WHITE=(225,225,225)
      total_seconds=self.frame_count//self.FPS
      minutes=total_seconds//60
      seconds=total_seconds
      output_string="Time Alive: {0:02}:{1:02}".format(minutes,seconds)
      text=self.font.render(output_string, True, WHITE)
      self.screen.blit(text,[0,250])
      
      
    

















'''
class Controller:

  def __init__(self):
  
    mainClock = pygame.time.Clock()
    from pygame.locals import *
    pygame.init()
    pygame.display.set_caption('Falling Frenzy')
    screen = pygame.display.set_mode((500, 500),0,32)
    
    ##Image Stuff
    backgroundfile = "assets/CS110EasyBackground.jpg"
    background = pygame.image.load(backgroundfile).convert_alpha() 
    
    """
    fallingobjects.add(fallingobjects.FallingObjects("Boogie", x, y, 'assets/fallingobject.png'))
    """
    
  font = pygame.font.SysFont(None, 75)
  font2 = pygame.font.SysFont(None, 20)
   
  def draw_text(text, font, color, surface, x, y):
      textobj = font.render(text, 1, color)
      textrect = textobj.get_rect()
      textrect.topleft = (x, y)
      surface.blit(textobj, textrect)
   
  click = False
   
  def main_menu(self):
      while True:
   
          self.screen.fill((150, 150, 250))
          self.draw_text('Falling Frenzy', font, (255, 255, 255), screen, 90, 100)
          draw_text('Click Button Below to Start', font2, (0,0,0), screen, 165, 225)
   
          mx, my = pygame.mouse.get_pos()
   
          button_1 = pygame.Rect(150, 250, 200, 75)
  
          if button_1.collidepoint((mx, my)):
              if click:
                  game()
          pygame.draw.rect(screen, (255, 0, 0), button_1)
   
          click = False
          for event in pygame.event.get():
              if event.type == QUIT:
                  pygame.quit()
                  sys.exit()
              if event.type == KEYDOWN:
                  if event.key == K_ESCAPE:
                      pygame.quit()
                      sys.exit()
              if event.type == MOUSEBUTTONDOWN:
                  if event.button == 1:
                      click = True
   
          pygame.display.update()
          mainClock.tick(60)
   
   
  def game():
      running = True
      while running:
          background=pygame.image.load('assets/CS110HardBackground.jpg')
          screen.blit(background,[0,0])
          
          draw_text('game', font, (255, 255, 255), screen, 20, 20)
  			
          for event in pygame.event.get():
              if event.type == QUIT:
                  pygame.quit()
                  sys.exit()
              if event.type == KEYDOWN:
                  if event.key == K_ESCAPE:
                      running = False
          
          pygame.display.update()
          mainClock.tick(60)
  
  
  
  def game_over():
    player.kill()
    screen.fill((150, 150, 250))
    draw_text('Game Over', font, (255, 255, 255), screen, 90, 100)
    while True:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
  
  
  
  
  
  main_menu()
  '''