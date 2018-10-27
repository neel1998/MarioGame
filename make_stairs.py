'''stairs module'''
def make_stairs(self, posx, height, dire):
    '''function stairs'''
    level1 = self.level1
    if dire == 1:
        for i in range(33, 33 - 3 * height + 1, -3):
            for j in range(posx + 4 * (int((33 - i) / 3)), posx + 4 * height + 1, 1):
                level1[i][j] = '\033[92m' + "X" + '\033[0m'
                level1[i - 1][j] = '\033[92m' + "X" + '\033[0m'
                level1[i - 2][j] = '\033[92m' + "X" + '\033[0m'
    else:
        for i in range(33, 33 - 3 * height + 1, -3):
            for j in range(posx, posx + 4 * height - 4 * (int((33 - i) / 3)) + 1, 1):
                level1[i][j] = '\033[92m' + "X" + '\033[0m'
                level1[i - 1][j] = '\033[92m' + "X" + '\033[0m'
                level1[i - 2][j] = '\033[92m' + "X" + '\033[0m'
