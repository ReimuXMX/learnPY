#!/usr/bin/env python

import random
import time


def lucky_roll():
    num_player = int(input('Please enter a number between 1 - 10: '))
    if num_player < 1 or num_player > 10:
        print('ERROR')
        exit(1)

    print('AI Rolling...')
    time.sleep(2)
    num_ai = random.randint(1, 10)
    print('AI has rolled ' + str(num_ai))

    if num_player > num_ai:
        print('LUCKY!')
    elif num_player < num_ai:
        print('UNLUCKY...QAQ')


def lucky_end():
    num_opt = input('Quit? (Y/N) ')

    if num_opt == 'Y' or num_opt == 'y':
        exit()
    elif num_opt == 'N' or num_opt == 'n':
        lucky_roll()
    else:
        print('Please enter Y or N!')
        return 0


def lucky_main():
    lucky_roll()
    while True:
        lucky_end()


lucky_main()
