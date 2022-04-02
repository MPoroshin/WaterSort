import sys, math
import pygame as pg
from pygame.color import THECOLORS

pg.init()
width = 1280
height = 720

screen = pg.display.set_mode((width, height))
pg.display.set_caption('Игра Переливание')

pg.mixer.music.load('losing-oneself-55732.mp3')
pg.mixer.music.play(-1)

class Flasks():
	"""  x,y - left upper corner  """
	global key
	def __init__(self,x,y,flask_list,Flask):
		self.x = x
		self.y = y
		self.flask_list = flask_list
		self.Flask = Flask
		self.x_for_circle = x+33
		self.y_for_circle = y+245


	def Fill_Flasks(self, c):
		if c == -1:
			k = 39*4
			for i in self.flask_list:
				pg.draw.rect(screen, THECOLORS[i],(self.x+18,self.y+k+25,58,39))
				k-=39
		else:
			k = 39*4
			for i in self.flask_list:
				if c <= 0: break
				pg.draw.rect(screen, THECOLORS[i],(self.x+18,self.y+k+25,58,39))
				k-=39
				c-=1
				

	def DrawFlask(self):
		screen.blit(self.Flask,(self.x+17,self.y+13))

	def ButtonFlask(self):
		global flaskkey
		global image
		mouse_pos = pg.mouse.get_pos()
		mouse_press = pg.mouse.get_pressed()
		if (mouse_pos[0] >=self.x) and (mouse_pos[0] <=self.x+93) and (mouse_pos[1] >=self.y+10) and (mouse_pos[1] <=self.y+231):
			if mouse_press[0] == True:
				flaskkey = self
				pg.time.delay(250)

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
			if mouse_press[0] == True:
				key = self.action
				pg.time.delay(200)
		else:
			screen.blit(self.inactive_image,(self.x,self.y))

def Drawlvl(button_back, Button_again, lvl_item, flasks_activity_list, flag):
	"""false - для анимации, True - для статичной картинки"""
	screen.fill((71,74,81))

	button_back.DrawButtonAndGetAction()
	Button_again.DrawButtonAndGetAction()
	


	if flag == False:
		for i in lvl_item:
			if (i != flasks_activity_list[0]) and (i != flasks_activity_list[1]):
				i.Fill_Flasks(-1)
			else:
				if (i == flasks_activity_list[1]):
					i.Fill_Flasks(len(flasks_activity_list[1].flask_list)-1)
				elif (i == flasks_activity_list[0]):
					i.Fill_Flasks(len(flasks_activity_list[0].flask_list))
				
			i.DrawFlask()
	else:
		for i in lvl_item:
			i.Fill_Flasks(-1)
			i.DrawFlask()
			i.ButtonFlask()




	for i in lvl_item:
		screen.blit(Inactive_flask_button,(i.x_for_circle,i.y_for_circle))

	if len(flasks_activity_list) > 0:
		screen.blit(Active_flask_button,(flasks_activity_list[0].x_for_circle,flasks_activity_list[0].y_for_circle))
	if len(flasks_activity_list) > 1:
		screen.blit(Active_flask_button,(flasks_activity_list[1].x_for_circle,flasks_activity_list[1].y_for_circle))

def Animation(color,pos_del,button_back, Button_again, lvl_item, flasks_activity_list):
	global key

	dist = abs(flasks_activity_list[0].x - flasks_activity_list[1].x)
	up_value = (flasks_activity_list[0].y+25+pos_del - flasks_activity_list[0].y)+39 - 15   #на сколько двигать вверх?

	down_value = (5 - len(flasks_activity_list[1].flask_list)     )*39 + 39 + 15#на сколько двигать вниз?
	pos_fill = -39-15

	k1 = 0
	k2 = 0


	for _ in range(1,up_value+1):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				sys.exit()


		Drawlvl(button_back, Button_again, lvl_item, flasks_activity_list, False)
	
		
		pg.draw.rect(screen, THECOLORS[color],(flasks_activity_list[0].x+18,flasks_activity_list[0].y+25+pos_del-k1,58,39))
		k1 += 1
		flasks_activity_list[0].DrawFlask()
		if key is not None:
			break
		pg.display.update()

	pos_del += 39
	up_value -= 39
	k1 = 0

	"""  движение по траектории  """
	R_vertik = 120
	R_horiz = dist//2

	
	if (flasks_activity_list[0].x - flasks_activity_list[1].x) < 0:
		X0 = flasks_activity_list[0].x + 18 + R_horiz
		Y0 = flasks_activity_list[0].y - 39
		a =-3.14
		while a <= 0.2:
			for event in pg.event.get():
				if event.type == pg.QUIT:
					pg.quit()
					sys.exit()
			Drawlvl(button_back, Button_again, lvl_item, flasks_activity_list, False)
			X = int( ( R_horiz * math.cos(a)  ) + X0)
			Y = int( ( R_vertik * math.sin(a)  ) + Y0)
			pg.draw.rect(screen, THECOLORS[color], (X, Y, 58, 39) )
			a += 0.1
			pg.time.delay(10)
			pg.display.update()
	else:
		X0 = flasks_activity_list[1].x + 18 + R_horiz
		Y0 = flasks_activity_list[1].y - 39
		a =0.2
		while a >= -3.14:
			for event in pg.event.get():
				if event.type == pg.QUIT:
					pg.quit()
					sys.exit()
			Drawlvl(button_back, Button_again, lvl_item, flasks_activity_list, False)
			X = int( ( R_horiz * math.cos(a) )  + X0)
			Y = int( ( R_vertik * math.sin(a) )  + Y0)
			pg.draw.rect(screen, THECOLORS[color], (X, Y, 58, 39) )
			a -= 0.1
			pg.time.delay(10)
			pg.display.update()
	"""  движение по траектории  """

	for _ in range(1,down_value+1):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				sys.exit()

		Drawlvl(button_back, Button_again, lvl_item, flasks_activity_list, False)
		flasks_activity_list[0].DrawFlask()
		pg.draw.rect(screen, THECOLORS[color], (flasks_activity_list[1].x+18,flasks_activity_list[1].y+25 + pos_fill + k2,58,39))
		k2 += 1
		flasks_activity_list[1].DrawFlask()
		if key is not None:
			break
		pg.display.update()

	down_value -= 39
	k2 = 0
			
def SwapFlasks(button_back, Button_again, lvl_item, flasks_activity_list):
	i = flasks_activity_list[0].flask_list[-1]
	pos_del = (39* 5) - (39 *  len(flasks_activity_list[0].flask_list))
	color = flasks_activity_list[0].flask_list[-1]
	while (i == flasks_activity_list[0].flask_list[-1]) and (len(flasks_activity_list[1].flask_list) <5):
		flasks_activity_list[1].flask_list.append(flasks_activity_list[0].flask_list[-1])
		del flasks_activity_list[0].flask_list[-1]
		Animation(color,pos_del,button_back, Button_again, lvl_item, flasks_activity_list)
		if len(flasks_activity_list[0].flask_list) == 0:
			break
	
def lvl(lvl_item,link_on_lvl):
	screen.fill((71,74,81))
	pg.display.update()
	global r, key, run, flaskkey, flasks_activity_list, rotated_image_list
	button_back = Button(10,10,"level_menu",Button_back_active,Button_back_inactive,150,85)
	Button_again = Button(width-150,height-710,link_on_lvl,Button_again_active,Button_again_inactive,135,105) #width-135-10, height-(height-10)
	run = True
	key = None

	fill_flask_count = 0
	while run == True:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				sys.exit()

		if flaskkey is not None:
			flasks_activity_list.append(flaskkey)
			flaskkey = None
		
		if (len(flasks_activity_list)>1) and ((len(list(set(flasks_activity_list)))) == 1):
			flasks_activity_list = []

		Drawlvl(button_back, Button_again, lvl_item, flasks_activity_list, True)
		
		if (len(flasks_activity_list) > 1):
			if (len(flasks_activity_list[0].flask_list) != 0):
				if (len(flasks_activity_list[1].flask_list) != 5):
					if ((len(flasks_activity_list[0].flask_list) == 5) and (len(list(set(flasks_activity_list[0].flask_list)))==1)) is not True:
						if (len(flasks_activity_list[1].flask_list) == 0) or (flasks_activity_list[0].flask_list[-1] == flasks_activity_list[1].flask_list[-1]):
							SwapFlasks(button_back, Button_again, lvl_item, flasks_activity_list)
							fill_flask_count = 0
							for i in lvl_item:
								if ((len(list(set(i.flask_list))) == 1) and (len(i.flask_list) == 5)) or (len(i.flask_list) == 0):
									fill_flask_count+=1
							flasks_activity_list = []
						else:
							flasks_activity_list = []
					else:
						flasks_activity_list = []
				else:
					flasks_activity_list = []
			else:
				flasks_activity_list = []
			

		if fill_flask_count == len(lvl_item):
			for i in lvl_item:
				screen.blit(Active_flask_button,(i.x_for_circle,i.y_for_circle))
				screen.blit(Win_text,(width//2-800//2+50,height//2-225))

		if key is not None:
			run = False

		pg.display.update()
		pg.time.delay(1)

def Pause_or_Resume():
	global key
	global volume_key
	if volume_key == True:
		pg.mixer.music.pause()
		volume_key = False
	else:
		pg.mixer.music.unpause()
		volume_key = True
	key = None

def Main_Menu():
	global key
	global run
	global volume_key
	screen.fill((71,74,81))
	
	pg.display.update()
	button_play = Button(width//2-350//2,height//2-350//2+50,"level_menu",Button_play_active,Button_play_inactive,320,120)
	button_exit = Button(width//2-250//2,height//2-250//2+150,"exit",Button_exit_active,Button_exit_inactive,220,90)
	button_volume_play = Button(10,10,"volume",Volume_play_active,Volume_play_inactive,150,85)
	button_volume_pause = Button(10,10,"volume",Volume_pause_active,Volume_pause_inactive,150,85)
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

		if volume_key == True:
			button_volume_play.DrawButtonAndGetAction()
		else:
			button_volume_pause.DrawButtonAndGetAction()
		if key == "volume":
			Pause_or_Resume()
		if key is not None:
			run = False
		pg.display.update()
		pg.time.delay(10)
	
def Levels():
	global key
	global run
	screen.fill((71,74,81))
	pg.display.update()
	key = None
	run = True
	button_back = Button(10,10,"main",Button_back_active,Button_back_inactive,150,85)
	
	button_lvl1 = Button(width-(width-150),height-320,"lvl1",lvl1_active,lvl1_inactive,155,140)  #height width
	button_lvl2 = Button(width-(width-350),height-320,"lvl2",lvl2_active,lvl2_inactive,155,140)
	button_lvl3 = Button(width-(width-550),height-320,"lvl3",lvl3_active,lvl3_inactive,155,140)
	button_lvl4 = Button(width-(width-750),height-320,"lvl4",lvl4_active,lvl4_inactive,155,140)
	button_lvl5 = Button(width-(width-950),height-320,"lvl5",lvl5_active,lvl5_inactive,155,140)

	while run == True:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				sys.exit()

		screen.fill((71,74,81))
		button_back.DrawButtonAndGetAction()
		screen.blit(Level_menu_text,(100,200))
		
		button_lvl1.DrawButtonAndGetAction()
		button_lvl2.DrawButtonAndGetAction()
		button_lvl3.DrawButtonAndGetAction()
		button_lvl4.DrawButtonAndGetAction()
		button_lvl5.DrawButtonAndGetAction()

		if key is not None:
			run = False
		pg.display.update()
		pg.time.delay(30)




"""images""" 

Volume_pause_active = pg.image.load("images/Volume_pause_active.png").convert_alpha()
Volume_pause_active = pg.transform.scale(Volume_pause_active,(250,250))

Volume_play_active = pg.image.load("images/Volume_play_active.png").convert_alpha()
Volume_play_active = pg.transform.scale(Volume_play_active,(250,250))

Volume_play_inactive = pg.image.load("images/Volume_play_inactive.png").convert_alpha()
Volume_play_inactive = pg.transform.scale(Volume_play_inactive,(250,250))

Volume_pause_inactive = pg.image.load("images/Volume_pause_inactive.png").convert_alpha()
Volume_pause_inactive = pg.transform.scale(Volume_pause_inactive,(250,250))



Flask = pg.image.load("images/Flask.png").convert_alpha()
Flask = pg.transform.scale(Flask,(60,210))

Button_play_inactive = pg.image.load("images/Button_play_inactive.png").convert_alpha()
Button_play_inactive = pg.transform.scale(Button_play_inactive,(350,350))

Button_play_active = pg.image.load("images/Button_play_active.png").convert_alpha()
Button_play_active = pg.transform.scale(Button_play_active,(349,349))

Button_back_active = pg.image.load("images/Button_back_active.png").convert_alpha()
Button_back_active = pg.transform.scale(Button_back_active,(250,250))

Button_back_inactive = pg.image.load("images/Button_back_inactive.png").convert_alpha()
Button_back_inactive = pg.transform.scale(Button_back_inactive,(249,249))

Active_flask_button = pg.image.load("images/Active_flask_button.png").convert_alpha()
Active_flask_button = pg.transform.scale(Active_flask_button,(150,150))

Inactive_flask_button = pg.image.load("images/Inactive_flask_button.png").convert_alpha()
Inactive_flask_button = pg.transform.scale(Inactive_flask_button,(149,149))

Button_exit_inactive = pg.image.load("images/Button_exit_inactive.png").convert_alpha()
Button_exit_inactive = pg.transform.scale(Button_exit_inactive,(250,250))

Button_exit_active = pg.image.load("images/Button_exit_active.png").convert_alpha()
Button_exit_active = pg.transform.scale(Button_exit_active,(249,249))

Level_menu_text = pg.image.load("images/Level_menu_text.png").convert_alpha()
Level_menu_text = pg.transform.scale(Level_menu_text,(350,350))

lvl1_active = pg.image.load("images/lvl1_active.png").convert_alpha()
lvl1_active = pg.transform.scale(lvl1_active,(350,690))

lvl2_active = pg.image.load("images/lvl2_active.png").convert_alpha()
lvl2_active = pg.transform.scale(lvl2_active,(350,350))

lvl3_active = pg.image.load("images/lvl3_active.png").convert_alpha()
lvl3_active = pg.transform.scale(lvl3_active,(350,350))

lvl4_active = pg.image.load("images/lvl4_active.png").convert_alpha()
lvl4_active = pg.transform.scale(lvl4_active,(350,350))

lvl5_active = pg.image.load("images/lvl5_active.png").convert_alpha()
lvl5_active = pg.transform.scale(lvl5_active,(350,350))

lvl1_inactive = pg.image.load("images/lvl1_inactive.png").convert_alpha()
lvl1_inactive = pg.transform.scale(lvl1_inactive,(350,690))

lvl2_inactive = pg.image.load("images/lvl2_inactive.png").convert_alpha()
lvl2_inactive = pg.transform.scale(lvl2_inactive,(350,350))

lvl3_inactive = pg.image.load("images/lvl3_inactive.png").convert_alpha()
lvl3_inactive = pg.transform.scale(lvl3_inactive,(350,350))

lvl4_inactive = pg.image.load("images/lvl4_inactive.png").convert_alpha()
lvl4_inactive = pg.transform.scale(lvl4_inactive,(350,350))

lvl5_inactive = pg.image.load("images/lvl5_inactive.png").convert_alpha()
lvl5_inactive = pg.transform.scale(lvl5_inactive,(350,350))

Button_again_active = pg.image.load("images/Button_again_active.png").convert_alpha()
Button_again_active = pg.transform.scale(Button_again_active,(200,200))

Button_again_inactive = pg.image.load("images/Button_again_inactive.png").convert_alpha()
Button_again_inactive = pg.transform.scale(Button_again_inactive,(200,200))

Win_text = pg.image.load("images/Win_text.png").convert_alpha()
Win_text = pg.transform.scale(Win_text,(800,800))
"""images"""

run =True
key = "main"
flaskkey = None
flasks_activity_list = []
volume_key = True

while 1:
	"""lvl1"""
	link_on_lvl1 = "lvl1"
	Flasks1_1 = Flasks(width//2-73//2-500//2,320,["green","red","green","red","green"],Flask)
	Flasks1_2 = Flasks(width//2-73//2,320,["red","green","red","green","red"],Flask)
	Flasks1_3 = Flasks(width//2-73//2+500//2,320,[],Flask)
	lvl1 = [Flasks1_1,Flasks1_2,Flasks1_3]

	"""lvl2"""
	link_on_lvl2 = "lvl2"
	Flasks2_1 = Flasks(width//2-73//2-390,320,["orange","orange","red","green","red"],Flask)
	Flasks2_2 = Flasks(width//2-73//2-130,320,["green","orange","green","orange","red"],Flask)
	Flasks2_3 = Flasks(width//2-73//2+130,320,["green","red","green","orange","red"],Flask)
	Flasks2_4 = Flasks(width//2-73//2+390,320,[],Flask)
	lvl2 = [Flasks2_1,Flasks2_2,Flasks2_3,Flasks2_4]

	"""lvl3"""
	link_on_lvl3 = "lvl3"
	Flasks3_1 = Flasks(width//2-73//2-400,320,["green","yellow","green","green","red"],Flask)
	Flasks3_2 = Flasks(width//2-73//2-200,320,["blue","yellow","red","blue","yellow"],Flask)
	Flasks3_3 = Flasks(width//2-73//2,320,["red","blue","blue","red","green"],Flask)
	Flasks3_4 = Flasks(width//2-73//2+200,320,["red","yellow","blue","yellow","green"],Flask)
	Flasks3_5 = Flasks(width//2-73//2+400,320,[],Flask)
	lvl3 = [Flasks3_1,Flasks3_2,Flasks3_3,Flasks3_4,Flasks3_5]

	"""lvl4"""
	link_on_lvl4 = "lvl4"
	Flasks4_1 = Flasks(width//2-73//2-415,320,["orange","grey","orange","grey","grey"],Flask)
	Flasks4_2 = Flasks(width//2-73//2-250,320,["grey","orange","orange","purple","pink"],Flask)
	Flasks4_3 = Flasks(width//2-73//2-85,320,["blue","blue","blue","blue","purple"],Flask)
	Flasks4_4 = Flasks(width//2-73//2+85,320,["grey","orange","purple","pink","pink"],Flask)
	Flasks4_5 = Flasks(width//2-73//2+250,320,["blue","pink","pink","purple","purple"],Flask)
	Flasks4_6 = Flasks(width//2-73//2+415,320,[],Flask)
	lvl4 = [Flasks4_1,Flasks4_2,Flasks4_3,Flasks4_4,Flasks4_5,Flasks4_6]

	"""lvl5"""
	link_on_lvl5 = "lvl5"
	Flasks5_1 = Flasks(width//2-73//2-450,320,["salmon","khaki","red","red","red"],Flask)
	Flasks5_2 = Flasks(width//2-73//2-300,320,["khaki","khaki","red","salmon","salmon"],Flask)
	Flasks5_3 = Flasks(width//2-73//2-150,320,["pink","pink","lime","khaki","lime"],Flask)
	Flasks5_4 = Flasks(width//2-73//2,320,["lime","yellow","salmon","salmon","khaki"],Flask)
	Flasks5_5 = Flasks(width//2-73//2+150,320,["yellow","lime","pink","lime","yellow",],Flask)
	Flasks5_6 = Flasks(width//2-73//2+300,320,["pink","yellow","pink","yellow","red"],Flask)
	Flasks5_7 = Flasks(width//2-73//2+450,320,[],Flask)  
	lvl5 = [Flasks5_1,Flasks5_2,Flasks5_3,Flasks5_4,Flasks5_5,Flasks5_6,Flasks5_7]

	if key == "main":
		Main_Menu()
	elif key == "level_menu":
		Levels()
	elif key == "lvl1":
		lvl(lvl1,link_on_lvl1)
	elif key == "lvl2":
		lvl(lvl2,link_on_lvl2)
	elif key == "lvl3":
		lvl(lvl3,link_on_lvl3)
	elif key == "lvl4":
		lvl(lvl4,link_on_lvl4)
	elif key == "lvl5":
		lvl(lvl5,link_on_lvl5)
	elif key == "exit":
		pg.quit()
		sys.exit()
