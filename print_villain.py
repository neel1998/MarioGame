def print_villain(self,x,y):
	level1=self.level1
	
	level1[y][x+3]='\033[31m'+"^"+'\033[0m'
	level1[y][x+4]='\033[31m'+"^"+'\033[0m'

	level1[y+1][x+2]='\033[31m'+"^"+'\033[0m'
	level1[y+1][x+3]='\033[31m'+"^"+'\033[0m'
	level1[y+1][x+4]='\033[31m'+"^"+'\033[0m'
	level1[y+1][x+5]='\033[31m'+"^"+'\033[0m'

	level1[y+2][x+1]='\033[34m'+"="+'\033[0m'
	level1[y+2][x+2]='\033[34m'+"="+'\033[0m'
	level1[y+2][x+3]='\033[34m'+"="+'\033[0m'
	level1[y+2][x+4]='\033[34m'+"="+'\033[0m'
	level1[y+2][x+5]='\033[34m'+"="+'\033[0m'
	level1[y+2][x+6]='\033[34m'+"="+'\033[0m'
	
	level1[y+3][x+2]='\033[33m'+"{"+'\033[0m'
	level1[y+3][x+3]='\033[33m'+"o"+'\033[0m'
	level1[y+3][x+4]='\033[33m'+"o"+'\033[0m'
	level1[y+3][x+5]='\033[33m'+")"+'\033[0m'

	level1[y+4][x+1]='\033[35m'+"/"+'\033[0m'
	level1[y+4][x+5]='\033[35m'+"\\"+'\033[0m'
	level1[y+4][x+6]='\033[35m'+"\\"+'\033[0m'
	level1[y+4][x+7]='\033[33m'+">"+'\033[0m'

	level1[y+5][x+1]='\033[35m'+"|"+'\033[0m'
	level1[y+5][x+5]='\033[35m'+"|"+'\033[0m'
	level1[y+5][x+6]='\033[35m'+"|"+'\033[0m'
	level1[y+5][x+7]='\033[33m'+">"+'\033[0m'

	level1[y+6][x+1]='\033[35m'+"|"+'\033[0m'
	level1[y+6][x+5]='\033[35m'+"|"+'\033[0m'
	level1[y+6][x+6]='\033[35m'+"|"+'\033[0m'
	level1[y+6][x+7]='\033[33m'+">"+'\033[0m'

	level1[y+7][x+1]='\033[35m'+"|"+'\033[0m'
	level1[y+7][x+5]='\033[35m'+"|"+'\033[0m'
	level1[y+7][x+6]='\033[35m'+"|"+'\033[0m'
	level1[y+7][x+7]='\033[33m'+">"+'\033[0m'

	level1[y+8][x+1]='\033[35m'+"\\"+'\033[0m'
	level1[y+8][x+5]='\033[35m'+"/"+'\033[0m'
	level1[y+8][x+6]='\033[35m'+"/"+'\033[0m'
	level1[y+8][x+2]='\033[35m'+"_"+'\033[0m'
	level1[y+8][x+3]='\033[35m'+"_"+'\033[0m'
	level1[y+8][x+4]='\033[35m'+"_"+'\033[0m'

	level1[y+8][x+7]='\033[33m'+">"+'\033[0m'

	level1[y+9][x+1]='\033[33m'+"/"+'\033[0m'
	level1[y+9][x+5]='\033[33m'+"\\"+'\033[0m'