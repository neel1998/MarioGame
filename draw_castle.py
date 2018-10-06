def draw_castle(self,x,y):
	level1=self.level1
	for i in range(y,34,1):
		for j in range(x,x+40,1):
			level1[i][j]='\033[93m'+"#"+'\033[0m'

	for i in range(y-7,y,1):
		for j in range(x+10,x+30,1):
			level1[i][j]='\033[93m'+"#"+'\033[0m'

	for i in range(y-12,y-7,1):
		level1[i][x+20]='\033[93m'+"#"+'\033[0m'

	for i in range(y-5,y,1):
		level1[i][x]='\033[93m'+"#"+'\033[0m'
		level1[i][x+39]='\033[93m'+"#"+'\033[0m'

	for i in range(y-5,y-2,1):
		for j in range(x+1,x+5,1):
			level1[i][j]='\033[91m'+"M"+'\033[0m'

	for i in range(y-12,y-9,1):
		for j in range(x+21,x+26,1):
			level1[i][j]='\033[91m'+"M"+'\033[0m'

	for i in range(y-5,y-2,1):
		for j in range(x+40,x+44,1):
			level1[i][j]='\033[91m'+"M"+'\033[0m'

	for i in range(y,34,1):
		for j in range(x+17,x+24,1):
			level1[i][j]=" "	

	for i in range(y+5,34,1):
		for j in range(x+5,x+11,1):
			level1[i][j]=" "
	for i in range(y+5,34,1):
		for j in range(x+30,x+36,1):
			level1[i][j]=" "