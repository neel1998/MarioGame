'''print bullet module'''
def print_bullet(self, bullets):
    '''print bullet function'''
    level1 = self.level1
    for bul in bullets:
        if bul.type == 1:
            level1[bul.posy][bul.posx] = '\033[91m' + "*" + '\033[0m'
        else:
            level1[bul.posy][bul.posx] = '\033[95m' + "<" + '\033[0m'
