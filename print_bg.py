import random
from make_stairs import*
from draw_castle import*
from colorama import *
def print_background(self,ss):
		# init(autoreset=True)
		level1=self.level1
		for i in range(40):
			for j in range(1000):
				level1[i][j]=" "
		#Ground
		# level1[0].insert(0,s)
		if self.player.level==1:
			for j in range(0,1000,8):
				for k in range(j,j+4,1):
					level1[35][k]='\033[93m'+"/"+'\033[0m'
					level1[37][k]='\033[93m'+"/"+'\033[0m'
					level1[39][k]='\033[93m'+"/"+'\033[0m'
			for j in range(4,1000-8,8):
				for k in range(j,j+4,1):
					level1[36][k]='\033[93m'+"/"+'\033[0m'
					level1[38][k]='\033[93m'+"/"+'\033[0m'
			for j in range(1000):
				level1[34][j]='\033[92m'+"X"+'\033[0m'

			#pipes
			for i in range(27,34,1):
				level1[i][130]="|"
				level1[i][131]="|"
				level1[i][135]="|"			
				level1[i][136]="|"
			level1[26][129]="["
			level1[26][137]="]"
			for i in range(129,138,1):
				level1[26][i]='\033[92m'+"X"+'\033[0m'


			for i in range(25,34,1):
				level1[i][180]="|"
				level1[i][181]="|"
				level1[i][185]="|"			
				level1[i][186]="|"
			level1[24][179]="["
			level1[24][187]="]"
			for i in range(179,188,1):
				level1[24][i]='\033[92m'+"X"+'\033[0m'

			for i in range(25,34,1):
				level1[i][210]="|"
				level1[i][211]="|"
				level1[i][215]="|"			
				level1[i][216]="|"
			level1[24][209]="["
			level1[24][217]="]"
			for i in range(209,218,1):
				level1[24][i]='\033[92m'+"X"+'\033[0m'

			for i in range(25,34,1):
				level1[i][435]="|"
				level1[i][436]="|"
				level1[i][440]="|"			
				level1[i][441]="|"
			level1[24][434]="["
			level1[24][442]="]"
			for i in range(434,443,1):
				level1[24][i]='\033[92m'+"X"+'\033[0m'

			for i in range(25,34,1):
				level1[i][300]="|"
				level1[i][301]="|"
				level1[i][305]="|"			
				level1[i][306]="|"
			level1[24][299]="["
			level1[24][307]="]"
			for i in range(299,308,1):
				level1[24][i]='\033[92m'+"X"+'\033[0m'

			for i in range(25,34,1):
				level1[i][630]="|"
				level1[i][631]="|"
				level1[i][635]="|"			
				level1[i][636]="|"
			level1[24][629]="["
			level1[24][637]="]"
			for i in range(629,638,1):
				level1[24][i]='\033[92m'+"X"+'\033[0m'
			level1[23][631]='\033[91m'+"B"+'\033[0m'
			level1[23][632]='\033[91m'+"O"+'\033[0m'
			level1[23][633]='\033[91m'+"N"+'\033[0m'
			level1[23][634]='\033[91m'+"U"+'\033[0m'
			level1[23][635]='\033[91m'+"S"+'\033[0m'

			level1[22][633]='\033[91m'+"+"+'\033[0m'

			level1[21][631]='\033[91m'+"L"+'\033[0m'
			level1[21][632]='\033[91m'+"I"+'\033[0m'
			level1[21][633]='\033[91m'+"V"+'\033[0m'
			level1[21][634]='\033[91m'+"E"+'\033[0m'
			level1[21][635]='\033[91m'+"S"+'\033[0m'

			level1[20][633]='\033[91m'+"+"+'\033[0m'

			level1[19][632]='\033[91m'+"G"+'\033[0m'
			level1[19][633]='\033[91m'+"U"+'\033[0m'
			level1[19][634]='\033[91m'+"N"+'\033[0m'
			#pit
			for i in range(350,400,1):
				for j in range(34,40,1):
					level1[j][i]=" "
			for i in range(270,280,1):
				for j in range(34,40,1):
					level1[j][i]=" "
			for i in range(450,460,1):
				for j in range(34,40,1):
					level1[j][i]=" "
			for i in range(600,610,1):
				for j in range(34,40,1):
					level1[j][i]=" "	
			#Cloud
			for i in range(1,150*5,150):
				for j in range(20,150,30):
					if j==20:
						t=5
					elif j==50:
						t=15
					elif j==80:
						t=8
					elif j==130:
						t=2
					else:
						t=10
					level1[t][i+j+3]='\033[94m'+"_"+'\033[0m'
					level1[t+1][i+j+1]='\033[94m'+"_"+'\033[0m'
					level1[t+1][i+j+2]='\033[94m'+"("+'\033[0m'
					level1[t+1][i+j+4]='\033[94m'+")"+'\033[0m'
					level1[t+2][i+j]='\033[94m'+"("+'\033[0m'
					level1[t+2][i+j+1]='\033[94m'+"_"+'\033[0m'
					level1[t+2][i+j+2]='\033[94m'+"_"+'\033[0m'
					level1[t+2][i+j+3]='\033[94m'+"_"+'\033[0m'
					level1[t+2][i+j+4]='\033[94m'+"_"+'\033[0m'
					level1[t+2][i+j+5]='\033[94m'+")"+'\033[0m'
			# float
			for i in range(self.f.posx,self.f.posx+10,1):
				level1[self.f.posy][i]="X" 
			#Stairs
			make_stairs(self,480,5,1)
			make_stairs(self,505,4,-1)
			make_stairs(self,650,7,1)
			draw_castle(self,780,23)		
		else:
			for i in range(40):
				for j in range(150):
					if j==0 or j==149:
						level1[i][j]='\033[92m'+"X"+'\033[0m'
			for j in range(150):
				level1[0][j]='\033[92m'+"X"+'\033[0m'
				level1[39][j]='\033[92m'+"X"+'\033[0m'
			for j in range(5,15,1):
				level1[0][j]=" "
			for i in range(30,40,1):
				level1[i][149]=" "