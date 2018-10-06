def draw_coin(self,coins):
	level1=self.level1
	for i in coins:
		level1[i.y][i.x]='\033[93m'+"("+'\033[0m'
		level1[i.y][i.x+1]='\033[93m'+"$"+'\033[0m'
		level1[i.y][i.x+2]='\033[93m'+")"+'\033[0m'			