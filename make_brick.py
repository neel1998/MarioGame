'''class to make bricks'''
class MakeBrick:
    '''class to make bricks'''
    def __init__(self, x, y, t):
        self.posx = x
        self.posy = y
        self.type = t
    def get_x(self):
        '''getter for x'''
        return self.posx
    def get_y(self):
        '''getter for y'''
        return self.posy
