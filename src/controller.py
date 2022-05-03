import pygame
import sys


class Controller:

  screen = pygame.display.set_mode((500, 500),0,32) ##sets the scre
  font = pygame.font.SysFont(None, 20) ##sets the font of the writing
  
  def __init__(self):
    pygame.init()
    self.screen=di
    
    #setup pygame data
    
  def mainloop(self):
    ##unfinished
    while True:      
      if(self.state == "GAME"):
        self.gameLoop()
      elif(self.state == "GAMEOVER"):
        self.gameOver()
  
  def menuloop(self):
        ##unfinished
    while True:

      screen.fill((0,0,0))    ## makes the entire screen black
      draw_text('Falling Frenzy', font, (255, 255, 255), screen, 20, 20)  #writes falling frenzy
'''
      EasyMode = pygame.Rect(50, 75, 200, 50)     ##Button for easy mode
      MediumMode = pygame.Rect(50, 150, 200, 50)  ##Button for medium mode
      HardMode = pygame.Rect(50, 225, 200, 50)    ##Button for hard mode
'''

      if EasyMode.collidepoint((mx, my)):
        if click:
          ##Play game with easy difficulty
      if MediumMode.collidepoint((mx, my)):
        if click:
          ##Play game with medium difficulty
      if HardMode.collidepoint((mx, my)):
        if click:
          ##Play game with hard difficulty
          '''
      pygame.draw.rect(screen, (255, 0, 0), EasyMode)
      pygame.draw.rect(screen, (255, 0, 0), MediumMode)
      pygame.draw.rect(screen, (255, 0, 0), HardMode)
    '''
      
  def gameloop(self):    ##add timer - top left
        ##unfinished
    while self.state == "GAME":         
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          sys.exit()
        if event.type == pygame.KEYDOWN:
          if (event.key == pygame.K_LEFT):
            self.hero.move_left()
          elif(event.key == pygame.K_RIGHT):
            self.hero.move_right()
    
  def gameoverloop(self):    ##add points count
    ##unfinished
      self.hero.kill()   ##remove sprite
        myfont = pygame.font.SysFont(None, 30)
        message = myfont.render('Game Over', False, (0, 0, 0))
        self.screen.blit(message, (self.width / 2, self.height / 2))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


  def findScore(self):
    

