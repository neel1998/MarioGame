'''print player module'''
def print_player(self):
    '''print player function'''
    level1 = self.level1
    cordx = self.player.posx
    cordy = self.player.posy
    level1[cordy][cordx + 1] = '\033[91m' + "=" + '\033[0m'
    level1[cordy][cordx + 2] = '\033[91m' + "=" + '\033[0m'
    level1[cordy][cordx + 3] = '\033[91m' + "=" + '\033[0m'
    level1[cordy][cordx + 4] = '\033[91m' + "=" + '\033[0m'
    level1[cordy + 1][cordx] = '\033[91m' + "=" + '\033[0m'
    level1[cordy + 1][cordx + 1] = '\033[91m' + "=" + '\033[0m'
    level1[cordy + 1][cordx + 2] = '\033[91m' + "=" + '\033[0m'
    level1[cordy + 1][cordx + 3] = '\033[91m' + "=" + '\033[0m'
    level1[cordy + 1][cordx + 4] = '\033[91m' + "=" + '\033[0m'
    level1[cordy + 1][cordx + 5] = '\033[91m' + "=" + '\033[0m'

    level1[cordy + 2][cordx + 1] = '\033[93m' + "[" + '\033[0m'
    level1[cordy + 2][cordx + 2] = '\033[93m' + "o" + '\033[0m'
    level1[cordy + 2][cordx + 3] = '\033[93m' + "o" + '\033[0m'
    level1[cordy + 2][cordx + 4] = '\033[93m' + "]" + '\033[0m'
    level1[cordy + 3][cordx] = '\033[93m' + "/" + '\033[0m'

    level1[cordy + 3][cordx + 1] = '\033[94m' + "M" + '\033[0m'
    level1[cordy + 3][cordx + 2] = '\033[94m' + "M" + '\033[0m'
    level1[cordy + 3][cordx + 3] = '\033[94m' + "M" + '\033[0m'
    level1[cordy + 3][cordx + 4] = '\033[94m' + "M" + '\033[0m'
    level1[cordy + 3][cordx + 5] = '\033[93m' + "\\" + '\033[0m'

    level1[cordy + 4][cordx + 1] = '\033[94m' + "M" + '\033[0m'
    level1[cordy + 4][cordx + 2] = '\033[94m' + "M" + '\033[0m'
    level1[cordy + 4][cordx + 3] = '\033[94m' + "M" + '\033[0m'
    level1[cordy + 4][cordx + 4] = '\033[94m' + "M" + '\033[0m'
    if cordx % 2:
        level1[cordy + 5][cordx + 1] = '\033[93m' + "/" + '\033[0m'
        level1[cordy + 5][cordx + 4] = '\033[93m' + "\\" + '\033[0m'
    else:
        level1[cordy + 5][cordx + 1] = '\033[93m' + "\\" + '\033[0m'
        level1[cordy + 5][cordx + 4] = '\033[93m' + "/" + '\033[0m'
