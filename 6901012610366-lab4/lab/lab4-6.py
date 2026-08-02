from random import randint

x = randint(1, 100)

ans = -1

while ans != x and ans != 0:
    ans = int(input("Enter a number: "))
    if ans == 0:
        print("You have exited the game.")
    elif ans < x:
        print("Your number is too low.")
    elif ans > x:
        print("Your number is too high.")
    else:
        print("Congratulations! You guessed the number.")
    