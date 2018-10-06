import random
from mario import *
from print_player import*
from print_bg import*
from brick import *
from draw_brick import*
from enemy import*
from print_enemy import*
from fl import *
from print_bullet import*
from make_brick import*
from coin import *
from draw_coin import*
from write import*
import time
from print_villain import*
from villain import*
from win import *
class board:
	bricks=[]
	bricks2=[]
	level1=[]
	enemies=[]
	bullets=[]
	eb=[]

	
	co=[]

	f=fl(355,35,1,0)

	vt=0


	player=mario(0,28,5,0,0,1);
	for j in range(40):
		row=[]
		for k in range(1000):
			row.append(" ")
		level1.append(row)
	
	
	
	e=enemy(140,20,1,0)
	enemies.append(e)

	e=enemy(170,32,1,0)
	enemies.append(e)

	e=enemy(150,32,-1,0)
	enemies.append(e)

	e=enemy(215,20,1,0)
	enemies.append(e)

	e=enemy(265,32,1,0)
	enemies.append(e)	

	e=enemy(580,32,1,0)
	enemies.append(e)

	e=enemy(590,32,1,0)
	enemies.append(e)

	v=villain(730,22,0,10)

	brick(bricks)
	for i in range(70,130,5):
		b=make_brick(i,30,-2)
		bricks2.append(b)
		c=coin(i+1,28)
		co.append(c)

	for i in range(50,80,5):
		b=make_brick(i,20,-2)
		bricks2.append(b)
		c=coin(i+1,18)
		co.append(c)
	for i in range(10,60,5):
		b=make_brick(i,30,-2)
		bricks2.append(b)
		c=coin(i+1,28)
		co.append(c)
	for i in range(100,140,5):
		b=make_brick(i,20,-2)
		bricks2.append(b)
		c=coin(i+1,18)
		co.append(c)
	t=0
	alivev=1
	# print_background(level1)
	# draw_brick(level1,bricks)
	def print_board(self,k):
		
		if self.player.level==1:
			print_background(self,k)
			print_player(self)
			draw_brick(self,self.bricks)
			print_enemy(self)
			print_bullet(self,self.bullets)
			print_bullet(self,self.eb)
						
			if self.alivev==1:
				print_villain(self,self.v.x,self.v.y)

			if self.alivev==0:
				win(self)
				# time.sleep(3)

			temp=""

			s='\033[93m'+"Life="+str(self.player.life)+" Score="+str(self.player.score)+" Coins="+str(self.player.coins)+"\n"+'\033[0m'
			if k>=550 and self.alivev==1:
				s+='\033[93m'+"Boss Life="+str(self.v.life)+"\n"+'\033[0m'

			temp+=s
			
			for i in range(40):
				
				for j in range(k,k+150,1):
					temp+=self.level1[i][j]
				
			print(temp)
		else:
			print_background(self,k)
			print_player(self)
			draw_brick(self,self.bricks2)
			draw_coin(self,self.co)

			if (time.time()-self.t>=0.3):
				write(self)
				self.t=time.time()

			temp=""

			s='\033[93m'+"Life="+str(self.player.life)+" Score="+str(self.player.score)+" Coins="+str(self.player.coins)+"\n"+'\033[0m'

			temp+=s
			
			for i in range(40):
				
				for j in range(k,k+150,1):
					temp+=self.level1[i][j]
				
			print(temp)
