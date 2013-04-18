from curses import initscr, COLOR_YELLOW,COLOR_CYAN,COLOR_MAGENTA,curs_set,newwin,endwin,KEY_RIGHT,COLOR_BLACK,KEY_LEFT,init_pair,KEY_DOWN,KEY_UP,beep,noecho,start_color,A_REVERSE,COLOR_BLUE,COLOR_RED,COLOR_GREEN,init_color,color_pair
from random import randrange,sample
initscr()
start_color()
init_pair(1,COLOR_RED,COLOR_BLACK)
init_pair(2,COLOR_GREEN,COLOR_BLACK)
init_pair(3,COLOR_BLUE,COLOR_BLACK)
init_pair(4,COLOR_YELLOW,COLOR_BLACK)
init_pair(5,COLOR_MAGENTA,COLOR_BLACK)
init_pair(6,COLOR_CYAN,COLOR_BLACK)
curs_set(0)
win = newwin(30,80,2,30)
win.keypad(1)
win.nodelay(1)
win.border(124,124,45,45,'*','*','*','*')
robo_width=5
robo_height=5
bomb=[randrange(9,79,1),randrange(8,29,1)]
win.addch(bomb[1],bomb[0],'B',color_pair(5))
class machine():
  pass
class Robot():
	A=machine()
#A.	
	def __init__(self):
		self.robo=[[4,5],[5,5],[6,5],[7,5],[8,5],[3,6],[4,6],[5,6],[6,6],[7,6],[8,6],[9,6],[4,7],[8,7]]
		self.decodes=0
		self.flag=0
		self.flag1=0
		self.points=0
	def robot_moves(self,x):
		if x == KEY_RIGHT:
			for i in range(len(self.robo)):
				self.robo[i][0]+=1
		if x == KEY_LEFT:
			for i in range(len(self.robo)):
				self.robo[i][0]-=1
		if x == KEY_UP:
			for i in range(len(self.robo)):
				self.robo[i][1]-=1
		if x == KEY_DOWN:
			for i in range(len(self.robo)):
				self.robo[i][1]+=1
	def print_space(self,x):
		if x == KEY_RIGHT:
			for i in range(len(self.robo)):
				win.addch(self.robo[i][1],self.robo[i][0]-1,' ')
		if x == KEY_LEFT:
			for i in range(len(self.robo)):
				win.addch(self.robo[i][1],self.robo[i][0]+1,' ')
		if x == KEY_UP:
			for i in range(len(self.robo)):
				win.addch(self.robo[i][1]+1,self.robo[i][0],' ')
		if x == KEY_DOWN:
			for i in range(len(self.robo)):
				win.addch(self.robo[i][1]-1,self.robo[i][0],' ')
	def print_robot(self):
		win.addstr(self.robo[0][1],self.robo[0][0],'[i_i]',color_pair(1))
		win.addstr(self.robo[5][1],self.robo[5][0],'/|<@>|\\',color_pair(2))
		win.addstr(self.robo[12][1],self.robo[12][0],')',color_pair(3))
		win.addstr(self.robo[13][1],self.robo[13][0],'(',color_pair(3))

	def check(self):
		for i in range(len(self.robo)):
			for j in range(len(d)):
				if d[j]==self.robo[i]:
					d[j]=[]
					self.decodes+=1
					self.points+=10
		for k in range(len(self.robo)):
			if self.robo[k] == bomb:
				self.flag1=1
				break
		if self.robo[11][0] > 79 or  self.robo[5][0] < 1 or  self.robo[0][1] < 1 or self.robo[12][1] > 28:
			self.flag=1

robot=Robot()
key=KEY_RIGHT
level=1	
flag=0
d=[]
while(len(d)!=5):
	d = [n for n in [[randrange(1,79,1),randrange(1,29,1)] for x in range(5)] if n not in robot.robo or bomb]
for i in range(len(d)):
	win.addch(d[i][1],d[i][0],'D',color_pair(6))
def game_play():	
	key=KEY_RIGHT
	flag=0
	while key!=27:
		win.addstr(0,4,'<( ',color_pair(4))
		win.addstr(0,7,'DEFUSES COLLECTED',A_REVERSE)
		win.addstr(0,24,': ' + str(robot.decodes) + ')>',color_pair(4))
		win.addstr(29,60,'<( ',color_pair(6))
		win.addstr(29,63,'LEVEL',A_REVERSE) 
		win.addstr(29,68,' : ' + str(level) + ')>',color_pair(6))
		win.timeout(150 - (robot.decodes)*10)
		prevkey = key
		keystroke = win.getch()
		noecho()
		if keystroke == -1:
			key=key
		else:
			key = keystroke
		if key == ord('p') :
			while(1):
				key = win.getch()
				noecho()
				if key==ord('p'):
					break
	
				if key == 27 :
					flag=1
					break
			key = prevkey
		if flag == 1:
			break
		robot.robot_moves(key)
		robot.check()
		if robot.flag == 0:
			robot.print_space(key)
			robot.print_robot()
		if robot.flag == 1 or robot.flag1==1:
			break
	endwin()
game_play()
if robot.decodes == 5 and robot.flag1==1:
#stopgame=False
		win = newwin(30,80,2,30)
		win.border(124,124,45,45,'*','*','*','*')
		win.addstr(12,26,'!!!!!!YOU WON THE GAME WITH!!!!!!')
		win.addstr(13,25,'@@@@@YOU EARNED -> ' +str(robot.points)+' POINTS@@@@@')
		win.addstr(14,23,'~~~PRESS n TO ENTER THE SECOND LEVEL~~~')
		win.addstr(15,24,'>>>PRESS Esc KEY TO QUIT FROM GAME<<<') 
		while(1):
			key = win.getch()
			noecho()
			if key == 27 or key == ord('n'):
				break
		if key == 27:
		 	endwin()
		if key == ord('n'):
			endwin()
			import secondlevel
else:
		win = newwin(30,80,2,30)
		win.border(124,124,45,45,'*','*','*','*')
		win.addstr(12,25,'!!!!!!YOU LOSE THE GAME!!!!!!')
		win.addstr(13,26,'@@@@YOU EARNED -> ' +str(robot.points)+' POINTS@@@@')
		win.addstr(14,24,'>>>PRESS Esc KEY TO QUIT FROM GAME<<<') 
		while(win.getch()!=27):
			continue
		endwin()

