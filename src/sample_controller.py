import pygame
import sys


class Controller:

  screen = pygame.display.set_mode((500, 500),0,32)
  font = pygame.font.SysFont(None, 20)
  
  def __init__(self):
    #setup pygame data
    
  def mainloop(self):
    #select state loop
    
  
  ### below are some sample loop states ###

  def menuloop(self):
    while True:

      screen.fill((0,0,0))    ## makes the entire screen black
      draw_text('Falling Frenzy', font, (255, 255, 255), screen, 20, 20)  #writes falling frenzy

      EasyMode = pygame.Rect(50, 75, 200, 50)     ##Button for easy mode
      MediumMode = pygame.Rect(50, 150, 200, 50)  ##Button for medium mode
      HardMode = pygame.Rect(50, 225, 200, 50)    ##Button for hard mode


      if EasyMode.collidepoint((mx, my)):
        if click:
          ##Play game with easy difficulty
      if MediumMode.collidepoint((mx, my)):
        if click:
          ##Play game with medium difficulty
      if HardMode.collidepoint((mx, my)):
        if click:
          ##Play game with hard difficulty
      pygame.draw.rect(screen, (255, 0, 0), EasyMode)
      pygame.draw.rect(screen, (255, 0, 0), MediumMode)
      pygame.draw.rect(screen, (255, 0, 0), HardMode)
      #event loop

      #update data

      #redraw
      
  def gameloop(self):
    running = True
      #event loop

      #update data

      #redraw
    
  def gameoverloop(self):
      #event loop

      #update data

      #redraw
