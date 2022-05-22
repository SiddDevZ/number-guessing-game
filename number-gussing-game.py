# 
# made by sidd#9999
# 
# 
import random
from colorama import Fore

user_guess = input('how big do u want the number to be: ')
user_guess = int(user_guess)

guesses = 0

random_number = random.randint(0, user_guess)

while True:
    guesses += 1
    user_number = input("enter your number: ")
    user_number = int(user_number)
    if user_number == random_number:
        print(Fore.GREEN + 'you did it')
        print(Fore.WHITE + 'you got it in ' + str(guesses) + Fore.BLUE + ' tries')
        break

    else: print(Fore.RED + 'you got it wrong')
    if user_number > random_number:
        print(Fore.WHITE + 'lower')
    if user_number < random_number:
        print(Fore.WHITE + 'higher')

#    else: print(Fore.GREEN + 'Congratulations!')
