import random

# Taking input for level
while (True):
    try:
        level = int(input("Level: "))
    except ValueError:
        continue
    else:
        if level <= 0:
            continue
        else:
            break

number = random.randint(1, level)

while (True):
    try:
        guess = int(input("Guess: "))
    except ValueError:
        continue
    else:
        if guess <= 0:
            continue
        elif guess > number:
            print("Too large!")
        elif guess < number:
            print("Too small!")
        else:
            print("Just right!")
            break