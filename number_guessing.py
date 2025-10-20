from random import randint
import os

def press_enter():
    input('press enter to continue...')
    
def clear_screan():
    if os.name == 'nt':
        os.system('cls') # windows users
    else:
        os.system('clear') # linux users

def guess():
    clear_screan()
    try:
        your_number = int(input('What\'s your guess?(number between 0 and 10) '))
        if your_number > 10 or your_number < 0:
            print('--> OMG!!')
            print('--> Bro... I said between 0 and 1, not 0 and infinity :/')
            print('--> Go back and TRY AGAIN |: \n')
            press_enter()
            return
            
    except ValueError:
        print('--> You broke math. Congrats...')
        press_enter()
        return

    if your_number == random_number:
        print('Finally! Don\'t spend all your luck at once :)')
        press_enter()
        return
    else:
        print(f"You worked so hard to be wrong… I admire your consistency. (number : {random_number})")
        press_enter()
        return

run = True
while run:
    random_number = randint(0, 10)
    clear_screan()
    print('-' * 20)
    print('1. GUESS THE NUMBER.')
    print('2. Exit...')
    print('-' * 20)
    
    choice = 0
    for attempt in range(3):
        try:
            while choice == 0:
                choice = int(input('Enter your option(1 or 2): '))
                if choice == 1:
                    guess()
                elif choice == 2:
                    run = False
                else:
                    choice = 0
                    print('--> Pro tip: The numbers 1 and 2 are right there on your keyboard. \n')

        except ValueError:
            if attempt == 2:
                clear_screan()
                print('--> Do you know what a number is?')
                press_enter()
                break
            
            print('Enter 1 or 2. \n')    


    