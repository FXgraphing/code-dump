import random
solution = random.randint(1, 100)
guess = 0

while guess != solution:
    guess = int(input("Guess the number (1-100):"))
    if guess < solution:
        print("Your guess is too low")
    elif guess > solution:
        print("Your guess is too high")
    else:
        print("You guessed the number!")