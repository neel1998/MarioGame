'''print enemy module'''
def print_enemy(self):
    '''print enemy function'''
    level1 = self.level1
    for enemy in self.enemies:
        level1[enemy.posy][enemy.posx] = '\033[91m' + "{" + '\033[0m'
        level1[enemy.posy][enemy.posx + 1] = '\033[91m' + "O" + '\033[0m'
        level1[enemy.posy][enemy.posx + 2] = '\033[91m' + "O" + '\033[0m'
        level1[enemy.posy][enemy.posx + 3] = '\033[91m' + "}" + '\033[0m'
        if enemy.posx % 2:
            level1[enemy.posy + 1][enemy.posx + 1] = '\033[95m' + "/" + '\033[0m'
            level1[enemy.posy + 1][enemy.posx + 2] = '\033[95m' + "\\" + '\033[0m'
        else:
            level1[enemy.posy + 1][enemy.posx + 1] = '\033[95m' + "\\" + '\033[0m'
            level1[enemy.posy + 1][enemy.posx + 2] = '\033[95m' + "/" + '\033[0m'
