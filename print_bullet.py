def print_bullet(self,bullets):
	level1=self.level1
	for b in bullets:
		if b.type==1:
			level1[b.y][b.x]='\033[91m'+"*"+'\033[0m'
		else:
			level1[b.y][b.x]='\033[95m'+"<"+'\033[0m'