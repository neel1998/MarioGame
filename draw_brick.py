'''function to draw bricks'''
def draw_brick(self, bricks):
    '''draw function'''
    level1 = self.level1
    for i in bricks:
            # for j in i:
        cordx = i.posx
        cordy = i.posy
        btype = i.type
        if btype == -2:
            char = "X"
        else:
            char = '\033[91m' + str(btype) + '\033[0m'
        level1[cordy][cordx] = "X"
        level1[cordy][cordx + 1] = "X"
        level1[cordy][cordx + 2] = "X"
        level1[cordy][cordx + 3] = "X"
        level1[cordy + 1][cordx] = "X"
        level1[cordy + 1][cordx + 3] = "X"
        level1[cordy + 2][cordx] = "X"
        level1[cordy + 2][cordx + 1] = "X"
        level1[cordy + 2][cordx + 2] = "X"
        level1[cordy + 2][cordx + 3] = "X"

        level1[cordy + 1][cordx + 1] = char
        level1[cordy + 1][cordx + 2] = char
