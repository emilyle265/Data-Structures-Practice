import random

def search():
    num_guess = -5
    low = 0
    high = 100

    random_num = random.random() * 100
    guess_input = int(raw_input("Enter a number between 1-100 > "))

    while guess_input != random_num:
        num_guess += 1 
        middle = int(high/2)
        if guess_input > random_num:
            print "too high!"
        elif guess_input < random_num:
            print "too low!"
        elif guess_input == random_num:
            print "you got it!"
            break

        if guess_input >= middle:
            low = middle
        elif guess_input < middle:
            high = middle
        guess_input = int(raw_input("Enter a number between 1-100 > "))

    print "you got it!", random_num, " was the right answer!"
