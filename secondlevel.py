from curses import initscr,COLOR_CYAN,curs_set,init_pair,color_pair,newwin,endwin,KEY_RIGHT,COLOR_BLACK,COLOR_MAGENTA,COLOR_YELLOW,KEY_LEFT,KEY_DOWN,KEY_UP,beep,noecho,start_color,A_REVERSE,COLOR_BLUE,COLOR_RED,COLOR_GREEN,init_color,A_DIM
from random import randrange,sample
initscr()
curs_set(0)
start_color()
init_pair(1,COLOR_RED,COLOR_BLACK)
init_pair(2,COLOR_YELLOW,COLOR_BLACK)
init_pair(3,COLOR_GREEN,COLOR_BLACK)
init_pair(4,COLOR_MAGENTA,COLOR_BLACK)
init_pair(5,COLOR_BLUE,COLOR_BLACK)
init_pair(6,COLOR_CYAN,COLOR_BLACK)
noecho()
dirkeys=[KEY_RIGHT,KEY_LEFT,KEY_UP,KEY_DOWN,27]
win = newwin(30,80,2,30)
win.keypad(1)
win.nodelay(1)
win.border(124,124,45,45,'*','*','*','*')
bomb=[randrange(39,55,1),randrange(11,16,1)]
win.addch(bomb[1],bomb[0],'B',color_pair(4))
class machine():
  pass
class Robot():
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
		win.addstr(self.robo[0][1],self.robo[0][0],'[i_i]',color_pair(5))
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
		for k in range(len(self.robo)):
			for j in range(len(m)):
				if m[j]==self.robo[k]:
					self.flag=1
					break
		for k in range(len(self.robo)):
			for j in range(len(l)):
				if l[j]==self.robo[k]:
					self.flag=1
					break
		for k in range(len(self.robo)):
			if self.robo[k] == s1 or self.robo[k] == s2:
					self.flag=1
		if self.robo[11][0] > 78 or  self.robo[5][0] < 1 or  self.robo[0][1] < 1 or self.robo[12][1] > 28:
			self.flag=1

robot=Robot()
key=KEY_RIGHT
level=2	
flag=0
temp=0
d=[]
m=[]
key1=KEY_RIGHT
s1flag=0
s1=[38,10]
s2=[55,16]
l=[[37,9],[37,10],[37,11],[37,12],[37,13],[37,14],[37,15],[37,16],[37,17],[56,9],[56,10],[56,11],[56,12],[56,13],[56,14],[56,15],[56,16],[56,17]]
for i in range(len(l)):
	win.addch(l[i][1],l[i][0],'^',color_pair(6))
while(len(d)!=10):
	for i in range(3):
		d.append([randrange(9,79,1),randrange(1,8,1)])
	for i in range(3):
		d.append([randrange(1,36,1),randrange(9,29,1)])
	for i in range(2):
		d.append([randrange(57,79,1),randrange(9,29,1)])
		d.append([randrange(37,56,1),randrange(18,29,1)])
	d = [n for n in d if n not in robot.robo or l or bomb]
for i in range(len(d)):
	win.addch(d[i][1],d[i][0],'D',color_pair(2))
#while(len(m)!=15):
for i in range(3):
	m.append([randrange(9,79,1),randrange(1,8,1)])
for i in range(3):
	m.append([randrange(1,36,1),randrange(9,29,1)])
for i in range(2):
	m.append([randrange(57,79,1),randrange(9,29,1)])
	m.append([randrange(37,56,1),randrange(18,29,1)])
m = [n for n in m if n not in robot.robo or l or d or bomb]
for i in range(len(m)):
	win.addch(m[i][1],m[i][0],'*',color_pair(5))
key=KEY_RIGHT
flag=0
robot.print_robot()
while key!=27:
	win.addstr(0,4,'<( ',color_pair(3))
	win.addstr(0,7,'DECODES COLLECTED',A_REVERSE)
	win.addstr(0,24,': ' + str(robot.decodes) + ')>',color_pair(3))
	win.addstr(29,60,'<( ',color_pair(5))
	win.addstr(29,63,'LEVEL',A_REVERSE) 
	win.addstr(29,68,' : ' + str(level) + ')>',color_pair(5))
	win.timeout(250 - (robot.decodes)*4)
	if key1 == KEY_RIGHT:
		s1[0]+=1
		s2[0]-=1
		if s1[0] == 55:
			key1 = KEY_LEFT
		win.addch(s1[1],s1[0]-1,' ')
		win.addch(s2[1],s2[0]+1,' ')
		win.addch(s1[1],s1[0],'(',color_pair(1))
		win.addch(s2[1],s2[0],')',color_pair(1))
	if key1 == KEY_LEFT:
		s1[0]-=1
		s2[0]+=1
		if s1[0] == 38:
			key1 = KEY_RIGHT
		win.addch(s1[1],s1[0]+1,' ')
		win.addch(s2[1],s2[0]-1,' ')
		win.addch(s1[1],s1[0],')',color_pair(1))
		win.addch(s2[1],s2[0],'(',color_pair(1))
	prevkey = key
	keystroke = win.getch()
	if keystroke not in dirkeys and keystroke !=27 and  keystroke != ord('p') and keystroke != ord('P'):
		key=key
	else:
		key = keystroke
	if key == ord('p') or key == ord('P'):
		while(1):
			key = win.getch()
			if key==ord('p') or key == ord('P'):
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
if robot.decodes == 10 and robot.flag1==1:
		win = newwin(30,80,2,30)
		win.border(124,124,45,45,'*','*','*','*')
		win.addstr(12,26,'!!!!!!YOU WON THE GAME!!!!!!')
		win.addstr(13,25,'@@@@YOU EARNED -> ' +str(robot.points)+' POINTS@@@@')
		win.addstr(14,24,'>>>PRESS Esc KEY TO QUIT FROM GAME<<<') 
		while(win.getch()!=27):continue
		endwin()
else:
		win = newwin(30,80,2,30)
		win.border(124,124,45,45,'*','*','*','*')
		win.addstr(12,26,'!!!!!!YOU LOSE THE GAME!!!!!!')
		win.addstr(13,25,'@@@@YOU EARNED -> ' +str(robot.points)+' POINTS@@@@')
		win.addstr(14,24,'>>>PRESS Esc KEY TO QUIT FROM GAME<<<') 
		while(win.getch()!=27):continue
		endwin()
