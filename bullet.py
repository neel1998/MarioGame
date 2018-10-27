'''class to make bullet'''
class Bullet():
    '''class to make bullet'''
    def __init__(self, x, y, t, ty):
        self.posx = x
        self.posy = y
        self.time = t
        self.type = ty
    def get_x(self):
        '''getter fro x'''
        return self.posx
    def get_y(self):
        '''getter for y'''
        return self.posy
