import sys
from pygame.color import THECOLORS
import pygame as pygame
import pymunk
import pymunk.pygame_util

pymunk.pygame_util.positive_y_is_up = False
pygame.init()
screen = pygame.display.set_mode((1000, 700))
pygame.display.set_caption('Игра Переливание')
clock = pygame.time.Clock()
draw_options = pymunk.pygame_util.DrawOptions(screen)
space = pymunk.Space()
space.gravity = 0, 2000

"""def create_waterball(space,pos):
	ball_mass, ball_radius = 10, 25
	ball_moment = pymunk.moment_for_circle(ball_mass, 0, ball_radius)
	ball_body = pymunk.Body(ball_mass, ball_moment)
	ball_body.position = pos
	ball_shape = pymunk.Circle (ball_body, ball_radius)
	space.add(ball_body,ball_shape)

plita1 = pymunk.Segment(space.static_body,(0,700),(1000,700),20)
plita1.elasticity = 0.8
space.add(plita1)

plita2 = pymunk.Segment(space.static_body,(0,0),(1000,0),1)
plita2.elasticity = 0.8
space.add(plita2)

plita3 = pymunk.Segment(space.static_body,(0,0),(0,700),1)
plita3.elasticity = 0.8
space.add(plita3)


plita4 = pymunk.Segment(space.static_body,(1000,0),(1000,700),1)
plita4.elasticity = 0.8
space.add(plita4)"""


class Flasks():
	"""  x,y - left upper corner  """
	global key
	def __init__(self,x,y,flask_list):
		self.x = x
		self.y = y
		self.flask_list = flask_list
		self.button_flag = False
	
	def Fill_Flasks(self):
		k = 38*4
		for i in self.flask_list:
			pygame.draw.rect(screen, THECOLORS[i],(self.x+13,self.y+k+8,45,38))
			k-=38
			
	def Fill_Flasks_del(self):
		k = 38*4
		for i in range(0,5):
			pygame.draw.rect(screen, THECOLORS["black"],(self.x+13,self.y+k+8,45,38))
			k-=38
			

	def DrawFlask(self,color):
		pygame.draw.line(screen,THECOLORS[color],(self.x,self.y),(self.x+10,self.y),5)
		pygame.draw.line(screen,THECOLORS[color],(self.x+60,self.y),(self.x+70,self.y),5)
		pygame.draw.line(screen,THECOLORS[color],(self.x+10,self.y),(self.x+10,self.y+200),5)
		pygame.draw.line(screen,THECOLORS[color],(self.x+60,self.y),(self.x+60,self.y+200),5)
		pygame.draw.line(screen,THECOLORS[color],(self.x+10,self.y+200),(self.x+60,self.y+200),5)

	def ButtonFlask(self):
		global flaskkey
		global image
		mouse_pos = pygame.mouse.get_pos()
		mouse_press = pygame.mouse.get_pressed()
		if (mouse_pos[0] >=self.x) and (mouse_pos[0] <=self.x+70) and (mouse_pos[1] >=self.y) and (mouse_pos[1] <=self.y+200):
			self.DrawFlask("white")
			if mouse_press[0] == True:
				flaskkey = self
				self.button_flag = True

class Button():
	"""  x,y - left upper corner  """
	global key
	def __init__(self,x,y,length,height,action,font_size,text,text_x,text_y):
		self.x = x
		self.y = y
		self.action = action
		self.length = length
		self.height = height
		self.font_size = font_size
		self.text = text
		self.text_x = text_x
		self.text_y = text_y
	def DrawButtonAndGetAction(self):
		global key
		font1 = pygame.font.SysFont('timesnewroman', self.font_size)
		mouse_pos = pygame.mouse.get_pos()
		mouse_press = pygame.mouse.get_pressed()
		if (mouse_pos[0] >=self.x) and (mouse_pos[0] <=self.x+self.length) and (mouse_pos[1] >=self.y) and (mouse_pos[1] <=self.y+self.height):
			pygame.draw.rect(screen, THECOLORS["white"],(self.x,self.y,self.length,self.height))
			pygame.draw.rect(screen, THECOLORS["black"],(self.x+5,self.y+5,self.length-10,self.height-10))
			screen.blit((font1.render(str(self.text), True, THECOLORS['white'])),(self.text_x,self.text_y))
			if mouse_press[0] == True:
				key = self.action
				pygame.time.delay(15)
		else:
			pygame.draw.rect(screen, THECOLORS["grey"],(self.x,self.y,self.length,self.height))
			pygame.draw.rect(screen, THECOLORS["black"],(self.x+5,self.y+5,self.length-10,self.height-10))
			screen.blit((font1.render(str(self.text), True, THECOLORS['grey'])),(self.text_x,self.text_y-1))

def Win():
	screen.fill(pygame.color.THECOLORS["black"])
	pygame.display.update()
	global run
	global key
	button_back = Button(10,10,200,50,"main",30,"Главное меню",20,18)
	key = None
	run = True
	font1 = pygame.font.SysFont('timesnewroman', 100)
	
	while run == True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		button_back.DrawButtonAndGetAction()
		screen.blit((font1.render("ПОБЕДА ! ! !", True, THECOLORS['white'])),(250,300))
		if key is not None:
			run = False
		pygame.display.update()
		clock.tick(60)

def SwapFlasks():
	global flasks_activity_list
	if (len(flasks_activity_list[0].flask_list) != 0) and (len(flasks_activity_list[1].flask_list) != 5):
		if ((len(flasks_activity_list[0].flask_list)==5) and (len(list(set(flasks_activity_list[0].flask_list)))==1)) is not True:
			if (len(flasks_activity_list[1].flask_list) == 0) or (flasks_activity_list[0].flask_list[-1] == flasks_activity_list[1].flask_list[-1]):
				i = flasks_activity_list[0].flask_list[-1]
				while (i == flasks_activity_list[0].flask_list[-1]) and (len(flasks_activity_list[1].flask_list) <5):
					flasks_activity_list[1].flask_list.append(flasks_activity_list[0].flask_list[-1])
					del flasks_activity_list[0].flask_list[-1]
					if len(flasks_activity_list[0].flask_list) == 0:
						break
				flasks_activity_list[0].Fill_Flasks_del()
				flasks_activity_list[0].Fill_Flasks()
				flasks_activity_list[1].Fill_Flasks_del()
				flasks_activity_list[1].Fill_Flasks()

def lvl():


	global key
	global run
	global flaskkey
	global flasks_activity_list
	


	button_back = Button(10,10,100,50,"main",30,"Назад",20,18)
	run = True
	key = None

	Flasks1 = Flasks(150,320,["orange","orange","red","green","red"])
	Flasks2 = Flasks(350,320,["green","orange","green","orange","red"])
	Flasks3 = Flasks(550,320,["green","red","green","orange","red"])
	Flasks4 = Flasks(750,320,[])
	#"red","green","brown","pink"

	

	
	while run == True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()

		space.step(1 / 60)
		space.debug_draw(draw_options)


		button_back.DrawButtonAndGetAction()

		Flasks1.DrawFlask("gray")
		Flasks2.DrawFlask("gray")
		Flasks3.DrawFlask("gray")
		Flasks4.DrawFlask("gray")

		if Flasks1.button_flag == False:
			Flasks1.ButtonFlask()
		else: Flasks1.button_flag = False
		
		if Flasks2.button_flag == False:
			Flasks2.ButtonFlask()
		else: Flasks2.button_flag = False

		if Flasks3.button_flag == False:
			Flasks3.ButtonFlask()
		else: Flasks3.button_flag = False

		if Flasks4.button_flag == False:
			Flasks4.ButtonFlask()
		else: Flasks4.button_flag = False
		
		Flasks1.Fill_Flasks()
		Flasks2.Fill_Flasks()
		Flasks3.Fill_Flasks()
		Flasks4.Fill_Flasks()

		if flaskkey is not None:
			flasks_activity_list.append(flaskkey)
			flaskkey = None

		if len(flasks_activity_list) > 0:
			flasks_activity_list[0].DrawFlask("yellow")
			
		if (len(flasks_activity_list)>1) and ((len(list(set(flasks_activity_list)))) == 1):
			flasks_activity_list = []

		if len(flasks_activity_list) > 1:
			flasks_activity_list[1].DrawFlask("yellow")
			pygame.display.update()
			pygame.time.delay(100)
			SwapFlasks()
			flasks_activity_list = []
		
		


		if ((len(list(set(Flasks1.flask_list))) == 1) and (len(Flasks1.flask_list) == 5)) or (len(Flasks1.flask_list) == 0):
			if ((len(list(set(Flasks2.flask_list))) == 1) and (len(Flasks2.flask_list) == 5)) or (len(Flasks2.flask_list) == 0):
				if ((len(list(set(Flasks3.flask_list))) == 1) and (len(Flasks3.flask_list) == 5)) or (len(Flasks3.flask_list) == 0):
					if ((len(list(set(Flasks4.flask_list))) == 1) and (len(Flasks4.flask_list) == 5)) or (len(Flasks4.flask_list) == 0):
						key = "win"
						Flasks1.DrawFlask("yellow")
						Flasks2.DrawFlask("yellow")
						Flasks3.DrawFlask("yellow")
						Flasks4.DrawFlask("yellow")


		if key == "win":
			run = False
			pygame.display.update()
			pygame.time.delay(1000)
		elif key is not None:
			run = False
		pygame.display.update()
		screen.fill(pygame.color.THECOLORS["black"])
		clock.tick(60)

def Main_Menu():
	global key
	global run
	screen.fill(pygame.color.THECOLORS["black"])
	pygame.display.update()
	button_play = Button(400,225,200,90,"lvl",50,"ИГРАТЬ",410,242)
	button_exit = Button(400,350,200,90,"exit",50,"ВЫХОД",410,367)
	key = None
	run = True

	
	while run == True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
		button_play.DrawButtonAndGetAction()
		button_exit.DrawButtonAndGetAction()
		
		if key is not None:
			run = False
			
		pygame.display.update()
		clock.tick(60)

run =True
key = "main"
flaskkey = None
flasks_activity_list = []

while True:
	if key == "win":
		Win()
	elif key == "main":
		Main_Menu()
	elif key == "lvl":
		lvl()
	elif key == "exit":
		pygame.quit()
		sys.exit()