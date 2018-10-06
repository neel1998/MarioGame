from board import *
import signal
from getch import _getChUnix as getChar
from alarmexception import AlarmException
import os
import time
import sys
from bullet import *
from print_villain import*
def move():
	def alarmhandler(signum, frame):
	    raise AlarmException
	def user_input(timeout=0.1):
		signal.signal(signal.SIGALRM, alarmhandler)
		signal.setitimer(signal.ITIMER_REAL, timeout)
		try:
			text = getChar()()
			signal.alarm(0)
			return text
		except AlarmException:
			pass
		signal.signal(signal.SIGALRM, signal.SIG_IGN)
		return ''
	char = user_input()
	return char
test=board()
player=test.player
i=0;
j=0;
l=8
t=0;
finalj=0
finali=0
power=0
level2=0
vt=0
time1=0
s=0
test.print_board(j)
onboard=False
while True:
	sys.stdout.write("\033c")

	if (onboard):
		player.posx+=test.f.dir
		i+=test.f.dir
		j+=test.f.dir

	l=8
	if time.time()-test.f.t>=0.1:
		test.f.t=time.time()
		test.f.posx+=test.f.dir
		if(test.f.posx>=388 and  test.f.dir==1):
			test.f.dir=-1
		elif(test.f.posx<=352 and  test.f.dir==-1):
			test.f.dir=1
		if ((test.f.posx<=player.posx<=player.posx+5 or player.posx<=test.f.posx<=player.posx+5)and player.posy+6==test.f.posy):
			onboard=True
		else:
			onboard=False
	#quit
	if(player.life<0):
		print('\033[95m'+"GAME OVER\nYOUR SCORE="+str(player.score)+"\nYOUR COINS="+str(player.coins)+"\n"+'\033[0m')
		quit()
	
	if player.posx==775:
		print('\033[95m'+"GAME OVER\nYOUR SCORE="+str(player.score)+"\nYOUR COINS="+str(player.coins)+"\n"+'\033[0m')
		quit()

	#gravity
	try:
		if((test.level1[player.posy+6][player.posx+5]!='\033[92m'+"X"+'\033[0m' and test.level1[player.posy+6][player.posx+1]!='\033[92m'+"X"+'\033[0m')
			and (test.level1[player.posy+6][player.posx+5]!='X' and test.level1[player.posy+6][player.posx+1]!='X')
			# and onboard==False
		 # and (test.level1[player.posy+6][player.posx+5]!="#" and test.level1[player.posy+6][player.posx+1]!="#") 
		 # and (test.level1[player.posy+6][player.posx+5]!="*" and test.level1[player.posy+6][player.posx+1]!="*")
		 ):
			g=1
			player.posy+=1
		# test.print_board(j)

	except:
		player.posx=0
		j=0
		i=0
		player.posy=28
		player.life-=1
		# test.print_board(j)
	#moves
	char=move()
	if char=='d':
		if ((test.level1[player.posy+1][player.posx+6]!="|" 
		and test.level1[player.posy][player.posx+5]!="|"
		 and test.level1[player.posy+2][player.posx+5]!="|" 
		 and test.level1[player.posy+3][player.posx+6]!="|" 
		 and test.level1[player.posy+4][player.posx+5]!="|" 
		 and test.level1[player.posy+5][player.posx+5]!="|" )
		and
		(test.level1[player.posy+1][player.posx+6]!="X" 
		and test.level1[player.posy][player.posx+5]!="X"
		 and test.level1[player.posy+2][player.posx+5]!="X" 
		 and test.level1[player.posy+3][player.posx+6]!="X" 
		 and test.level1[player.posy+4][player.posx+5]!="X" 
		 and test.level1[player.posy+5][player.posx+5]!="X")
		and
		(test.level1[player.posy+1][player.posx+6]!='\033[92m'+"X"+'\033[0m' 
		and test.level1[player.posy][player.posx+5]!='\033[92m'+"X"+'\033[0m'
		 and test.level1[player.posy+2][player.posx+5]!='\033[92m'+"X"+'\033[0m'
		 and test.level1[player.posy+3][player.posx+6]!='\033[92m'+"X"+'\033[0m' 
		 and test.level1[player.posy+4][player.posx+5]!='\033[92m'+"X"+'\033[0m' 
		 and test.level1[player.posy+5][player.posx+5]!='\033[92m'+"X"+'\033[0m')
		and	j+75<=1000 and player.level==1):
			i+=1
			player.score+=1
			j=i-75
			if i<75:
				j=0
			player.posx+=1
			# test.print_board(j)
		elif player.level==2:
			player.posx+=1
	elif char=='a':
		if (test.level1[player.posy+1][player.posx-1]!="|"
			and
			test.level1[player.posy+1][player.posx-1]!="X"
			and
			test.level1[player.posy+3][player.posx-1]!="X"
			and
			test.level1[player.posy+3][player.posx-1]!="|"
			and
			test.level1[player.posy+1][player.posx-1]!='\033[92m'+"X"+'\033[0m'
			and
			test.level1[player.posy+3][player.posx-1]!='\033[92m'+"X"+'\033[0m'
			and
			player.posx>=0):
			i-=1
			j=i-75
			if i<75:
				j=0
			player.posx-=1
			# test.print_board(j)
	
	elif char=='w' and t<2:
		for ju in range(player.posy-1,player.posy-8,-1):
			if ((test.level1[ju][player.posx+1]=="X") 
			 or (test.level1[ju][player.posx+2]=="X") 
			 or (test.level1[ju][player.posx+3]=="X")
			 or (test.level1[ju][player.posx+4]=="X")):
				# try:
				for b in test.bricks:
					if player.posx<=b.x<=player.posx+4 and b.y==ju-2:
						if b.t!=-2:
							player.coins+=1
							if b.t==0:
								test.bricks.remove(b)
							else:
								b.t-=1
							break	
				l=player.posy-ju
				break
		if player.posy-l>=0:
			player.posy-=l
		# test.print_board(j)
		t+=1		
	elif char=='q':
		print('\033[95m'+"GAME OVER\nYOUR SCORE="+str(player.score)+"\nYOUR COINS="+str(player.coins)+"\n"+'\033[0m')
		quit()
	elif char==" " and power==1:
		bu=bullet(player.posx+6,player.posy+4,0,1)
		test.bullets.append(bu)
	elif char=='s' and 629<=player.posx<=638 and level2==0:
		level2=1
		player.level=2
		finali=i
		finalj=j
		i=0
		j=0
		player.posx=10
		player.posy=10
	#ground touch
	try:
		if(test.level1[player.posy+6][player.posx+5]=='\033[92m'+"X"+'\033[0m' or test.level1[player.posy+6][player.posx+1]=='\033[92m'+"X"+'\033[0m' or
			test.level1[player.posy+6][player.posx+5]=='X' or test.level1[player.posy+6][player.posx+1]=='X'
			):
			g=0
			t=0
	except:
		player.life-=1
		player.posx=0
		i=0
		j=0
		player.posy=28
		# test.print_board(j)

	#enemies
	for e in test.enemies:
		if e.posx>799 or e.posx<0:
			test.enemies.remove(e)
		if(((e.posx==player.posx+5) or (e.posx+1==player.posy))and 26<=player.posy<=28):
			player.life-=1
			player.posx=0
			player.score-=50
			j=0
			i=0
			# test.print_board(j)

		try:
			if((j<=e.posx<=j+150 or j-150<=e.posx<=j) and time.time()-e.t>=0.1 ):
				# erase_enemy(test.level1,test.enemies)				
				e.posx-=e.dir
				e.t=time.time()
				# test.print_board(j)
				if e.dir==1 and test.level1[e.posy][e.posx-1]!=" ":
					if test.level1[e.posy][e.posx-1]=="*":
						player.score+=10
						test.enemies.remove(e)
						# test.print_board(j)
						# break
					else:
						e.dir=0-e.dir
				elif e.dir==(0-1) and test.level1[e.posy][e.posx+3]!=" ":
					e.dir=0-e.dir	
				if(test.level1[e.posy+2][e.posx]!='\033[92m'+"X"+'\033[0m'):
					e.posy+=1
				# test.print_board(j)
			if(((player.posx<=e.posx<=player.posx+5 
				or (e.posx<=player.posx and player.posx<=e.posx+2<=player.posx+5) )
				and player.posy+6==e.posy)):
				player.score+=10
				test.enemies.remove(e)
				player.posy-=3
		except:
			# pass
			test.enemies.remove(e)
			# player.score+=10
			# test.print_board(j)	
	#bullets
	for bl in test.bullets:
		if time.time()-bl.t>=0.1:
			bl.t=time.time()
			if(bl.x+1<799):			
				bl.x+=1
			else:
				test.bullets.remove(bl)
				break
		if test.level1[bl.y][bl.x+1]!=" ":
			if bl.x==test.v.x and test.v.y<=bl.y<=test.v.y+10:
				test.v.life-=1
				player.score+50
			test.bullets.remove(bl)
		if bl.x-player.posx>150:
			test.bullets.remove(bl)
	
	if player.level==2:
		if player.posx==145 and 30<=player.posy<40:
			player.posx=635
			player.posy=17
			player.level=1
			i=finali
			j=finalj
			power=1
			player.life+=5
		for c in test.co:
			if ((c.x==player.posx+6 or c.x+3==player.posx or player.posx<=c.x<=player.posx+5) and (c.y==player.posy+4 or c.y==player.posy+6 )):
				test.co.remove(c)
				player.coins+=1
	

	if time.time()-test.v.t>=1:
		test.v.t=time.time()
		test.v.x=random.randint(730,750)
		test.v.y=random.randint(15,23)
	

	if time.time()-time1>=3 and test.alivev==1:
		time1=time.time()
		ebullet=bullet(test.v.x,test.v.y+7,0,2)
		test.eb.append(ebullet)

	for ebullet in test.eb:
		if time.time()-ebullet.t>=0.1:
			ebullet.x-=1
			if ebullet.x<=678:
				test.eb.remove(ebullet)
			ebullet.t=time.time()

		if ebullet.x==player.posx+5 and player.posy<=ebullet.y<=player.posy+6:
			player.life-=1
			test.eb.remove(ebullet)

	if test.alivev==1 and player.posx>=730:
		player.posx-=20
		player.life-=1

	if test.v.life<0:
		test.alivev=0
		if s==0:
			player.score+=100
			s=1

	test.print_board(j)