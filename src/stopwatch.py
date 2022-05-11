import time
import pygame

class Stopwatch:
## When any of the difficulty buttons are clicked and the game starts
  def displayTime(self):
      clock = pygame.time.Clock()
      font=pygame.freetype.Sysfont(None,34)
      font.origin=True
      while True:
        for e in pygame.event.get():
          if e.type==pygame.QUIT: return
        screen.fill(pygame.Color('grey12'))
        ticks=pygame.time.get_ticks()
        millis=ticks%1000
        seconds=int(ticks/1000%60)
        minutes=int(ticks/60000%24)
        out='{minutes:02d}:{seconds:02d}:{millis}'.format(minutes=minutes, seconds=seconds, )
        font.render_to(screen(100,100), out, pygame.Color('dodgerblue'))
        pygame.display.flip()
        clock.tick(60)

