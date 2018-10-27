'''print villain module'''
def print_villain(self, posx, posy):
    '''print villain function'''
    level1 = self.level1

    level1[posy][posx + 3] = '\033[31m' + "^" + '\033[0m'
    level1[posy][posx + 4] = '\033[31m' + "^" + '\033[0m'

    level1[posy + 1][posx + 2] = '\033[31m' + "^" + '\033[0m'
    level1[posy + 1][posx + 3] = '\033[31m' + "^" + '\033[0m'
    level1[posy + 1][posx + 4] = '\033[31m' + "^" + '\033[0m'
    level1[posy + 1][posx + 5] = '\033[31m' + "^" + '\033[0m'

    level1[posy + 2][posx + 1] = '\033[34m' + "=" + '\033[0m'
    level1[posy + 2][posx + 2] = '\033[34m' + "=" + '\033[0m'
    level1[posy + 2][posx + 3] = '\033[34m' + "=" + '\033[0m'
    level1[posy + 2][posx + 4] = '\033[34m' + "=" + '\033[0m'
    level1[posy + 2][posx + 5] = '\033[34m' + "=" + '\033[0m'
    level1[posy + 2][posx + 6] = '\033[34m' + "=" + '\033[0m'

    level1[posy + 3][posx + 2] = '\033[33m' + "{" + '\033[0m'
    level1[posy + 3][posx + 3] = '\033[33m' + "o" + '\033[0m'
    level1[posy + 3][posx + 4] = '\033[33m' + "o" + '\033[0m'
    level1[posy + 3][posx + 5] = '\033[33m' + ")" + '\033[0m'

    level1[posy + 4][posx + 1] = '\033[35m' + "/" + '\033[0m'
    level1[posy + 4][posx + 5] = '\033[35m' + "\\" + '\033[0m'
    level1[posy + 4][posx + 6] = '\033[35m' + "\\" + '\033[0m'
    level1[posy + 4][posx + 7] = '\033[33m' + ">" + '\033[0m'

    level1[posy + 5][posx + 1] = '\033[35m' + "|" + '\033[0m'
    level1[posy + 5][posx + 5] = '\033[35m' + "|" + '\033[0m'
    level1[posy + 5][posx + 6] = '\033[35m' + "|" + '\033[0m'
    level1[posy + 5][posx + 7] = '\033[33m' + ">" + '\033[0m'

    level1[posy + 6][posx + 1] = '\033[35m' + "|" + '\033[0m'
    level1[posy + 6][posx + 5] = '\033[35m' + "|" + '\033[0m'
    level1[posy + 6][posx + 6] = '\033[35m' + "|" + '\033[0m'
    level1[posy + 6][posx + 7] = '\033[33m' + ">" + '\033[0m'

    level1[posy + 7][posx + 1] = '\033[35m' + "|" + '\033[0m'
    level1[posy + 7][posx + 5] = '\033[35m' + "|" + '\033[0m'
    level1[posy + 7][posx + 6] = '\033[35m' + "|" + '\033[0m'
    level1[posy + 7][posx + 7] = '\033[33m' + ">" + '\033[0m'

    level1[posy + 8][posx + 1] = '\033[35m' + "\\" + '\033[0m'
    level1[posy + 8][posx + 5] = '\033[35m' + "/" + '\033[0m'
    level1[posy + 8][posx + 6] = '\033[35m' + "/" + '\033[0m'
    level1[posy + 8][posx + 2] = '\033[35m' + "_" + '\033[0m'
    level1[posy + 8][posx + 3] = '\033[35m' + "_" + '\033[0m'
    level1[posy + 8][posx + 4] = '\033[35m' + "_" + '\033[0m'

    level1[posy + 8][posx + 7] = '\033[33m' + ">" + '\033[0m'

    level1[posy + 9][posx + 1] = '\033[33m' + "/" + '\033[0m'
    level1[posy + 9][posx + 5] = '\033[33m' + "\\" + '\033[0m'
