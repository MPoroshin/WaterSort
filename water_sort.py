import sys
import pygame as pg
from pygame.color import THECOLORS

pg.init()
screen = pg.display.set_mode((1000, 600))
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
			"""pg.draw.rect(screen, THECOLORS["white"],(self.x,self.y,self.length,self.height))
			pg.draw.rect(screen, THECOLORS["black"],(self.x+5,self.y+5,self.length-10,self.height-10))
			screen.blit((font1.render(str(self.text), True, THECOLORS['white'])),(self.text_x,self.text_y))"""
			if mouse_press[0] == True:
				key = self.action
				pg.time.delay(200)
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
	button_back = Button(10,10,"level_menu",Button_back_active,Button_back_inactive,180,90)
	key = None
	run = True
	
	while run == True:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				sys.exit()
		screen.fill((71,74,81))
		button_back.DrawButtonAndGetAction()
		screen.blit(Win_text,(280,250))
		if key is not None:
			run = False
		pg.display.update()
		pg.time.delay(100)

def Animation(pos_fill,count1,color,pos_del):
	global flasks_activity_list
	k = 0
	for _ in range(1,38*count1+1):
		pg.draw.rect(screen, (71,74,81),(flasks_activity_list[0].x+9,flasks_activity_list[0].y+13+pos_del+k,56,1))
		flasks_activity_list[0].DrawFlask()
		pg.draw.rect(screen, THECOLORS[color],(flasks_activity_list[1].x+9,flasks_activity_list[1].y+13+pos_fill-k,56,1))
		flasks_activity_list[1].DrawFlask()
		pg.display.update()
		pg.time.delay(15)
		k += 1

def SwapFlasks():
	global flasks_activity_list
	if (len(flasks_activity_list[0].flask_list) != 0) and (len(flasks_activity_list[1].flask_list) != 5):
		if ((len(flasks_activity_list[0].flask_list)==5) and (len(list(set(flasks_activity_list[0].flask_list)))==1)) is not True:
			if (len(flasks_activity_list[1].flask_list) == 0) or (flasks_activity_list[0].flask_list[-1] == flasks_activity_list[1].flask_list[-1]):
				i = flasks_activity_list[0].flask_list[-1]
				pos_del = (38* 5) - (38 *  len(flasks_activity_list[0].flask_list))
				color = flasks_activity_list[0].flask_list[-1]
				count1 = 0
				pos_fill =  (38* 5) - (38 *  len(flasks_activity_list[1].flask_list))
				while (i == flasks_activity_list[0].flask_list[-1]) and (len(flasks_activity_list[1].flask_list) <5):
					count1+=1
					flasks_activity_list[1].flask_list.append(flasks_activity_list[0].flask_list[-1])
					del flasks_activity_list[0].flask_list[-1]
					if len(flasks_activity_list[0].flask_list) == 0:
						break
				Animation(pos_fill,count1,color,pos_del)

def lvl(lvl_item,link_on_lvl):
	screen.fill((71,74,81))
	pg.display.update()

	global key
	global run
	global flaskkey
	global flasks_activity_list
	
	button_back = Button(10,10,"level_menu",Button_back_active,Button_back_inactive,150,85)
	Button_again = Button(850,10,link_on_lvl,Button_again_active,Button_again_inactive,135,105)
	run = True
	key = None

	

	while run == True:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				sys.exit()
		screen.fill((71,74,81))

		if key != "win":
			for i in lvl_item:
				screen.blit(Inactive_flask_button,(i.x+23,i.y+230))
		else:
			for i in lvl_item:
				screen.blit(Active_flask_button,(i.x+23,i.y+230))

		button_back.DrawButtonAndGetAction()
		Button_again.DrawButtonAndGetAction()

		for i in lvl_item:
			i.ButtonFlask()
			i.Fill_Flasks()
			i.DrawFlask()

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
			flasks_activity_list = []
			
		if key == "win":
			run = False
			pg.display.update()
			pg.time.delay(1000)

		if key is not None:
			run = False

		fill_flask_count = 0
		for i in lvl_item:
			if ((len(list(set(i.flask_list))) == 1) and (len(i.flask_list) == 5)) or (len(i.flask_list) == 0):
				fill_flask_count+=1
		if fill_flask_count == len(lvl_item):
			key = "win"

		pg.display.update()
		screen.fill((71,74,81))
		pg.time.delay(30)

def Main_Menu():
	global key
	global run
	screen.fill((71,74,81))
	pg.display.update()
	button_play = Button(370,225,"level_menu",Button_play_active,Button_play_inactive,270,100)
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
		pg.time.delay(30)

def Levels():
	global key
	global run
	screen.fill((71,74,81))
	pg.display.update()
	key = None
	run = True
	button_back = Button(10,10,"main",Button_back_active,Button_back_inactive,150,85)
	
	button_lvl1 = Button(20,400,"lvl1",lvl1_active,lvl1_inactive,155,140)
	button_lvl2 = Button(220,400,"lvl2",lvl2_active,lvl2_inactive,155,140)
	button_lvl3 = Button(420,400,"lvl3",lvl3_active,lvl3_inactive,155,140)
	button_lvl4 = Button(620,400,"lvl4",lvl4_active,lvl4_inactive,155,140)
	button_lvl5 = Button(820,400,"lvl5",lvl5_active,lvl5_inactive,155,140)


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
Flask1 = pg.image.load("images/Flask.png").convert_alpha()
Flask1 = pg.transform.scale(Flask1,(73,211))

Flask2 = pg.image.load("images/Flask.png").convert_alpha()
Flask2 = pg.transform.scale(Flask2,(73,211))

Flask3 = pg.image.load("images/Flask.png").convert_alpha()
Flask3 = pg.transform.scale(Flask3,(73,211))

Flask4 = pg.image.load("images/Flask.png").convert_alpha()
Flask4 = pg.transform.scale(Flask4,(73,211))

Flask5 = pg.image.load("images/Flask.png").convert_alpha()
Flask5 = pg.transform.scale(Flask5,(73,211))

Flask6 = pg.image.load("images/Flask.png").convert_alpha()
Flask6 = pg.transform.scale(Flask6,(73,211))

Flask7 = pg.image.load("images/Flask.png").convert_alpha()
Flask7 = pg.transform.scale(Flask7,(73,211))

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
Win_text = pg.transform.scale(Win_text,(500,500))
"""images"""

run =True
key = "main"
flaskkey = None
flasks_activity_list = []


while True:
	"""lvl1"""
	link_on_lvl1 = "lvl1"
	Flasks1_1 = Flasks(260,320,["green","red","green","red","green"],Flask1)
	Flasks1_2 = Flasks(460,320,["red","green","red","green","red"],Flask2)
	Flasks1_3 = Flasks(660,320,[],Flask3)
	lvl1 = [Flasks1_1,Flasks1_2,Flasks1_3]

	"""lvl2"""
	link_on_lvl2 = "lvl2"
	Flasks2_1 = Flasks(170,320,["orange","orange","red","green","red"],Flask1)
	Flasks2_2 = Flasks(370,320,["green","orange","green","orange","red"],Flask2)
	Flasks2_3 = Flasks(570,320,["green","red","green","orange","red"],Flask3)
	Flasks2_4 = Flasks(770,320,[],Flask4)
	lvl2 = [Flasks2_1,Flasks2_2,Flasks2_3,Flasks2_4]

	"""lvl3"""
	link_on_lvl3 = "lvl3"
	Flasks3_1 = Flasks(65,320,["green","yellow","green","green","red"],Flask1)
	Flasks3_2 = Flasks(265,320,["blue","yellow","red","blue","yellow"],Flask2)
	Flasks3_3 = Flasks(465,320,["red","blue","blue","red","green"],Flask3)
	Flasks3_4 = Flasks(665,320,["red","yellow","blue","yellow","green"],Flask4)
	Flasks3_5 = Flasks(865,320,[],Flask5)
	lvl3 = [Flasks3_1,Flasks3_2,Flasks3_3,Flasks3_4,Flasks3_5]

	"""lvl4"""
	link_on_lvl4 = "lvl4"
	Flasks4_1 = Flasks(150,320,["orange","grey","orange","grey","grey"],Flask1)
	Flasks4_2 = Flasks(275,320,["grey","orange","orange","purple","pink"],Flask2)
	Flasks4_3 = Flasks(400,320,["blue","blue","blue","blue","purple"],Flask3)
	Flasks4_4 = Flasks(525,320,["grey","orange","purple","pink","pink"],Flask4)
	Flasks4_5 = Flasks(650,320,["blue","pink","pink","purple","purple"],Flask5)
	Flasks4_6 = Flasks(775,320,[],Flask6)
	lvl4 = [Flasks4_1,Flasks4_2,Flasks4_3,Flasks4_4,Flasks4_5,Flasks4_6]

	"""lvl5"""
	link_on_lvl5 = "lvl5"
	Flasks5_1 = Flasks(125-35,320,["salmon","khaki","red","red","red"],Flask1)
	Flasks5_2 = Flasks(250-35,320,["khaki","khaki","red","salmon","salmon"],Flask2)
	Flasks5_3 = Flasks(375-35,320,["pink","pink","lime","khaki","lime"],Flask3)
	Flasks5_4 = Flasks(500-35,320,["lime","yellow","salmon","salmon","khaki"],Flask4)
	Flasks5_5 = Flasks(625-35,320,["yellow","lime","pink","lime","yellow",],Flask5)
	Flasks5_6 = Flasks(750-35,320,["pink","yellow","pink","yellow","red"],Flask6)
	Flasks5_7 = Flasks(875-35,320,[],Flask7)  
	lvl5 = [Flasks5_1,Flasks5_2,Flasks5_3,Flasks5_4,Flasks5_5,Flasks5_6,Flasks5_7]

	if key == "win":
		Win()
	elif key == "main":
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
