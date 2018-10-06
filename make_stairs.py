def make_stairs(self,x,h,d):
	level1=self.level1
	if(d==1):
		for i in range(33,33-3*h+1,-3):
			for j in range(x+4*(int((33-i)/3)),x+4*h+1,1):
				level1[i][j]='\033[92m'+"X"+'\033[0m'
				level1[i-1][j]='\033[92m'+"X"+'\033[0m'
				level1[i-2][j]='\033[92m'+"X"+'\033[0m'
	else:
		for i in range(33,33-3*h+1,-3):
			for j in range(x,x+4*h-4*(int((33-i)/3))+1,1):
				level1[i][j]='\033[92m'+"X"+'\033[0m'
				level1[i-1][j]='\033[92m'+"X"+'\033[0m'
				level1[i-2][j]='\033[92m'+"X"+'\033[0m'
