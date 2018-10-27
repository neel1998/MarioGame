'''villain module'''
class Villain:
    '''villain class'''
    def __init__(self, x, y, t, l):
        self.posx = x
        self.posy = y
        self.time = t
        self.life = l
    def get_x(self):
        '''getter fro x'''
        return self.posx
    def get_y(self):
        '''getter for y'''
        return self.posy
