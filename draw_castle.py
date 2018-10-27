'''module to draw castle'''
def draw_castle(self, posx, posy):
    '''function to draw castle'''
    level1 = self.level1
    for i in range(posy, 34, 1):
        for j in range(posx, posx + 40, 1):
            level1[i][j] = '\033[93m' + "#" + '\033[0m'

    for i in range(posy - 7, posy, 1):
        for j in range(posx + 10, posx + 30, 1):
            level1[i][j] = '\033[93m' + "#" + '\033[0m'

    for i in range(posy - 12, posy - 7, 1):
        level1[i][posx + 20] = '\033[93m' + "#" + '\033[0m'

    for i in range(posy - 5, posy, 1):
        level1[i][posx] = '\033[93m' + "#" + '\033[0m'
        level1[i][posx + 39] = '\033[93m' + "#" + '\033[0m'

    for i in range(posy - 5, posy - 2, 1):
        for j in range(posx + 1, posx + 5, 1):
            level1[i][j] = '\033[91m' + "M" + '\033[0m'

    for i in range(posy - 12, posy - 9, 1):
        for j in range(posx + 21, posx + 26, 1):
            level1[i][j] = '\033[91m' + "M" + '\033[0m'

    for i in range(posy - 5, posy - 2, 1):
        for j in range(posx + 40, posx + 44, 1):
            level1[i][j] = '\033[91m' + "M" + '\033[0m'

    for i in range(posy, 34, 1):
        for j in range(posx + 17, posx + 24, 1):
            level1[i][j] = " "

    for i in range(posy + 5, 34, 1):
        for j in range(posx + 5, posx + 11, 1):
            level1[i][j] = " "
    for i in range(posy + 5, 34, 1):
        for j in range(posx + 30, posx + 36, 1):
            level1[i][j] = " "
