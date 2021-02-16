#!/usr/local/bin/python3.7
import random


print('************************************')
print('**********Guess The Number**********')
print('************************************')
print()

random_number = random.randrange(1, 21)

def get_user_guess():
  guess = input('Guess a number between 1 and 20 (q to quit): ')
  if guess == 'q':
    print()
    print('Program Ended')
    print()
    exit()
  else:
    try:
      guess = int(guess)
      if (guess <= 0) or (guess > 20):
        get_user_guess()
      else:
        if (guess > random_number):
          print("Your guess is too high")
          get_user_guess()
        elif (guess < random_number):
          print("Your guess is too low")
          get_user_guess()
        else:
            print(f'You guess correctly with the number {random_number}')
    except:
      print()
      print('Did you put in a number between 1 and 20?')
      print()
      get_user_guess()
    
get_user_guess()
