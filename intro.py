from curses import initscr, curs_set,newwin,endwin,KEY_RIGHT,KEY_LEFT,KEY_DOWN,A_UNDERLINE,KEY_UP,A_DIM,beep,noecho,start_color,A_REVERSE,COLOR_BLUE,COLOR_RED,COLOR_GREEN,init_color,color_pair,A_BOLD
initscr()
curs_set(0)
start_color()
curs_set(0)
win = newwin(33,100,1,20)
win.keypad(1)
win.nodelay(1)
win.border(124,124,45,45,'*','*','*','*')
win.addstr(2,29,'~~~WELCOME TO THE ROBOT-BOMB DEFUSER GAME~~~',A_BOLD)
win.addstr(4,2,'INTRODUCTION :',A_REVERSE)
win.addstr(6,4,'GAME SCENARIO :',A_BOLD)
win.addstr(8,6,'WE ARE IN THE ROBOT CITY AND DEATHLY BOT HAS PLANTED A BOMB IN THE CITY.',A_UNDERLINE)
win.addstr(9,6,'NOW IT\'s YOUR TURN TO SAVE THE CITY AS SUPERROBOT IS OUT OF THE CITY',A_UNDERLINE)
win.addstr(10,6,'SO GRAB THE DEFUSED CODES AND DEFUSE THE BOMB AND MAKE ROBOT CITY FREE OF PROBLEMS',A_UNDERLINE)
win.addstr(11,6,'LAST BUT NOT THE LEAST ::',A_UNDERLINE)
win.addstr(12,6,'>>>>BE AWARE OF THE BOT\'s NEXT REACTION<<<<<',A_BOLD)
win.addstr(14,4,'GAME PLAY:',A_BOLD)
win.addstr(16,6,'>>THERE ARE TWO LEVELS IN THE GAME :',A_UNDERLINE)
win.addstr(17,7,'*BEGINNER',A_UNDERLINE)
win.addstr(18,7,'*AMATEUR',A_UNDERLINE)
win.addstr(20,4,'GAME CONTROLS :',A_BOLD)
win.addstr(22,6,'<- TO MOVE LEFT,-> TO MOVE RIGHT',A_UNDERLINE)
win.addstr(23,6,'<UP ARROW KEY> TO MOVE UP,<DOWN ARROW KEY>TO MOVE DOWN',A_UNDERLINE)
win.addstr(25,4,'GAME HELP :',A_BOLD)
win.addstr(27,6,'>>p or P TO PAUSE THE GAME , PRESS Esc TO QUIT FROM GAME AT ANY LEVEL',A_UNDERLINE)
win.addstr(29,18,'PRESS n TO ENTER THE GAME LEVEL OR ELSE PRESS Esc TO QUIT FROM GAME',A_REVERSE)
win.addstr(31,33,'~~~~~<<<<CREATED BY SHARAD GUPTA>>>>~~~~~',A_BOLD)
key = win.getch()
noecho()
while(1):
  key=win.getch()
	noecho()
	if key == 27 or key == ord('n'):
		break
if key == 27:
	endwin()
if key == ord('n'):
	endwin()
	import firstlevel
	
