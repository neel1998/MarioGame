'''module to draw coin'''
def draw_coin(self, coins):
    '''function to draw coin'''
    level1 = self.level1
    for i in coins:
        level1[i.posy][i.posx] = '\033[93m' + "(" + '\033[0m'
        level1[i.posy][i.posx + 1] = '\033[93m' + "$" + '\033[0m'
        level1[i.posy][i.posx + 2] = '\033[93m' + ")" + '\033[0m'
