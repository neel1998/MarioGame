def print_enemy(self):
	level1=self.level1
	for e in self.enemies:
		level1[e.posy][e.posx]='\033[91m'+"{"+'\033[0m'
		level1[e.posy][e.posx+1]='\033[91m'+"O"+'\033[0m'
		level1[e.posy][e.posx+2]='\033[91m'+"O"+'\033[0m'
		level1[e.posy][e.posx+3]='\033[91m'+"}"+'\033[0m'
		if(e.posx%2):
			level1[e.posy+1][e.posx+1]='\033[95m'+"/"+'\033[0m'
			level1[e.posy+1][e.posx+2]='\033[95m'+"\\"+'\033[0m'
		else:
			level1[e.posy+1][e.posx+1]='\033[95m'+"\\"+'\033[0m'
			level1[e.posy+1][e.posx+2]='\033[95m'+"/"+'\033[0m'