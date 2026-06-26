# ----------------------------------------
# ========= NUMBER GUESSING GAME =========
# ----------------------------------------


import random

num = random.randint(1, 100)
count = 0

while True:
    guess = int(input("Guess: "))
    count += 1

    if guess == num:
        print("Correct!")
        print("Attempts:", count)
        break
    elif guess < num:
        print("Too Low")
    else:
        print("Too High")