def draw_brick(self,bricks):
	level1=self.level1
	for i in bricks:
		# for j in i:
			x=i.x
			y=i.y
			t=i.t
			if t==-2:
				char="X"
			else:
				char='\033[91m'+str(t)+'\033[0m'
			level1[y][x]="X"
			level1[y][x+1]="X"
			level1[y][x+2]="X"
			level1[y][x+3]="X"
			level1[y+1][x]="X"
			level1[y+1][x+3]="X"
			level1[y+2][x]="X"
			level1[y+2][x+1]="X"
			level1[y+2][x+2]="X"
			level1[y+2][x+3]="X"

			level1[y+1][x+1]=char
			level1[y+1][x+2]=char