'''coid module'''
class Coin:
    '''coin class'''
    def __init__(self, x, y):
        self.posx = x
        self.posy = y
    def get_x(self):
        '''getter for x'''
        return self.posx
    def get_y(self):
        '''getter for y'''
        return self.posy
