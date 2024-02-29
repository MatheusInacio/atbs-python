import random

print('hello what\'s your name')

name = input()

print('well ' + name + ', I am thinking of a number between 1 and 20')
secretNumber = random.randint(1, 20)

for guessTaken in range(0,7):
    print('take a guess')
    guess = int(input())
    if guess < secretNumber:
        print('your guess is too low')
    elif guess > secretNumber:
        print('your guess is too high')
    else:
        print('good job ' + name + ' you guessed my number in ' + str(guessTaken) + ' guesses')
        break
    
if guess != secretNumber:
    print('nope the number i was thinking of was ' + str(secretNumber))