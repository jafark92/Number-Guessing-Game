# About Number Guessing Game
# game will display a number of one digit for five seconds and user have to guess that number correctly within three
# chances. After each step user move forward, digits of guess number will be increase.

import random
import time

upgrade = 'y' # to check if user want to move forward
level = 0     # determine level of difficulty

while upgrade == 'y' or upgrade == 'Y': 

    guess_number = random.randint(10 ** level,10**(level+1)) # generate random num according to level of difficulty 

    print ('Are you ready', end = '\r')
    time.sleep(3)                        # wait for 3 seconds

    print (guess_number,'             ', end = '\r')
    time.sleep(5)                                   # display the random number for 5 seconds

    print ('              ', end = '\r')            # to remove the random number from screen

    x = 0 
    while x < 3:                                      # will give user a 3 chance to guess a number
        user = int ( input ('What was the number '))
        if user == guess_number:
            result = 'Win'
            break
        else:
            result = 'Lose'
            
            
        x += 1

    print ('You', result)

    upgrade = input('Want to move forward :"(y/n)"')
    level += 1                                          # increase level of difficulty

print ('Have a good day')
