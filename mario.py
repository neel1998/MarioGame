'''mario module'''
class Mario:
    '''mario class'''
    def __init__(self, x, y, l, c, s, level):
        self.posx = x
        self.posy = y
        self.life = l
        self.coins = c
        self.score = s
        self.level = level
    def get_x(self):
        '''getter fro x'''
        return self.posx
    def get_y(self):
        '''getter for y'''
        return self.posy
        