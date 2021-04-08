#TESTING EXERCISE

from random import randint
import sys
# generate a number 1~10
answer = randint(1, 10)

def guessing(number, correct_answer):
    if  0 < number < 11:
        if number == correct_answer:
            print('you are a genius!')
            return True
    else:
        print('hey bozo, I said 1~10')
        return False

if __name__ == '__main__':
    # input from user?
    # check that input is a number 1~10
    while True:
        try:
            guess = int(input('guess a number 1~10:  '))
            if guessing(guess, answer):
                break
        except ValueError as err:
            print('please enter a number')
            continue

