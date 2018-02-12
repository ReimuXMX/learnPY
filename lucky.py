#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import time


def luckyRoll():
    numPlayer = int(input('Enter a number between 1 - 10: '))
    if numPlayer > 10 or numPlayer < 1:
        print('ERROR')
        exit(1)

    print('AI rolling...')
    time.sleep(2)
    numAI = random.randint(1, 10)
    print('AI has rolled ' + str(numAI))

    if numPlayer > numAI:
        print('Lucky!!!')
    elif numPlayer < numAI:
        print('Unlucky...QAQ')
    else:
        print('Draw...Again!')
        pass


def luckyEnd():
    opt = str(input('Quit? (Y/N) '))

    if opt == 'Y' or opt == 'y':
        exit()
    elif opt == 'N' or opt == 'n':
        luckyRoll()
    else:
        print('Please enter y or n!')
        return 0


luckyRoll()
while True:
    luckyEnd()
