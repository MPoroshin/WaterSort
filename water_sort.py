import sys
import pygame as pg
from pygame.color import THECOLORS


pg.init()
screen = pg.display.set_mode((1000, 700))
pg.display.set_caption('Игра Переливание')


class Flasks():
	"""  x,y - left upper corner  """
	global key
	def __init__(self,x,y,flask_list,Flask):
		self.x = x
		self.y = y
		self.flask_list = flask_list
		self.Flask = Flask

	def Fill_Flasks(self):
		k = 38*4
		for i in self.flask_list:
			pg.draw.rect(screen, THECOLORS[i],(self.x+9,self.y+k+13,56,38))
			k-=38

	def DrawFlask(self):
		screen.blit(self.Flask,(self.x,self.y))
		"""pg.draw.line(screen,THECOLORS[color],(self.x,self.y),(self.x+10,self.y),5)
		pg.draw.line(screen,THECOLORS[color],(self.x+60,self.y),(self.x+70,self.y),5)
		pg.draw.line(screen,THECOLORS[color],(self.x+10,self.y),(self.x+10,self.y+200),5)
		pg.draw.line(screen,THECOLORS[color],(self.x+60,self.y),(self.x+60,self.y+200),5)
		pg.draw.line(screen,THECOLORS[color],(self.x+10,self.y+200),(self.x+60,self.y+200),5)"""

	def ButtonFlask(self):
		global flaskkey
		global image
		mouse_pos = pg.mouse.get_pos()
		mouse_press = pg.mouse.get_pressed()
		if (mouse_pos[0] >=self.x) and (mouse_pos[0] <=self.x+70) and (mouse_pos[1] >=self.y) and (mouse_pos[1] <=self.y+200):
			if mouse_press[0] == True:
				flaskkey = self

class Button():
	"""  x,y - left upper corner  """
	global key
	def __init__(self,x,y,action,active_image,inactive_image,length,height):
		self.x = x
		self.y = y
		self.action = action
		self.active_image = active_image
		self.inactive_image = inactive_image
		self.length = length
		self.height = height
		

	def DrawButtonAndGetAction(self):
		global key
		mouse_pos = pg.mouse.get_pos()
		mouse_press = pg.mouse.get_pressed()
		if (mouse_pos[0] >=self.x) and (mouse_pos[0] <=self.x+self.length) and (mouse_pos[1] >=self.y) and (mouse_pos[1] <=self.y+self.height):
			screen.blit(self.active_image,(self.x,self.y+1))
			"""pg.draw.rect(screen, THECOLORS["white"],(self.x,self.y,self.length,self.height))
			pg.draw.rect(screen, THECOLORS["black"],(self.x+5,self.y+5,self.length-10,self.height-10))
			screen.blit((font1.render(str(self.text), True, THECOLORS['white'])),(self.text_x,self.text_y))"""
			if mouse_press[0] == True:
				key = self.action
				pg.time.delay(100)
		else:
			screen.blit(self.inactive_image,(self.x,self.y))
			"""pg.draw.rect(screen, THECOLORS["grey"],(self.x,self.y,self.length,self.height))
			pg.draw.rect(screen, THECOLORS["black"],(self.x+5,self.y+5,self.length-10,self.height-10))
			screen.blit((font1.render(str(self.text), True, THECOLORS['grey'])),(self.text_x,self.text_y-1))"""

def Win():
	screen.fill((71,74,81))
	pg.display.update()
	global run
	global key
	button_back = Button(10,10,"main",Button_back_active,Button_back_inactive,180,90)
	key = None
	run = True
	font1 = pg.font.SysFont('timesnewroman', 100)
	
	while run == True:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				sys.exit()
		screen.fill((71,74,81))
		button_back.DrawButtonAndGetAction()
		screen.blit((font1.render("ПОБЕДА ! ! !", True, THECOLORS['white'])),(250,300))
		if key is not None:
			run = False
		pg.display.update()
		pg.time.delay(100)


def Animation():
	global count_colors
	global flasks_activity_list
	global copy_flask_list_1
	global copy_flask_list_2
	pg.display.update()

def SwapFlasks():
	global count_colors
	global flasks_activity_list
	global copy_flask_list_1
	global copy_flask_list_2
	if (len(flasks_activity_list[0].flask_list) != 0) and (len(flasks_activity_list[1].flask_list) != 5):
		if ((len(flasks_activity_list[0].flask_list)==5) and (len(list(set(flasks_activity_list[0].flask_list)))==1)) is not True:
			if (len(flasks_activity_list[1].flask_list) == 0) or (flasks_activity_list[0].flask_list[-1] == flasks_activity_list[1].flask_list[-1]):

				copy_flask_list_1 = flasks_activity_list[0].flask_list
				copy_flask_list_2 = flasks_activity_list[1].flask_list

				i = flasks_activity_list[0].flask_list[-1]
				while (i == flasks_activity_list[0].flask_list[-1]) and (len(flasks_activity_list[1].flask_list) <5):
					count_colors +=1
					flasks_activity_list[1].flask_list.append(flasks_activity_list[0].flask_list[-1])
					del flasks_activity_list[0].flask_list[-1]
					if len(flasks_activity_list[0].flask_list) == 0:
						break

def lvl():
	screen.fill((71,74,81))
	pg.display.update()

	global key
	global run
	global flaskkey
	global flasks_activity_list
	
	


	button_back = Button(10,10,"main",Button_back_active,Button_back_inactive,150,85)
	run = True
	key = None

	Flasks1 = Flasks(170,320,["orange","orange","red","green","red"],Flask1)
	Flasks2 = Flasks(370,320,["green","orange","green","orange","red"],Flask2)
	Flasks3 = Flasks(570,320,["green","red","green","orange","red"],Flask3)
	Flasks4 = Flasks(770,320,[],Flask4)
	#"red","green","brown","pink"

	

	while run == True:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				sys.exit()
		screen.fill((71,74,81))

		if key != "win":
			screen.blit(Inactive_flask_button,(Flasks1.x+23,Flasks1.y+230))
			screen.blit(Inactive_flask_button,(Flasks2.x+23,Flasks2.y+230))
			screen.blit(Inactive_flask_button,(Flasks3.x+23,Flasks3.y+230))
			screen.blit(Inactive_flask_button,(Flasks4.x+23,Flasks4.y+230))
		else:
			screen.blit(Active_flask_button,(Flasks1.x+23,Flasks1.y+230))
			screen.blit(Active_flask_button,(Flasks2.x+23,Flasks2.y+230))
			screen.blit(Active_flask_button,(Flasks3.x+23,Flasks3.y+230))
			screen.blit(Active_flask_button,(Flasks4.x+23,Flasks4.y+230))


		button_back.DrawButtonAndGetAction()

		Flasks1.ButtonFlask()
		Flasks2.ButtonFlask()
		Flasks3.ButtonFlask()
		Flasks4.ButtonFlask()
		
		Flasks1.Fill_Flasks()
		Flasks2.Fill_Flasks()
		Flasks3.Fill_Flasks()
		Flasks4.Fill_Flasks()

		Flasks1.DrawFlask()
		Flasks2.DrawFlask()
		Flasks3.DrawFlask()
		Flasks4.DrawFlask()

		if flaskkey is not None:
			flasks_activity_list.append(flaskkey)
			flaskkey = None
		if len(flasks_activity_list) > 0:
			screen.blit(Active_flask_button,(flasks_activity_list[0].x+23,flasks_activity_list[0].y+230))


		if (len(flasks_activity_list)>1) and ((len(list(set(flasks_activity_list)))) == 1):
			flasks_activity_list = []
			

		if len(flasks_activity_list) > 1:
			screen.blit(Active_flask_button,(flasks_activity_list[1].x+23,flasks_activity_list[1].y+230))
			pg.time.delay(100)
			SwapFlasks()
			Animation()
			count_colors = 0
			copy_flask_list_1 = []
			copy_flask_list_2 = []
			flasks_activity_list = []
			
		
		if key == "win":
			run = False
			pg.display.update()
			pg.time.delay(1000)
		if key is not None:
			run = False


		if ((len(list(set(Flasks1.flask_list))) == 1) and (len(Flasks1.flask_list) == 5)) or (len(Flasks1.flask_list) == 0):
			if ((len(list(set(Flasks2.flask_list))) == 1) and (len(Flasks2.flask_list) == 5)) or (len(Flasks2.flask_list) == 0):
				if ((len(list(set(Flasks3.flask_list))) == 1) and (len(Flasks3.flask_list) == 5)) or (len(Flasks3.flask_list) == 0):
					if ((len(list(set(Flasks4.flask_list))) == 1) and (len(Flasks4.flask_list) == 5)) or (len(Flasks4.flask_list) == 0):
						key = "win"
						

		

		pg.display.update()
		screen.fill((71,74,81))
		pg.time.delay(100)

def Main_Menu():
	global key
	global run
	screen.fill((71,74,81))
	pg.display.update()
	button_play = Button(370,225,"lvl",Button_play_active,Button_play_inactive,270,100)
	button_exit = Button(425,350,"exit",Button_exit_active,Button_exit_inactive,160,65)
	key = None
	run = True

	
	while run == True:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				sys.exit()
		screen.fill((71,74,81))
		button_play.DrawButtonAndGetAction()
		button_exit.DrawButtonAndGetAction()
		
		if key is not None:
			run = False
		pg.display.update()
		pg.time.delay(100)





"""images"""
Flask1 = pg.image.load("images/Flask.png").convert_alpha()
Flask1 = pg.transform.scale(Flask1,(73,211))

Flask2 = pg.image.load("images/Flask.png").convert_alpha()
Flask2 = pg.transform.scale(Flask2,(73,211))

Flask3 = pg.image.load("images/Flask.png").convert_alpha()
Flask3 = pg.transform.scale(Flask3,(73,211))

Flask4 = pg.image.load("images/Flask.png").convert_alpha()
Flask4 = pg.transform.scale(Flask4,(73,211))

Button_play_inactive = pg.image.load("images/Button_play_inactive.png").convert_alpha()
Button_play_inactive = pg.transform.scale(Button_play_inactive,(300,300))

Button_play_active = pg.image.load("images/Button_play_active.png").convert_alpha()
Button_play_active = pg.transform.scale(Button_play_active,(299,299))

Button_back_active = pg.image.load("images/Button_back_active.png").convert_alpha()
Button_back_active = pg.transform.scale(Button_back_active,(250,250))

Button_back_inactive = pg.image.load("images/Button_back_inactive.png").convert_alpha()
Button_back_inactive = pg.transform.scale(Button_back_inactive,(249,249))

Active_flask_button = pg.image.load("images/Active_flask_button.png").convert_alpha()
Active_flask_button = pg.transform.scale(Active_flask_button,(150,150))

Inactive_flask_button = pg.image.load("images/Inactive_flask_button.png").convert_alpha()
Inactive_flask_button = pg.transform.scale(Inactive_flask_button,(149,149))

Button_exit_inactive = pg.image.load("images/Button_exit_inactive.png").convert_alpha()
Button_exit_inactive = pg.transform.scale(Button_exit_inactive,(180,180))

Button_exit_active = pg.image.load("images/Button_exit_active.png").convert_alpha()
Button_exit_active = pg.transform.scale(Button_exit_active,(179,179))
"""images"""

run =True
key = "main"
flaskkey = None
flasks_activity_list = []
count_colors = 0
copy_flask_list_1 = []
copy_flask_list_2 = []

while True:
	if key == "win":
		Win()
	elif key == "main":
		Main_Menu()
	elif key == "lvl":
		lvl()
	elif key == "exit":
		pg.quit()
		sys.exit()