import random

guess = random.randint(1, 10000)
count = 10
while count > 0:
    user_guess_input = input(print("guess a number between 1 and 10000"))
    count -= 1
    print("you have {} tries left".format(count))
    try:
        user_guess = int(user_guess_input)
    except (TypeError, ValueError):
        print("This is not an integer number. Please enter a valid number")
        continue
    diff = abs(user_guess - guess)

    if user_guess < guess and  1<=diff<10 :
        print("your guess is abit small")
    elif user_guess < guess and  10<=diff<100 :
        print("your guess is  small")
    elif user_guess < guess and  100<=diff<10000 :
        print("your guess is too small")
    if user_guess > guess and  1<=diff<10 :
        print("your guess is abit large")
    if user_guess > guess and  10<=diff<100 :
        print("your guess is large")
    if user_guess > guess and  100<=diff<10000 :
        print("your guess is too large")
    else:
        if user_guess == guess:
            print("you won, the number was {}".format(guess))
            break

if count <= 0:
    print("you lose, the number was {} ".format(guess))
