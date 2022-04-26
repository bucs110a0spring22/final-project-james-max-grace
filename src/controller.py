class Controller:
	def __init__(self, width=480, height=320):
    pygame.init()
    self.width = width
    self.height = height
    Utility.screen_height = height
    Utility.screen_width = width

	def mainloop(self):

	def menuloop(self):
		#user select easy, medium, hard difficulty

	def gameoverloop(text,size,color,x,y):
		self.draw_text("Game Over")
		