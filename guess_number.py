import random
import sys
print("Hi! I'm thinking of a random number between 1 and 1 000 000.")
angelica = 0
roger = 0

number = random.randint(1, 1000000)
my_input = input("input \"a\" to guess a number, input \"b\" to quit ")
if my_input.lower()== "a":
    while roger < 300:
        print('Take a guess.')
        angelica = input()
        angelica = int(angelica)
        
        roger = roger + 1
        
        if angelica < number:
            print('Your guess is too low.')
        
        if angelica > number:
            print('Your guess is too high.')
        
        if angelica == number:
            break
else:
    my_input.lower()== "b"
    sys.exit
if angelica == number:
    roger = str(roger)
    print('You guessed my number in ' + roger + ' guesses!')

if angelica != number and roger != 0:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number)
