import random

guess = 0

solutionx = int(input("Pick the lowest number: "))
solutiony = int(input("Pick the highest number: "))

solution = random.randint(solutionx, solutiony)

while guess != solution:
    guess = int(input(f"Guess the number ({solutionx} - {solutiony}): "))
    if guess < solution:
        print("Your guess is too low")
    elif guess > solution:
        print("Your guess is too high")
    else:
        print("You guessed the number!")