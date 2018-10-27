'''main module to run game'''
import signal
import random
import time
import sys
from board import Board
from bullet import Bullet
from getch import _getChUnix as getChar
from alarmexception import AlarmException


def move():
    '''get Keyboard inputs for movements'''
    def alarmhandler(signum, frame):
        '''handles alarm'''
        raise AlarmException

    def user_input(timeout=0.1):
        '''takes user input'''
        signal.signal(signal.SIGALRM, alarmhandler)
        signal.setitimer(signal.ITIMER_REAL, timeout)
        try:
            text = getChar()()
            signal.alarm(0)
            return text
        except AlarmException:
            pass
        signal.signal(signal.SIGALRM, signal.SIG_IGN)
        return ''
    char = user_input()
    return char
TEST = Board()
PLAYER = TEST.player
i = 620
j = 620
l = 8
t = 0
FINALJ = 0
FINALI = 0
POWER = 0
LEVEL2 = 0
VT = 0
TIME1 = 0
S = 0
TEST.print_board(j)
ONBOARD = False
while True:
    sys.stdout.write("\033c")
    #flyer
    if ONBOARD:
        PLAYER.posx += TEST.flyer.dir
        i += TEST.flyer.dir
        j += TEST.flyer.dir

    l = 8
    if time.time() - TEST.flyer.time >= 0.1:
        TEST.flyer.time = time.time()
        TEST.flyer.posx += TEST.flyer.dir
        if TEST.flyer.posx >= 388 and TEST.flyer.dir == 1:
            TEST.flyer.dir = -1
        elif TEST.flyer.posx <= 352 and TEST.flyer.dir == -1:
            TEST.flyer.dir = 1
        if ((TEST.flyer.posx <= PLAYER.posx <= PLAYER.posx + 5
        	    or PLAYER.posx <= TEST.flyer.posx <= PLAYER.posx + 5) and PLAYER.posy + 6 == TEST.flyer.posy):
            ONBOARD = True
        else:
            ONBOARD = False
    # quit
    if PLAYER.life < 0:
        print('\033[95m' + "GAME OVER\nYOUR SCORE=" + str(PLAYER.score) +
              "\nYOUR COINS=" + str(PLAYER.coins) + "\n" + '\033[0m')
        quit()

    if PLAYER.posx == 775:
        print('\033[95m' + "GAME OVER\nYOUR SCORE=" + str(PLAYER.score) +
              "\nYOUR COINS=" + str(PLAYER.coins) + "\n" + '\033[0m')
        quit()

    # gravity
    try:
        if((TEST.level1[PLAYER.posy + 6][PLAYER.posx + 5] != '\033[92m' + "X" + '\033[0m'
        	and TEST.level1[PLAYER.posy + 6][PLAYER.posx + 1] != '\033[92m' + "X" + '\033[0m')
           and (TEST.level1[PLAYER.posy + 6][PLAYER.posx + 5] != 'X'
           	    and TEST.level1[PLAYER.posy + 6][PLAYER.posx + 1] != 'X')):
            G = 1
            PLAYER.posy += 1
        # TEST.print_board(j)

    except:
        PLAYER.posx = 0
        j = 0
        i = 0
        PLAYER.posy = 28
        PLAYER.life -= 1
        # TEST.print_board(j)
    # moves
    CH = move()
    if CH == 'd':
        if ((TEST.level1[PLAYER.posy + 1][PLAYER.posx + 6] != "|"
             and TEST.level1[PLAYER.posy][PLAYER.posx + 5] != "|"
             and TEST.level1[PLAYER.posy + 2][PLAYER.posx + 5] != "|"
             and TEST.level1[PLAYER.posy + 3][PLAYER.posx + 6] != "|"
             and TEST.level1[PLAYER.posy + 4][PLAYER.posx + 5] != "|"
             and TEST.level1[PLAYER.posy + 5][PLAYER.posx + 5] != "|")
                and
                (TEST.level1[PLAYER.posy + 1][PLAYER.posx + 6] != "X"
                 and TEST.level1[PLAYER.posy][PLAYER.posx + 5] != "X"
                 and TEST.level1[PLAYER.posy + 2][PLAYER.posx + 5] != "X"
                 and TEST.level1[PLAYER.posy + 3][PLAYER.posx + 6] != "X"
                 and TEST.level1[PLAYER.posy + 4][PLAYER.posx + 5] != "X"
                 and TEST.level1[PLAYER.posy + 5][PLAYER.posx + 5] != "X")
                and
                (TEST.level1[PLAYER.posy + 1][PLAYER.posx + 6] != '\033[92m' + "X" + '\033[0m'
                 and TEST.level1[PLAYER.posy][PLAYER.posx + 5] != '\033[92m' + "X" + '\033[0m'
                 and TEST.level1[PLAYER.posy + 2][PLAYER.posx + 5] != '\033[92m' + "X" + '\033[0m'
                 and TEST.level1[PLAYER.posy + 3][PLAYER.posx + 6] != '\033[92m' + "X" + '\033[0m'
                 and TEST.level1[PLAYER.posy + 4][PLAYER.posx + 5] != '\033[92m' + "X" + '\033[0m'
                 and TEST.level1[PLAYER.posy + 5][PLAYER.posx + 5] != '\033[92m' + "X" + '\033[0m')
                and j + 75 <= 1000 and PLAYER.level == 1):
            i += 1
            PLAYER.score += 1
            j = i - 75
            if i < 75:
                j = 0
            PLAYER.posx += 1
            # TEST.print_board(j)
        elif PLAYER.level == 2:
            PLAYER.posx += 1
    elif CH == 'a':
        if (TEST.level1[PLAYER.posy + 1][PLAYER.posx - 1] != "|"
                and
                TEST.level1[PLAYER.posy + 1][PLAYER.posx - 1] != "X"
                and
                TEST.level1[PLAYER.posy + 3][PLAYER.posx - 1] != "X"
                and
                TEST.level1[PLAYER.posy + 3][PLAYER.posx - 1] != "|"
                and
                TEST.level1[PLAYER.posy + 1][PLAYER.posx -
                                             1] != '\033[92m' + "X" + '\033[0m'
                and
                TEST.level1[PLAYER.posy + 3][PLAYER.posx -
                                             1] != '\033[92m' + "X" + '\033[0m'
                and
                PLAYER.posx >= 0):
            i -= 1
            j = i - 75
            if i < 75:
                j = 0
            PLAYER.posx -= 1
            # TEST.print_board(j)

    elif CH == 'w' and t < 2:
        for ju in range(PLAYER.posy - 1, PLAYER.posy - 8, -1):
            if ((TEST.level1[ju][PLAYER.posx + 1] == "X")
                    or (TEST.level1[ju][PLAYER.posx + 2] == "X")
                    or (TEST.level1[ju][PLAYER.posx + 3] == "X")
                    or (TEST.level1[ju][PLAYER.posx + 4] == "X")):
                # try:
                for b in TEST.bricks:
                    if PLAYER.posx <= b.posx <= PLAYER.posx + 4 and b.posy == ju - 2:
                        if b.type != -2:
                            PLAYER.coins += 1
                            if b.type == 0:
                                TEST.bricks.remove(b)
                            else:
                                b.type -= 1
                            break
                l = PLAYER.posy - ju
                break
        if PLAYER.posy - l >= 0:
            PLAYER.posy -= l
        # TEST.print_board(j)
        t += 1
    elif CH == 'q':
        print('\033[95m' + "GAME OVER\nYOUR SCORE=" + str(PLAYER.score) +
              "\nYOUR COINS=" + str(PLAYER.coins) + "\n" + '\033[0m')
        quit()
    elif CH == " " and POWER == 1:
        BU = Bullet(PLAYER.posx + 6, PLAYER.posy + 4, 0, 1)
        TEST.bullets.append(BU)
    elif CH == 's' and 629 <= PLAYER.posx <= 638 and LEVEL2 == 0:
        LEVEL2 = 1
        PLAYER.level = 2
        FINALI = i
        FINALJ = j
        i = 0
        j = 0
        PLAYER.posx = 10
        PLAYER.posy = 10
    # ground touch
    try:
        if(TEST.level1[PLAYER.posy + 6][PLAYER.posx + 5] == '\033[92m' + "X" + '\033[0m'
        	  or TEST.level1[PLAYER.posy + 6][PLAYER.posx + 1] == '\033[92m' + "X" + '\033[0m'
        	  or TEST.level1[PLAYER.posy + 6][PLAYER.posx +5] == 'X'
        	  or TEST.level1[PLAYER.posy + 6][PLAYER.posx + 1] == 'X'):
            G = 0
            t = 0
    except:
        PLAYER.life -= 1
        PLAYER.posx = 0
        i = 0
        j = 0
        PLAYER.posy = 28
        # TEST.print_board(j)

    # enemies
    for e in TEST.enemies:
        if e.posx > 799 or e.posx < 0:
            TEST.enemies.remove(e)
        if((e.posx == PLAYER.posx + 5) or (e.posx + 1 == PLAYER.posy))and 26 <= PLAYER.posy <= 28:
            PLAYER.life -= 1
            PLAYER.posx = 0
            PLAYER.score -= 50
            j = 0
            i = 0
            # TEST.print_board(j)

        try:
            if(j <= e.posx <= j + 150 or j - 150 <= e.posx <= j) and time.time() - e.time >= 0.1:
                # erase_enemy(TEST.level1,TEST.enemies)
                e.posx -= e.dir
                e.time = time.time()
                # TEST.print_board(j)
                if e.dir == 1 and TEST.level1[e.posy][e.posx - 1] != " ":
                    if TEST.level1[e.posy][e.posx - 1] == "*":
                        PLAYER.score += 10
                        TEST.enemies.remove(e)
                        # TEST.print_board(j)
                        # break
                    else:
                        e.dir = 0 - e.dir
                elif e.dir == (0 - 1) and TEST.level1[e.posy][e.posx + 3] != " ":
                    e.dir = 0 - e.dir
                if TEST.level1[e.posy + 2][e.posx] != '\033[92m' + "X" + '\033[0m':
                    e.posy += 1
                # TEST.print_board(j)
            if(((PLAYER.posx <= e.posx <= PLAYER.posx + 5
                 or (e.posx <= PLAYER.posx and PLAYER.posx <= e.posx + 2 <= PLAYER.posx + 5))
                    and PLAYER.posy + 6 == e.posy)):
                PLAYER.score += 10
                TEST.enemies.remove(e)
                PLAYER.posy -= 3
        except:
            # pass
            TEST.enemies.remove(e)
            # PLAYER.score+=10
            # TEST.print_board(j)
    # bullets
    for bl in TEST.bullets:
        if time.time() - bl.time >= 0.1:
            bl.time = time.time()
            if bl.posx + 1 < 799:
                bl.posx += 1
            else:
                TEST.bullets.remove(bl)
                break
        if TEST.level1[bl.posy][bl.posx + 1] != " ":
            if bl.posx == TEST.vil.posx and TEST.vil.posy <= bl.posy <= TEST.vil.posy + 10:
                TEST.vil.life -= 1
                PLAYER.score += 50
            TEST.bullets.remove(bl)
        if bl.posx - PLAYER.posx > 150:
            TEST.bullets.remove(bl)

    if PLAYER.level == 2:
        if PLAYER.posx == 145 and 30 <= PLAYER.posy < 40:
            PLAYER.posx = 635
            PLAYER.posy = 17
            PLAYER.level = 1
            i = FINALI
            j = FINALJ
            POWER = 1
            PLAYER.life += 5
        for c in TEST.coins:
            if ((c.posx == PLAYER.posx + 6
            	    or c.posx + 3 == PLAYER.posx
            	    or PLAYER.posx <= c.posx <= PLAYER.posx + 5)
                    and (c.posy == PLAYER.posy + 4 or c.posy == PLAYER.posy + 6)):
                TEST.coins.remove(c)
                PLAYER.coins += 1

    if time.time() - TEST.vil.time >= 1:
        TEST.vil.time = time.time()
        TEST.vil.posx = random.randint(730, 750)
        TEST.vil.posy = random.randint(15, 23)

    if time.time() - TIME1 >= 3 and TEST.alivev == 1:
        TIME1 = time.time()
        EBULLET = Bullet(TEST.vil.posx, TEST.vil.posy + 7, 0, 2)
        TEST.ebul.append(EBULLET)

    for ebullet in TEST.ebul:
        if time.time() - ebullet.time >= 0.1:
            ebullet.posx -= 1
            if ebullet.posx <= 678:
                TEST.ebul.remove(ebullet)
            ebullet.time = time.time()

        if ebullet.posx == PLAYER.posx + 5 and PLAYER.posy <= ebullet.posy <= PLAYER.posy + 6:
            PLAYER.life -= 1
            TEST.ebul.remove(ebullet)

    if TEST.alivev == 1 and PLAYER.posx >= 730:
        PLAYER.posx -= 20
        PLAYER.life -= 1

    if TEST.vil.life < 0:
        TEST.alivev = 0
        if S == 0:
            PLAYER.score += 100
            S = 1

    TEST.print_board(j)
