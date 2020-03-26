import random
guess = random.randint(1, 10000)
count = 20
print(guess)
while count > 0 :
    user_guess_input = input(print("guess a number between 1 and 10000"))
    count -= 1
    print("you have {} tries left".format(count))
    try:
        user_guess = int(user_guess_input)
    except (TypeError, ValueError):
        print("This is not an integer number. Please enter a valid number")
        continue
    if guess - user_guess > 100:

        print("your guess is too small")

    if user_guess - guess >100:
        print("your guess is too large")

    if guess - user_guess > 10:
        print("your guess is  small")

    if user_guess - guess > 10:
        print("your guess is  large")
    if guess == user_guess:
        print("you won, the number was {}" .format(guess))
        break


if count <= 0:
    print("you lose, the number was {} ".format(guess))
