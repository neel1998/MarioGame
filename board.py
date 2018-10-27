'''board module'''
import time
from mario import Mario
from print_player import print_player
from print_bg import print_background
from brick import brick
from draw_brick import draw_brick
from enemy import Enemy
from print_enemy import print_enemy
from fl import Flyer
from print_bullet import print_bullet
from make_brick import MakeBrick
from coin import Coin
from draw_coin import draw_coin
from write import write
from print_villain import print_villain
from villain import Villain
from win import win


class Board:
    '''board class'''
    bricks = []
    bricks2 = []
    level1 = []
    enemies = []
    bullets = []
    ebul = []

    coins = []

    flyer = Flyer(355, 35, 1, 0)


    player = Mario(620, 28, 5, 0, 0, 1)
    for j in range(40):
        row = []
        for k in range(1000):
            row.append(" ")
        level1.append(row)

    enemy = Enemy(140, 20, 1, 0)
    enemies.append(enemy)

    enemy = Enemy(170, 32, 1, 0)
    enemies.append(enemy)

    enemy = Enemy(150, 32, -1, 0)
    enemies.append(enemy)

    enemy = Enemy(215, 20, 1, 0)
    enemies.append(enemy)

    enemy = Enemy(265, 32, 1, 0)
    enemies.append(enemy)

    enemy = Enemy(580, 32, 1, 0)
    enemies.append(enemy)

    enemy = Enemy(590, 32, 1, 0)
    enemies.append(enemy)

    vil = Villain(730, 22, 0, 10)

    brick(bricks)
    for i in range(70, 130, 5):
        brick = MakeBrick(i, 30, -2)
        bricks2.append(brick)
        coin = Coin(i + 1, 28)
        coins.append(coin)

    for i in range(50, 80, 5):
        brick = MakeBrick(i, 20, -2)
        bricks2.append(brick)
        coin = Coin(i + 1, 18)
        coins.append(coin)
    for i in range(10, 60, 5):
        brick = MakeBrick(i, 30, -2)
        bricks2.append(brick)
        coin = Coin(i + 1, 28)
        coins.append(coin)
    for i in range(100, 140, 5):
        brick = MakeBrick(i, 20, -2)
        bricks2.append(brick)
        coin = Coin(i + 1, 18)
        coins.append(coin)
    time = 0
    alivev = 1
    # print_background(level1)
    # draw_brick(level1,bricks)

    def print_board(self, k):
        '''print board function'''
        if self.player.level == 1:
            print_background(self)
            print_player(self)
            draw_brick(self, self.bricks)
            print_enemy(self)
            print_bullet(self, self.bullets)
            print_bullet(self, self.ebul)

            if self.alivev == 1:
                print_villain(self, self.vil.posx, self.vil.posy)

            if self.alivev == 0:
                win(self)
                # time.sleep(3)

            temp = ""

            string = '\033[93m' + "Life=" + str(self.player.life) + " Score=" + str(
                self.player.score) + " Coins=" + str(self.player.coins) + "\n" + '\033[0m'
            if k >= 550 and self.alivev == 1:
                string += '\033[93m' + "Boss Life=" + \
                    str(self.vil.life) + "\n" + '\033[0m'

            temp += string

            for i in range(40):

                for j in range(k, k + 150, 1):
                    temp += self.level1[i][j]

            print(temp)
        else:
            print_background(self)
            print_player(self)
            draw_brick(self, self.bricks2)
            draw_coin(self, self.coins)

            if time.time() - self.time >= 0.3:
                write(self)
                self.time = time.time()

            temp = ""

            string = '\033[93m' + "Life=" + str(self.player.life) + " Score=" + str(
                self.player.score) + " Coins=" + str(self.player.coins) + "\n" + '\033[0m'

            temp += string

            for i in range(40):

                for j in range(k, k + 150, 1):
                    temp += self.level1[i][j]

            print(temp)
    def dum(self):
        '''dummy method'''
        return self
