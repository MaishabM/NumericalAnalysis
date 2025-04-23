import random

num = random.randint(1,20)
print('Guess a number between 1-20')
while True:
    choice = int(input())
    if choice>num:
        print('Try a lower number.')
    elif choice<num:
        print('Try a higher number.')
    else:
        print('Congratulations! You have successfully guessed the number.')
        break