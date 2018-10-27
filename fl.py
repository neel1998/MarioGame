'''flyer module'''
class Flyer():
    '''flyer class'''
    def __init__(self, x, y, d, t):
        self.posx = x
        self.posy = y
        self.dir = d
        self.time = t
    def get_x(self):
        '''getter fro x'''
        return self.posx
    def get_y(self):
        '''getter for y'''
        return self.posy
